from .transaction import Transaction

class Account:
    """
    Класс финансового счета пользователя.
    """
    def __init__(self, name: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.name = name
        self.balance = initial_balance
        self.transactions = []

    def get_balance(self) -> float:
        """Возвращает текущий баланс."""
        return self.balance

    def add_transaction(self, transaction: Transaction):
        """Добавляет операцию и обновляет баланс."""
        self.transactions.append(transaction)
        
        if transaction.category.type == 'income':
            self.balance += transaction.amount
        elif transaction.category.type == 'expense':
            self.balance -= transaction.amount

    def deposit(self, amount: float):
        """Пополнение средств."""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля.")
        self.balance += amount

    def withdraw(self, amount: float):
        """Списание средств."""
        if amount <= 0:
            raise ValueError("Сумма списания должна быть больше нуля.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount