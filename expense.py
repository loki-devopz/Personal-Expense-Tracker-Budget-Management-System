
"""
Expense Module
Handles expense creation and storage.
"""

# Store expenses
expenses = []


def add_expense(name, amount, category):
    """Add a new expense to the expense list."""

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print(f"{name} expense added successfully!")


def get_expenses():
    """Return all recorded expenses."""

    return expenses


def add_multiple_expenses(*expense_list):
    """Add multiple expenses using variable arguments."""

    for expense in expense_list:
        expenses.append(expense)

    print("Multiple expenses added successfully!")
