from storage import load_expenses
from utils import print_header, format_currency, pause


def budget_report():

    print_header("BUDGET REPORT")

    expenses = load_expenses()

    if not expenses:

        print("No expenses found.")
        pause()
        return

    budget = float(
        input("Enter Monthly Budget: ₹")
    )

    total_expense = sum(
        float(expense['amount'])
        for expense in expenses
    )

    remaining = budget - total_expense

    usage = int((total_expense / budget) * 100)

    print("\n" + "=" * 50)

    print(f"{'Monthly Budget':<25}: {format_currency(budget)}")
    print(f"{'Total Expenses':<25}: {format_currency(total_expense)}")
    print(f"{'Remaining Balance':<25}: {format_currency(remaining)}")

    print("=" * 50)

    # STATUS

    if total_expense > budget:

        status = "OVER BUDGET"

    elif usage >= 80:

        status = "WARNING"

    else:

        status = "UNDER CONTROL"

    print(f"\nBudget Status : {status}")

    # PROGRESS BAR

    bar =  (usage // 5)

    print(f"\nUsage : [{bar:<20}] {usage}%")

    pause()