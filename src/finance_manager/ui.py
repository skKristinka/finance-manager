"""Консольный интерфейс Lavender Dream для менеджера личных финансов."""
from __future__ import annotations
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from .account import Account
from .category import Category
from .report import Report
from .transaction import Transaction

DATA_FILE = Path(os.environ.get("FINANCE_MANAGER_DATA", "data/transactions.json"))
LAVENDER, BLUE, PINK, RESET = "\033[38;5;183m", "\033[38;5;153m", "\033[38;5;218m", "\033[0m"

def _paint(text: str, color: str) -> str:
    if os.getenv("NO_COLOR") is not None or not sys.stdout.isatty():
        return text
    return f"{color}{text}{RESET}"

class FinanceApp:
    """Меню, проверка ввода и сохранение операций в JSON."""
    def __init__(self, data_file: Path | str = DATA_FILE):
        self.data_file = Path(data_file)
        self.account = Account("Личный счёт")
        self._history: list[dict] = []
        self._load()

    def _load(self) -> None:
        if not self.data_file.exists():
            return
        try:
            records = json.loads(self.data_file.read_text(encoding="utf-8"))
            if not isinstance(records, list):
                raise ValueError("ожидался список операций")
            for record in records:
                category = Category(record["category"], record["type"])
                transaction = Transaction(float(record["amount"]), category,
                    datetime.fromisoformat(record["date"]), record.get("description", ""))
                self.account.add_transaction(transaction)
                self._history.append(record)
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            print(f"Не удалось загрузить историю: {exc}")
            self.account = Account("Личный счёт")
            self._history = []

    def _save(self) -> None:
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.data_file.with_suffix(self.data_file.suffix + ".tmp")
        temporary.write_text(json.dumps(self._history, ensure_ascii=False, indent=2), encoding="utf-8")
        temporary.replace(self.data_file)

    @staticmethod
    def _read_amount(prompt: str) -> float | None:
        while True:
            raw = input(prompt).strip().replace(",", ".")
            if raw.lower() in {"q", "отмена", "cancel"}:
                return None
            try:
                amount = float(raw)
                if amount > 0:
                    return amount
            except ValueError:
                pass
            print("Введите положительную сумму числом (например, 1250.50) или q для отмены.")

    def add_operation(self, operation_type: str) -> None:
        label = "дохода" if operation_type == "income" else "расхода"
        amount = self._read_amount(f"Сумма {label} (q — отмена): ")
        if amount is None:
            print("Операция отменена.")
            return
        category_name = input("Категория: ").strip()
        if not category_name:
            print("Категория не может быть пустой.")
            return
        description = input("Описание (необязательно): ").strip()
        try:
            category = Category(category_name, operation_type)
            transaction = Transaction(amount, category, datetime.now(), description)
            self.account.add_transaction(transaction)
            self._history.append({"amount": amount, "category": category_name,
                "type": operation_type, "date": transaction.date.isoformat(timespec="seconds"),
                "description": description})
            self._save()
            print(_paint(f"Операция сохранена: {amount:.2f} ₽", BLUE))
        except (ValueError, OSError) as exc:
            print(f"Не удалось сохранить операцию: {exc}")

    def show_balance(self) -> None:
        print(_paint(f"\nБаланс: {self.account.get_balance():,.2f} ₽".replace(",", " "), LAVENDER))

    def show_report(self) -> None:
        report = Report(self.account)
        print(_paint("\n── Финансовый отчёт ──", LAVENDER))
        print(f"Доходы:  {report.get_total_income():,.2f} ₽".replace(",", " "))
        print(f"Расходы: {report.get_total_expense():,.2f} ₽".replace(",", " "))
        print(f"Разница: {report.get_balance_difference():,.2f} ₽".replace(",", " "))
        groups = report.group_by_category()
        if groups:
            print("\nПо категориям:")
            for name, total in sorted(groups.items()):
                print(f"  • {name}: {total:,.2f} ₽".replace(",", " "))

    def show_history(self) -> None:
        print(_paint("\n── История операций ──", LAVENDER))
        if not self._history:
            print("Пока операций нет.")
            return
        for item in self._history:
            sign = "+" if item["type"] == "income" else "−"
            date = datetime.fromisoformat(item["date"]).strftime("%d.%m.%Y %H:%M")
            print(f"{date} | {sign}{float(item['amount']):.2f} ₽ | {item['category']} | {item.get('description', '')}")

    def run(self) -> None:
        print(_paint("\n♡ Lavender Dream — менеджер личных финансов ♡", LAVENDER))
        while True:
            print(_paint("\n╭── Главное меню ──╮", BLUE))
            print(" 1. Добавить доход\n 2. Добавить расход\n 3. Текущий баланс\n 4. Финансовый отчёт\n 5. История операций\n 0. Выход")
            choice = input(_paint("Выберите пункт: ", PINK)).strip()
            if choice == "1":
                self.add_operation("income")
            elif choice == "2":
                self.add_operation("expense")
            elif choice == "3":
                self.show_balance()
            elif choice == "4":
                self.show_report()
            elif choice == "5":
                self.show_history()
            elif choice == "0":
                print("До встречи! Ваши данные сохранены ♡")
                return
            else:
                print("Неизвестный пункт. Выберите число от 0 до 5.")

def main() -> None:
    FinanceApp().run()

if __name__ == "__main__":
    main()
