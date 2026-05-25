import json
import os
from getpass import getpass

USER_FILE = "data/users.json"


# ================= LOAD USERS =================

def load_users():

    try:

        with open(USER_FILE, "r") as file:

            return json.load(file)

    except FileNotFoundError:

        return []


# ================= SAVE USERS =================

def save_users(users):

    os.makedirs("data", exist_ok=True)

    with open(USER_FILE, "w") as file:

        json.dump(users, file, indent=4)


# ================= SIGNUP =================

def signup():

    print("\n========== SIGNUP ==========\n")

    username = input("Enter Username : ").strip()

    password = getpass("Enter Password : ")

    users = load_users()

    # CHECK EXISTING USER

    for user in users:

        if user["username"] == username:

            print("\nUsername already exists!")

            return None

    new_user = {

        "username": username,

        "password": password,

        "role": "user"
    }

    users.append(new_user)

    save_users(users)

    print("\nAccount Created Successfully!")


# ================= LOGIN =================

def login():

    print("\n========== LOGIN ==========\n")

    username = input("Enter Username : ").strip()

    password = getpass("Enter Password : ")

    users = load_users()

    # CHECK USERNAME

    for user in users:

        if user["username"] == username:

            # PASSWORD CHECK

            if user["password"] == password:

                print(f"\nWelcome {username}!")

                return user

            else:

                print("\nIncorrect Password!")

                input("\nPress Enter To Continue...")

                return None

    print("\nUsername Not Found!")

    input("\nPress Enter To Continue...")

    return None
# ================= DEFAULT ADMIN =================

def create_default_admin():

    users = load_users()

    admin_exists = False

    for user in users:

        if user["role"] == "admin":

            admin_exists = True
            break

    if not admin_exists:

        users.append({

            "username": "admin",

            "password": "admin123",

            "role": "admin"
        })

        save_users(users)