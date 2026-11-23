# Personal Expense Tracker & Budget Management System

A console-based Python application for recording expenses, managing a monthly budget, and generating a simple financial report.

## Features

- Set a monthly budget
- Add expenses with a name, amount, and category
- View expense details, total spending, average expense, and remaining budget
- Receive a warning when spending exceeds the monthly budget
- Apply a 10% discount to recorded expenses
- Calculate expenses after applying a 5% tax
- Display the report date and expense category information

## Project Structure

```text
.
|-- README.md
`-- ExpenseTracker/
    |-- main.py
    |-- expense.py
    |-- calculations.py
    `-- reports.py
```

- `main.py` - Runs the interactive menu and coordinates the application.
- `expense.py` - Stores and manages expense records.
- `calculations.py` - Calculates totals, averages, discounts, and taxes.
- `reports.py` - Formats and displays the financial report.

## Requirements

- Python 3.x

No external packages are required.

## Getting Started

1. Open a terminal in the project directory.
2. Change to the application folder:

```bash
cd ExpenseTracker
```

3. Run the program:

```bash
python main.py
```

## Using the Application

The main menu provides the following options:

| Option | Action |
|---|---|
| 1 | Set the monthly budget |
| 2 | Add an expense |
| 3 | View the expense report |
| 4 | Apply a 10% discount and display adjusted amounts |
| 5 | Apply a 5% tax and display adjusted amounts |
| 6 | Exit the application |

Enter numeric menu choices and provide values in the prompts. Amounts are displayed in Indian rupees (`Rs.`).

## Example

```text
===== EXPENSE TRACKER =====
1. Set Monthly Budget
2. Add Expense
3. View Expense Report
4. Apply Discount
5. Calculate Tax
6. Exit

Enter your choice: 1
Enter monthly budget: 20000
Budget set to Rs. 20000.00
```

## Data Storage

Expenses are stored in memory while the program is running. Data is reset whenever the application is restarted.
