from datetime import datetime
from .category import Category
from .exceptions import ValidationError, InvalidAmountError

class Transaction:
    """Класс финансовой операции с защищенными свойствами."""
    def __init__(self, amount: float, category: Category, date: datetime = None, description: str = ""):
        self.amount = amount
        self.category = category
        
        if date is not None and not isinstance(date, datetime):
            raise ValidationError("Дата должна быть объектом datetime.")
        self._date = date if date else datetime.now()
        
        if not isinstance(description, str):
            raise ValidationError("Описание должно быть строкой.")
        self._description = description

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value: float):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
            raise InvalidAmountError("Сумма операции должна быть положительным числом.")
        self._amount = float(value)

    @property
    def category(self) -> Category:
        return self._category

    @category.setter
    def category(self, value: Category):
        if not isinstance(value, Category):
            raise ValidationError("Передан некорректный объект категории.")
        self._category = value
        
    @property
    def date(self) -> datetime:
        return self._date
        
    @property
    def description(self) -> str:
        return self._description