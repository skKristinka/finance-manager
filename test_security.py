import pytest
from src.finance_manager.account import Account

def test_negative_balance_creation():
    """Проверка: нельзя создать счет с отрицательным балансом."""
    with pytest.raises(Exception):
        Account("Тест", -500)

def test_overdraft_protection():
    """Проверка: нельзя снять сумму, превышающую текущий баланс."""
    acc = Account("Тест2", 100)
    with pytest.raises(Exception):
        acc.withdraw(5000)

def test_positive_scenario():
    """Проверка: корректное снятие средств работает штатно."""
    acc = Account("Тест3", 1000)
    acc.withdraw(500)
    assert acc.balance == 500