# storage.py

import json


FILE_PATH = "data/expenses.json"


def load_expenses():

    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_expenses(expenses):

    with open(FILE_PATH, "w") as file:
        json.dump(expenses, file, indent=4)