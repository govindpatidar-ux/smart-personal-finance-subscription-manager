from storage import load_expenses
from utils import print_header, format_currency, pause


def monthly_analytics():

    print_header("MONTHLY ANALYTICS")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        pause()
        return

    total_expense = 0
    category_totals = {}

    highest_expense = expenses[0]

    # ================= CALCULATIONS =================

    for expense in expenses:

        amount = float(expense['amount'])

        total_expense += amount

        category = expense['category']

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

        if amount > float(highest_expense['amount']):
            highest_expense = expense

    # ================= SUMMARY =================

    print("=" * 60)

    print(
        f"{'Total Expenses':<30}"
        f": {format_currency(total_expense)}"
    )

    print(
        f"{'Total Records':<30}"
        f": {len(expenses)}"
    )

    print("=" * 60)

    # ================= CATEGORY ANALYTICS =================

    print("\nCATEGORY WISE SPENDING\n")

    print("-" * 60)

    print(
        f"{'Category':<20}"
        f"{'Amount':<15}"
        f"{'Usage'}"
    )

    print("-" * 60)

    for category, amount in category_totals.items():

        # Progress Bar
        bar = int(amount / 500)

        print(
            f"{category:<20}"
            f"{format_currency(amount):<15}"
            f"{bar}"
        )

    print("-" * 60)

    # ================= HIGHEST EXPENSE =================

    print("\nHIGHEST EXPENSE\n")

    print("-" * 60)

    print(
        f"Title      : {highest_expense['title']}"
    )

    print(
        f"Amount     : "
        f"{format_currency(highest_expense['amount'])}"
    )

    print(
        f"Category   : "
        f"{highest_expense['category']}"
    )

    print("-" * 60)

    # ================= AVERAGE =================

    average = total_expense / len(expenses)

    print(
        f"\nAverage Expense : "
        f"{format_currency(average)}"
    )

    # ================= STATUS =================

    if total_expense > 30000:

        print("\nSTATUS : HIGH SPENDING")

    elif total_expense > 15000:

        print("\nSTATUS : MODERATE SPENDING")

    else:

        print("\nSTATUS : HEALTHY SPENDING")

    pause()