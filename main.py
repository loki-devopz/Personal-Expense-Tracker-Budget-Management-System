
"""
Personal Expense Tracker
Main Application
"""

# Import custom modules
from expense import add_expense, get_expenses
from calculations import (
    calculate_total,
    calculate_remaining_budget,
    apply_discount,
    apply_tax
)
from reports import show_report

# Global variable
monthly_budget = 0


def display_menu():
    """Display the application menu."""

    print("\n===== EXPENSE TRACKER =====")
    print("1. Set Monthly Budget")
    print("2. Add Expense")
    print("3. View Expense Report")
    print("4. Apply Discount")
    print("5. Calculate Tax")
    print("6. Exit")


def set_budget():
    """Set the monthly spending budget."""

    global monthly_budget

    monthly_budget = float(input("Enter monthly budget: "))

    print(f"Budget set to Rs. {monthly_budget:.2f}")


def add_new_expense():
    """Collect expense details from the user."""

    name = input("Enter expense name: ").strip()

    amount = float(input("Enter expense amount: "))

    category = input("Enter expense category: ").strip()

    add_expense(name, amount, category)


def show_expense_report():
    """Display the expense report."""

    expenses = get_expenses()

    show_report(expenses, monthly_budget)


def process_discount():
    """Apply a 10% discount to recorded expenses."""

    expenses = get_expenses()

    amounts = [item["amount"] for item in expenses]

    discounted = apply_discount(amounts)

    print("\nDiscounted Expenses:")

    for amount in discounted:
        print(f"Rs. {amount:.2f}")


def process_tax():
    """Calculate expenses after applying 5% tax."""

    expenses = get_expenses()

    amounts = [item["amount"] for item in expenses]

    taxed = apply_tax(amounts)

    print("\nExpenses Including Tax:")

    for amount in taxed:
        print(f"Rs. {amount:.2f}")


# Main program
while True:

    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        set_budget()

    elif choice == "2":
        add_new_expense()

    elif choice == "3":
        show_expense_report()

    elif choice == "4":
        process_discount()

    elif choice == "5":
        process_tax()

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
