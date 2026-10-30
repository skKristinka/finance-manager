import pytest
from datetime import datetime

from src.finance_manager.transaction import Transaction
from src.finance_manager.category import Category


def test_transaction_creation():
    category = Category("Зарплата", "income")
    transaction = Transaction(5000, category, description="Аванс")

    assert transaction.amount == 5000
    assert transaction.category == category
    assert transaction.description == "Аванс"


def test_transaction_with_date():
    category = Category("Продукты", "expense")
    date = datetime(2026, 10, 30)

    transaction = Transaction(1500, category, date)

    assert transaction.date == date


def test_transaction_default_date():
    category = Category("Зарплата", "income")

    transaction = Transaction(5000, category)

    assert isinstance(transaction.date, datetime)


def test_transaction_invalid_amount():
    category = Category("Продукты", "expense")

    with pytest.raises(ValueError):
        Transaction(0, category)

    with pytest.raises(ValueError):
        Transaction(-100, category)


def test_transaction_invalid_category():
    with pytest.raises(ValueError):
        Transaction(1000, "Продукты")


def test_transaction_empty_description():
    category = Category("Зарплата", "income")

    transaction = Transaction(5000, category)

    assert transaction.description == ""
