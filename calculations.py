
"""
Calculations Module
Handles expense calculations.
"""


def calculate_total(*amounts):
    """Calculate the total of multiple expense amounts."""

    return sum(amounts)


def calculate_remaining_budget(budget, total_expense):
    """Calculate the remaining monthly budget."""

    return budget - total_expense


def calculate_average(amounts):
    """Calculate average expense."""

    if not amounts:
        return 0

    return sum(amounts) / len(amounts)


# Lambda function to calculate 10% discount
discount = lambda amount: amount * 0.90


# Lambda function to calculate 5% tax
tax = lambda amount: amount * 1.05


def apply_discount(amounts):
    """Apply discount to every expense using map()."""

    return list(map(discount, amounts))


def apply_tax(amounts):
    """Apply tax to every expense using map()."""

    return list(map(tax, amounts))
