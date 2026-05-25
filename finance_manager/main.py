# ===================== MAIN APPLICATION =====================
from expense_manager import *
from analytics import monthly_analytics
from reports import (
    budget_report,
)
from logger import *
from alerts import *
from emi_tracker import *
from subscription_manager import *
from dashboard import financial_dashboard
from auth import (
    signup,
    login,
    create_default_admin
)
from utils import (
    print_header,
    pause
)


# ===================== AUTH MENU =====================
def auth_menu():
    while True:
        print_header("SMART PERSONAL FINANCE MANAGER")
        print("1. Admin Login")
        print("2. User Login")
        print("3. User Signup")
        print("0. Exit")

        choice = input("\nEnter Choice: ")

        # ================= ADMIN LOGIN =================
        if choice == "1":
            user = login()
            if user:
                if user["role"] == "admin":
                    admin_menu()
                else:
                    print("\nAccess Denied!")
                    print("This is not an admin account.")
                    pause()

        # ================= USER LOGIN =================
        elif choice == "2":
            user = login()
            if user:
                if user["role"] == "user":
                    user_menu()
                else:
                    print("\nPlease use Admin Login.")
                    pause()

        # ================= USER SIGNUP =================
        elif choice == "3":
            signup()

        # ================= EXIT =================
        elif choice == "0":
            print("\nThank You For Using Smart Finance Manager")
            break
        else:
            print("\nInvalid choice.")
            pause()


# ===================== USER DASHBOARD =====================
def user_menu():
    while True:
        print_header("USER DASHBOARD")
        print("1. Expense Management")
        print("2. Analytics & Reports")
        print("3. Alerts")
        print("4. Subscription Management")
        print("5. EMI Management")
        print("6. Financial Dashboard")
        print("0. Logout")

        choice = input("\nEnter Choice: ")

        # ================= EXPENSE =================
        if choice == "1":
            expense_menu()

        # ================= REPORTS =================
        elif choice == "2":
            reports_menu()

        # ================= ALERTS =================
        elif choice == "3":
            alerts_menu()

        # ================= SUBSCRIPTIONS =================
        elif choice == "4":
            subscription_menu()

        # ================= EMI =================
        elif choice == "5":
            emi_menu()

        # ================= DASHBOARD =================
        elif choice == "6":
            financial_dashboard()
            pause()  # DASHBOARD KE BAAD BHI PAUSE ZAROORI HAI

        # ================= LOGOUT =================
        elif choice == "0":
            print("\nLogged Out Successfully!")
            break
        else:
            print("\nInvalid choice.")
            pause()


# ===================== ADMIN MENU =====================
def admin_menu():
    while True:
        print_header("ADMIN PANEL")
        print("1. View Expenses")
        print("2. View Logs")
        print("3. Export Logs CSV")
        print("4. Financial Dashboard")
        print("0. Logout")

        choice = input("\nEnter Choice: ")

        # ================= VIEW EXPENSES =================
        if choice == "1":
            view_expenses()
            pause()  # <--- PAUSE ADDED

        # ================= VIEW LOGS =================
        elif choice == "2":
            view_logs()
            pause()  # <--- PAUSE ADDED

        # ================= EXPORT LOGS =================
        elif choice == "3":
            export_logs_csv()
            pause()  # <--- PAUSE ADDED

        # ================= DASHBOARD =================
        elif choice == "4":
            financial_dashboard()
            pause()  # <--- PAUSE ADDED

        # ================= LOGOUT =================
        elif choice == "0":
            print("\nAdmin Logged Out Successfully!")
            break
        else:
            print("\nInvalid choice.")
            pause()


# ===================== EXPENSE MENU =====================
def expense_menu():
    while True:
        print_header("EXPENSE MANAGEMENT")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("0. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
            pause()  # <--- PAUSE ADDED (agar view karne ke baad gayab ho raha ho)
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            search_expense()
            pause()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")
            pause()


# ===================== REPORT MENU =====================
def reports_menu():
    while True:
        print_header("ANALYTICS & REPORTS")
        print("1. Monthly Analytics")
        print("2. Budget Report")
        print("3. Export Expense CSV")
        print("4. View Logs")
        print("5. Export Logs CSV")
        print("0. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            monthly_analytics()
            pause()  # <--- PAUSE ADDED

        elif choice == "2":
            budget_report()
            pause()  # <--- PAUSE ADDED

        elif choice == "3":
            export_emi_csv()  # <--- CORRECTED: Pehle yahan export_emi_csv() tha
            pause()  # <--- PAUSE ADDED

        elif choice == "4":
            view_logs()
            pause()  # <--- PAUSE ADDED

        elif choice == "5":
            export_logs_csv()
            pause()  # <--- PAUSE ADDED

        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")
            pause()


# ===================== ALERT MENU =====================
def alerts_menu():
    while True:
        print_header("ALERT SYSTEM")
        print("1. Due Date Alerts")
        print("2. Budget Limit Check")
        print("0. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            check_due_alerts()
            pause()
        elif choice == "2":
            check_budget_limits()
            pause()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")
            pause()


# ===================== SUBSCRIPTION MENU =====================
def subscription_menu():
    while True:
        print_header("SUBSCRIPTION MANAGEMENT")
        print("1. Add Subscription")
        print("2. View Subscriptions")
        print("3. Check Reminders")
        print("4. Export Subscription CSV")
        print("0. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            add_subscription()
        elif choice == "2":
            view_subscriptions()
            pause()
        elif choice == "3":
            check_reminders()
            pause()
        elif choice == "4":
            export_subscription_csv()
            pause()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")
            pause()


# ===================== EMI MENU =====================
def emi_menu():
    while True:
        print_header("EMI MANAGEMENT")
        print("1. Add EMI")
        print("2. View EMI")
        print("3. Pay EMI")
        print("4. Export EMI CSV")
        print("0. Back")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            add_emi()
        elif choice == "2":
            view_emi()
            pause()
        elif choice == "3":
            pay_emi()
        elif choice == "4":
            export_emi_csv()
            pause()
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.")
            pause()


# ===================== ENTRY POINT =====================
if __name__ == "__main__":
    try:
        # CREATE DEFAULT ADMIN
        create_default_admin()

        # START APPLICATION
        auth_menu()

    except KeyboardInterrupt:
        print("\n\nApplication Closed Safely.")