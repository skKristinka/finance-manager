class Category:
    """
    Класс для категории (например, 'Еда', 'Зарплата').
    type: 'income' (доход) или 'expense' (расход).
    """
    def __init__(self, name: str, type: str):
        if not name or not isinstance(name, str):
            raise ValueError("Название категории не может быть пустым.")
        if type not in ('income', 'expense'):
            raise ValueError("Тип категории должен быть 'income' или 'expense'.")
        
        self.name = name
        self.type = type