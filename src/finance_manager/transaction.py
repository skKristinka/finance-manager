from datetime import datetime
from .category import Category

class Transaction:
    """
    Класс для одной финансовой операции.
    """
    def __init__(self, amount: float, category: Category, date: datetime = None, description: str = ""):
        if amount <= 0:
            raise ValueError("Сумма операции должна быть больше нуля.")
        if not isinstance(category, Category):
            raise ValueError("Категория должна быть объектом класса Category.")
            
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now()
        self.description = description