from src.finance_manager.account import Account
from src.finance_manager.category import Category
from src.finance_manager.transaction import Transaction
from src.finance_manager.report import Report


def create_test_report():
    account = Account("Основной счёт", 0)

    salary = Category("Зарплата", "income")
    freelance = Category("Подработка", "income")
    food = Category("Продукты", "expense")
    transport = Category("Транспорт", "expense")

    account.add_transaction(Transaction(50000, salary))
    account.add_transaction(Transaction(10000, freelance))
    account.add_transaction(Transaction(5000, food))
    account.add_transaction(Transaction(2000, transport))

    return Report(account)


def test_total_income():
    report = create_test_report()

    assert report.get_total_income() == 60000


def test_total_expense():
    report = create_test_report()

    assert report.get_total_expense() == 7000


def test_balance_difference():
    report = create_test_report()

    assert report.get_balance_difference() == 53000


def test_group_by_category():
    report = create_test_report()

    result = report.group_by_category()

    assert result == {
        "Зарплата": 50000,
        "Подработка": 10000,
        "Продукты": 5000,
        "Транспорт": 2000
    }


def test_empty_report():
    account = Account("Пустой счёт")
    report = Report(account)

    assert report.get_total_income() == 0
    assert report.get_total_expense() == 0
    assert report.get_balance_difference() == 0
    assert report.group_by_category() == {}
