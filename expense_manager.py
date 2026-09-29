from models import Expense
from storage import load_expenses, save_expenses
from validators import validate_category, validate_amount


class ExpenseManager:

    def __init__(self):
        self.expenses = load_expenses()

    def add_expense(self, category, amount, note):
        if not validate_category(category):
            return False, "Category cannot be empty."

        if not validate_amount(amount):
            return False, "Amount must be a positive number."

        expense = Expense(
            category.strip(),
            float(amount),
            note.strip()
        )

        self.expenses.append(expense.to_dict())
        save_expenses(self.expenses)

        return True, "Expense added successfully."

    def get_expenses(self):
        return self.expenses

    def delete_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            return False, "Invalid expense number."

        self.expenses.pop(index)
        save_expenses(self.expenses)

        return True, "Expense deleted successfully."
    