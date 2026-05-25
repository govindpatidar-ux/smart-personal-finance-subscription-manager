# ===================== EMI TRACKER =====================

import json
import csv
import os

from utils import (
    print_header,
    validate_amount,
    format_currency,
    pause
)

EMI_FILE = "data/emi.json"


# ===================== LOAD EMI =====================

def load_emi():

    try:

        with open(EMI_FILE, "r") as f:

            return json.load(f)

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        return []


# ===================== SAVE EMI =====================

def save_emi(data):

    os.makedirs("data", exist_ok=True)

    with open(EMI_FILE, "w") as f:

        json.dump(data, f, indent=4)


# ===================== ADD EMI =====================

def add_emi():

    print_header("ADD EMI")

    name = input("Loan Name            : ").strip()

    total = input("Total Loan Amount    : ₹").strip()

    monthly = input("Monthly EMI Amount   : ₹").strip()

    months = input("Total Months         : ").strip()

    # VALIDATION

    if not name:

        print("\nLoan name cannot be empty.")

        pause()
        return

    if not validate_amount(total):

        print("\nInvalid Loan Amount.")

        pause()
        return

    if not validate_amount(monthly):

        print("\nInvalid EMI Amount.")

        pause()
        return

    try:

        months = int(months)

        if months <= 0:

            print("\nMonths must be greater than 0.")

            pause()
            return

    except ValueError:

        print("\nPlease enter valid months.")

        pause()
        return

    # EMI OBJECT

    emi = {

        "name": name,

        "total": float(total),

        "monthly": float(monthly),

        "months": months,

        "paid_months": 0
    }

    data = load_emi()

    data.append(emi)

    save_emi(data)

    print("\nEMI Added Successfully!")

    pause()


# ===================== VIEW EMI =====================

def view_emi():

    print_header("EMI MANAGEMENT STATUS")

    data = load_emi()

    if not data:

        print("No EMI records found.")

        pause()
        return

    print("-" * 120)

    print(

        f"{'No':<5}"

        f"{'Loan Name':<25}"

        f"{'Monthly EMI':<18}"

        f"{'Remaining Amount':<22}"

        f"{'Months Left':<15}"

        f"{'Status'}"
    )

    print("-" * 120)

    total_monthly = 0
    total_remaining = 0

    for index, emi in enumerate(data, start=1):

        remaining = (

            emi["total"] -

            (emi["monthly"] * emi["paid_months"])
        )

        months_left = (

            emi["months"] -

            emi["paid_months"]
        )

        total_monthly += emi["monthly"]

        total_remaining += remaining

        # STATUS

        if months_left == 0:

            status = "COMPLETED"

        elif months_left <= 3:

            status = "ENDING SOON"

        else:

            status = "ACTIVE"

        print(

            f"{index:<5}"

            f"{emi['name']:<25}"

            f"{format_currency(emi['monthly']):<18}"

            f"{format_currency(remaining):<22}"

            f"{months_left:<15}"

            f"{status}"
        )

    print("-" * 120)

    # ===================== SUMMARY =====================

    print("\nEMI SUMMARY\n")

    print(

        f"{'Total Monthly EMI':<30}"

        f": {format_currency(total_monthly)}"
    )

    print(

        f"{'Total Remaining Amount':<30}"

        f": {format_currency(total_remaining)}"
    )

    print(

        f"{'Total Loans':<30}"

        f": {len(data)}"
    )

    pause()


# ===================== PAY EMI =====================

def pay_emi():

    print_header("PAY EMI")

    data = load_emi()

    if not data:

        print("No EMI records found.")

        pause()
        return

    print("-" * 75)

    print(

        f"{'No':<5}"

        f"{'Loan Name':<30}"

        f"{'Paid Months'}"
    )

    print("-" * 75)

    for index, emi in enumerate(data, start=1):

        print(

            f"{index:<5}"

            f"{emi['name']:<30}"

            f"{emi['paid_months']}/{emi['months']}"
        )

    print("-" * 75)

    try:

        choice = int(

            input("\nSelect EMI Number: ")
        )

        if choice < 1 or choice > len(data):

            print("\nInvalid EMI selection.")

            pause()
            return

        emi = data[choice - 1]

        # CHECK COMPLETED

        if emi["paid_months"] >= emi["months"]:

            print("\nThis EMI is already completed.")

            pause()
            return

        # UPDATE PAYMENT

        emi["paid_months"] += 1

        save_emi(data)

        remaining_months = (

            emi["months"] -

            emi["paid_months"]
        )

        print("\nEMI Paid Successfully!")

        print(

            f"\nRemaining Months : "
            f"{remaining_months}"
        )

    except ValueError:

        print("\nPlease enter valid number.")

    pause()


# ===================== EXPORT EMI CSV =====================

def export_emi_csv():

    print_header("EXPORT EMI CSV")

    data = load_emi()

    if not data:

        print("No EMI records found.")

        pause()
        return

    os.makedirs("data", exist_ok=True)

    with open(

        "data/emi.csv",

        "w",

        newline=""

    ) as f:

        writer = csv.writer(f)

        writer.writerow([

            "Loan Name",

            "Total Amount",

            "Monthly EMI",

            "Total Months",

            "Paid Months"
        ])

        for emi in data:

            writer.writerow([

                emi["name"],

                emi["total"],

                emi["monthly"],

                emi["months"],

                emi["paid_months"]
            ])

    print("\nEMI CSV Exported Successfully!")

    print("\nFile Location : data/emi.csv")

    pause()