from storage import load_expenses
from emi_tracker import load_emi
from subscription_manager import load_subs

from utils import print_header, pause, format_currency

def financial_dashboard():

    print_header("FINANCIAL DASHBOARD")

    expenses = load_expenses()

    total_expense = sum(
        float(e["amount"])
        for e in expenses
    )

    try:
        emis = load_emi()

        total_emi = sum(
            e["monthly"]
            for e in emis
        )

    except:
        total_emi = 0

    try:
        subs = load_subs()

        total_sub = sum(
            s["amount"]
            for s in subs
        )

    except:
        total_sub = 0

    income = 50000

    total_spending = (
        total_expense +
        total_emi +
        total_sub
    )

    savings = income - total_spending

    print("=" * 55)

    print(f"{'Monthly Income':<30}: {format_currency(income)}")
    print(f"{'Total Expenses':<30}: {format_currency(total_expense)}")
    print(f"{'Total EMI':<30}: {format_currency(total_emi)}")
    print(f"{'Subscriptions':<30}: {format_currency(total_sub)}")

    print("=" * 55)

    print(f"{'Net Savings':<30}: {format_currency(savings)}")

    print("=" * 55)

    if savings < 0:

        print("\nSTATUS : OVERSPENDING")

    elif savings < 10000:

        print("\nSTATUS : LOW SAVINGS")

    else:

        print("\nSTATUS : HEALTHY BUDGET")

    percent = int((total_spending / income) * 100)

    print(f"\nBudget Usage: {percent}%")