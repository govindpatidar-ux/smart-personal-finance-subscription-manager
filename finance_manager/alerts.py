from datetime import datetime
from storage import load_expenses
from utils import (
    print_header,
    format_currency,
    pause
)

# ================= CATEGORY LIMITS =================

category_budget = {
    "Food": 5000,
    "Travel": 3000,
    "Shopping": 4000,
    "Bills": 6000
}


# ================= DUE DATE ALERTS =================

def check_due_alerts():

    print_header("DUE DATE ALERTS")

    expenses = load_expenses()

    today = datetime.now().date()

    found = False

    print("-" * 70)

    print(
        f"{'Title':<25}"
        f"{'Due Date':<20}"
        f"{'Status'}"
    )

    print("-" * 70)

    for exp in expenses:

        if "due_date" in exp and exp["due_date"]:

            due = datetime.strptime(
                exp["due_date"],
                "%Y-%m-%d"
            ).date()

            days_left = (due - today).days

            # OVERDUE

            if days_left < 0:

                status = "OVERDUE"

            # DUE SOON

            elif days_left <= 3:

                status = f"DUE IN {days_left} DAYS"

            else:
                continue

            print(
                f"{exp['title']:<25}"
                f"{exp['due_date']:<20}"
                f"{status}"
            )

            found = True

    print("-" * 70)

    if not found:

        print("\nNo due alerts found.")

    pause()


# ================= BUDGET STATUS =================

def check_budget_limits():

    print_header("CATEGORY BUDGET STATUS")

    expenses = load_expenses()

    spent = {}

    # ================= CALCULATE =================

    for expense in expenses:

        category = expense["category"]

        amount = float(expense["amount"])

        spent[category] = (
            spent.get(category, 0) + amount
        )

    # ================= TABLE =================

    print("-" * 75)

    print(
        f"{'Category':<20}"
        f"{'Used':<15}"
        f"{'Limit':<15}"
        f"{'Usage'}"
    )

    print("-" * 75)

    total_used = 0
    total_limit = 0

    for category, limit in category_budget.items():

        used = spent.get(category, 0)

        total_used += used
        total_limit += limit

        # Percentage

        percent = int((used / limit) * 100)

        # Progress Bar

        bar = (percent // 10)

        # Status

        if percent > 100:

            status = "OVER LIMIT"

        elif percent >= 80:

            status = "WARNING"

        else:

            status = "SAFE"

        print(
            f"{category:<20}"
            f"{format_currency(used):<15}"
            f"{format_currency(limit):<15}"
            f"{bar} {percent}% ({status})"
        )

    print("-" * 75)

    # ================= SUMMARY =================

    remaining = total_limit - total_used

    print("\nOVERALL SUMMARY\n")

    print(
        f"{'Total Budget':<25}"
        f": {format_currency(total_limit)}"
    )

    print(
        f"{'Total Spending':<25}"
        f": {format_currency(total_used)}"
    )

    print(
        f"{'Remaining Budget':<25}"
        f": {format_currency(remaining)}"
    )

    # ================= FINAL STATUS =================

    if total_used > total_limit:

        print("\nFINAL STATUS : OVERALL BUDGET EXCEEDED")

    elif total_used >= total_limit * 0.8:

        print("\nFINAL STATUS : BUDGET WARNING")

    else:

        print("\nFINAL STATUS : BUDGET HEALTHY")

    pause()