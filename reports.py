
"""
Reports Module
Generates financial reports.
"""

from datetime import datetime
from statistics import mean


def show_report(expenses, budget):
    """Display the complete monthly expense report."""

    print("\n" + "=" * 45)
    print("       PERSONAL EXPENSE REPORT")
    print("=" * 45)

    print("Report Date:", datetime.now().strftime("%d-%m-%Y"))

    if not expenses:
        print("No expenses recorded.")
        return

    amounts = [item["amount"] for item in expenses]

    total = sum(amounts)

    print("\nExpense Details:")

    for item in expenses:
        print(
            f'{item["name"]:<15} '
            f'Rs. {item["amount"]:>8.2f} '
            f'({item["category"]})'
        )

    print("-" * 45)

    print(f"Monthly Budget : Rs. {budget:.2f}")
    print(f"Total Expense  : Rs. {total:.2f}")
    print(f"Average Expense: Rs. {mean(amounts):.2f}")
    print(f"Remaining      : Rs. {budget - total:.2f}")

    if total > budget:
        print("Warning: Monthly budget exceeded!")
    else:
        print("Status: Within budget!")

    print("=" * 45)
