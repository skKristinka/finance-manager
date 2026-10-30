class FinanceError(Exception):
    """Базовый класс для финансовых исключений."""
    pass

class ValidationError(FinanceError):
    """Ошибка валидации входных данных (типы, пустота)."""
    pass

class InvalidAmountError(FinanceError):
    """Ошибка некорректной суммы (<= 0)."""
    pass

class InsufficientFundsError(FinanceError):
    """Ошибка нехватки средств на балансе."""
    pass