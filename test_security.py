from src.finance_manager.account import Account
from src.finance_manager.category import Category
from src.finance_manager.transaction import Transaction

def run_tests():
    print("--- QA: Проверка работы системы ---\n")
    try:
        acc = Account("Тест", -500)
        # Если программа не выдаст ошибку, она напечатает это:
        print(f"БАГ 1: Счет успешно создан с отрицательным балансом: {acc.balance}")
    except Exception as e:
        print(f"ОК: Ошибка перехвачена: {e}")

    try:
        acc2 = Account("Тест2", 100)
        acc2.withdraw(5000)
        # Если овердрафт не заблокирован, баланс уйдет в минус:
        print(f"БАГ 2: Удалось снять 5000 при балансе 100. Итог: {acc2.balance}")
    except Exception as e:
        print(f"ОК: Защита от снятия сработала: {e}")

if __name__ == "__main__":
    run_tests()