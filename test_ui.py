import json
from datetime import datetime
from finance_manager.account import Account
from finance_manager.category import Category
from finance_manager.report import Report
from finance_manager.transaction import Transaction
from finance_manager.ui import FinanceApp

def test_account_and_report_public_api():
    account = Account("Тест")
    account.add_transaction(Transaction(100, Category("Зарплата", "income"), datetime(2026, 1, 1)))
    account.add_transaction(Transaction(25, Category("Кофе", "expense"), datetime(2026, 1, 2)))
    report = Report(account)
    assert account.get_balance() == 75
    assert report.get_total_income() == 100
    assert report.get_total_expense() == 25
    assert report.get_balance_difference() == 75

def test_load_saved_history_and_balance(tmp_path):
    file = tmp_path / "transactions.json"
    file.write_text(json.dumps([{"amount": 250, "category": "Подработка", "type": "income",
        "date": "2026-01-10T12:00:00", "description": "Тест"}]), encoding="utf-8")
    app = FinanceApp(file)
    assert app.account.get_balance() == 250
    assert len(app._history) == 1

def test_add_operation_saves_json(tmp_path, monkeypatch):
    app = FinanceApp(tmp_path / "data.json")
    answers = iter(["125,50", "Еда", "Обед"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    app.add_operation("expense")
    saved = json.loads((tmp_path / "data.json").read_text(encoding="utf-8"))
    assert saved[0]["amount"] == 125.5
    assert saved[0]["type"] == "expense"
    assert app.account.get_balance() == -125.5

def test_invalid_amount_retries_and_cancel(tmp_path, monkeypatch):
    app = FinanceApp(tmp_path / "data.json")
    answers = iter(["-5", "abc", "q"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    assert app._read_amount("Сумма: ") is None
    assert app.account.get_balance() == 0
