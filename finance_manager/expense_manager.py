from storage import load_expenses, save_expenses
from utils import print_header, validate_amount
from logger import log_info
from utils import print_header, pause


def add_expense():

    print_header("ADD EXPENSE")

    title = input("Enter Expense Title: ")

    amount = input("Enter Amount: ")

    if not validate_amount(amount):

        print("Invalid Amount.")
        return

    category = input("Enter Category: ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category
    }

    expenses = load_expenses()

    expenses.append(expense)

    save_expenses(expenses)

    print("\nExpense Added Successfully!")

    log_info(f"Expense Added: {title} | ₹{amount} | {category}")


def view_expenses():

    print_header("ALL EXPENSES")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        pause()
        return

    print("-" * 65)
    print(f"{'No':<5}{'Title':<20}{'Amount':<15}{'Category'}")
    print("-" * 65)

    for index, expense in enumerate(expenses, start=1):

        print(
            f"{index:<5}"
            f"{expense['title']:<20}"
            f"₹{expense['amount']:<14}"
            f"{expense['category']}"
        )
    print("-" * 65)
    pause()


def delete_expense():

    print_header("DELETE EXPENSE")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):

        print(
            f"{index}. "
            f"{expense['title']} | "
            f"₹{expense['amount']} | "
            f"{expense['category']}"
        )

    try:

        choice = int(input("\nEnter expense number to delete: "))

        if 1 <= choice <= len(expenses):

            deleted_expense = expenses.pop(choice - 1)

            save_expenses(expenses)

            print(
                f"\nExpense "
                f"'{deleted_expense['title']}' "
                f"deleted successfully!"
            )

            log_info(
                f"Expense Deleted: "
                f"{deleted_expense['title']}"
            )

        else:
            print("\nInvalid expense number.")

    except ValueError:

        print("\nPlease enter a valid number.")


def update_expense():

    print_header("UPDATE EXPENSE")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):

        print(
            f"{index}. "
            f"{expense['title']} | "
            f"₹{expense['amount']} | "
            f"{expense['category']}"
        )

    try:

        choice = int(input("\nEnter expense number to update: "))

        if 1 <= choice <= len(expenses):

            expense = expenses[choice - 1]

            print("\nLeave blank to keep old value.\n")

            new_title = input(
                f"Enter New Title ({expense['title']}): "
            )

            new_amount = input(
                f"Enter New Amount ({expense['amount']}): "
            )

            if new_amount and not validate_amount(new_amount):

                print("Invalid Amount.")
                return

            new_category = input(
                f"Enter New Category ({expense['category']}): "
            )

            if new_title:
                expense['title'] = new_title

            if new_amount:
                expense['amount'] = new_amount

            if new_category:
                expense['category'] = new_category

            save_expenses(expenses)

            print("\nExpense Updated Successfully!")

            log_info(
                f"Expense Updated: "
                f"{expense['title']}"
            )

        else:
            print("\nInvalid expense number.")

    except ValueError:

        print("\nPlease enter a valid number.")


def search_expense():

    print_header("SEARCH EXPENSE")

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    keyword = input(
        "Enter title or category to search: "
    ).lower()

    found = False

    for index, expense in enumerate(expenses, start=1):

        title = expense['title'].lower()

        category = expense['category'].lower()

        if keyword in title or keyword in category:

            print(
                f"{index}. "
                f"{expense['title']} | "
                f"₹{expense['amount']} | "
                f"{expense['category']}"
            )

            found = True

    if not found:

        print("\nNo matching expenses found.")
