import pytest
from src.finance_manager.account import Account


def test_account_creation():
    account = Account("Основной счёт", 1000)

    assert account.name == "Основной счёт"
    assert account.get_balance() == 1000


def test_account_initial_balance_zero():
    account = Account("Мой счёт")

    assert account.get_balance() == 0


def test_negative_initial_balance():
    with pytest.raises(ValueError):
        Account("Мой счёт", -100)


def test_deposit():
    account = Account("Мой счёт", 1000)

    account.deposit(500)

    assert account.get_balance() == 1500


def test_deposit_invalid_amount():
    account = Account("Мой счёт", 1000)

    with pytest.raises(ValueError):
        account.deposit(0)

    with pytest.raises(ValueError):
        account.deposit(-100)


def test_withdraw():
    account = Account("Мой счёт", 1000)

    account.withdraw(300)

    assert account.get_balance() == 700


def test_withdraw_insufficient_funds():
    account = Account("Мой счёт", 100)

    with pytest.raises(ValueError):
        account.withdraw(200)


def test_withdraw_invalid_amount():
    account = Account("Мой счёт", 1000)

    with pytest.raises(ValueError):
        account.withdraw(0)

    with pytest.raises(ValueError):
        account.withdraw(-100)
