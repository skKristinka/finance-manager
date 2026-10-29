from .account import Account

class Report:
    """
    Класс для формирования финансовых отчетов.
    """
    def __init__(self, account: Account):
        self.account = account

    def get_total_income(self) -> float:
        """Считает общую сумму доходов."""
        return sum(t.amount for t in self.account.transactions if t.category.type == 'income')

    def get_total_expense(self) -> float:
        """Считает общую сумму расходов."""
        return sum(t.amount for t in self.account.transactions if t.category.type == 'expense')

    def get_balance_difference(self) -> float:
        """Считает разницу между доходами и расходами."""
        return self.get_total_income() - self.get_total_expense()

    def group_by_category(self) -> dict:
        """Группирует операции по названиям категорий."""
        grouped = {}
        for t in self.account.transactions:
            cat_name = t.category.name
            if cat_name not in grouped:
                grouped[cat_name] = 0.0
            grouped[cat_name] += t.amount
        return grouped