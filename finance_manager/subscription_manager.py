import json
import csv
import os

from datetime import datetime, timedelta

from utils import (
    print_header,
    validate_amount,
    format_currency,
    pause
)

SUB_FILE = "data/subscriptions.json"


# ===================== LOAD =====================

def load_subs():

    try:

        with open(SUB_FILE, "r") as f:

            return json.load(f)

    except:

        return []


# ===================== SAVE =====================

def save_subs(data):

    with open(SUB_FILE, "w") as f:

        json.dump(data, f, indent=4)


# ===================== ADD SUBSCRIPTION =====================

def add_subscription():

    print_header("ADD SUBSCRIPTION")

    name = input("Service Name          : ").strip()

    amount = input("Monthly Cost          : ₹").strip()

    days = input("Renew After (Days)    : ").strip()

    # VALIDATION

    if not validate_amount(amount):

        print("\nInvalid amount.")

        pause()
        return

    try:

        days = int(days)

        if days <= 0:

            print("\nDays must be greater than 0.")

            pause()
            return

    except ValueError:

        print("\nPlease enter valid days.")

        pause()
        return

    renew_date = (

        datetime.now() +

        timedelta(days=days)

    ).strftime("%Y-%m-%d")

    subs = load_subs()

    subs.append({

        "name": name,

        "amount": float(amount),

        "renew_date": renew_date
    })

    save_subs(subs)

    print("\nSubscription Added Successfully!")

    pause()


# ===================== VIEW SUBSCRIPTIONS =====================

def view_subscriptions():

    print_header("ALL SUBSCRIPTIONS")

    subs = load_subs()

    if not subs:

        print("No subscriptions found.")

        pause()
        return

    print("-" * 95)

    print(

        f"{'No':<5}"

        f"{'Service Name':<30}"

        f"{'Monthly Cost':<20}"

        f"{'Renew Date'}"
    )

    print("-" * 95)

    total = 0

    for index, sub in enumerate(subs, start=1):

        total += float(sub["amount"])

        print(

            f"{index:<5}"

            f"{sub['name']:<30}"

            f"{format_currency(sub['amount']):<20}"

            f"{sub['renew_date']}"
        )

    print("-" * 95)

    print(

        f"\n{'Total Monthly Subscription Cost':<35}"

        f": {format_currency(total)}"
    )

    print(

        f"{'Total Active Subscriptions':<35}"

        f": {len(subs)}"
    )

    pause()


# ===================== CHECK REMINDERS =====================

def check_reminders():

    print_header("SUBSCRIPTION REMINDERS")

    subs = load_subs()

    if not subs:

        print("No subscriptions found.")

        pause()
        return

    today = datetime.now().date()

    print("-" * 100)

    print(

        f"{'Service':<30}"

        f"{'Renew Date':<20}"

        f"{'Days Left':<15}"

        f"{'Status'}"
    )

    print("-" * 100)

    found = False

    for sub in subs:

        renew = datetime.strptime(

            sub["renew_date"],

            "%Y-%m-%d"

        ).date()

        days_left = (renew - today).days

        # STATUS

        if days_left < 0:

            status = "EXPIRED"

        elif days_left <= 3:

            status = "RENEW SOON"

        elif days_left <= 7:

            status = "UPCOMING"

        else:

            status = "ACTIVE"

        print(

            f"{sub['name']:<30}"

            f"{sub['renew_date']:<20}"

            f"{days_left:<15}"

            f"{status}"
        )

        found = True

    print("-" * 100)

    if not found:

        print("\nNo reminders found.")

    pause()


# ===================== EXPORT CSV =====================

def export_subscription_csv():

    print_header("EXPORT SUBSCRIPTION CSV")

    subs = load_subs()

    if not subs:

        print("No subscriptions found.")

        pause()
        return

    os.makedirs("data", exist_ok=True)

    with open(

        "data/subscriptions.csv",

        "w",

        newline=""

    ) as f:

        writer = csv.writer(f)

        writer.writerow([

            "Service Name",

            "Monthly Cost",

            "Renew Date"
        ])

        for sub in subs:

            writer.writerow([

                sub["name"],

                sub["amount"],

                sub["renew_date"]
            ])

    print("\nSubscription CSV Exported Successfully!")

    print("\nFile Location : data/subscriptions.csv")

    pause()