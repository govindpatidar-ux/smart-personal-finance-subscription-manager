# utils.py

import os
from datetime import datetime


def clear_screen():

    os.system("clear")


def print_header(title):

    clear_screen()

    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def pause():

    input("\nPress Enter to continue...")


def validate_amount(amount):

    try:
        amount = float(amount)

        return amount > 0

    except ValueError:
        return False


def format_currency(amount):

    return f"₹{float(amount):,.2f}"


def get_current_time():

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")