from exceptions import ValidationError

class Category:
    """Класс для категории с защитой данных."""
    def init(self, name: str, type: str):
        self.name = name
        self.type = type

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValidationError("Название категории должно быть непустой строкой.")
        self._name = value.strip()

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        if value not in ('income', 'expense'):
            raise ValidationError("Тип категории должен быть строго 'income' или 'expense'.")
        self._type = value