import logging
import csv
import os

os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_info(message):

    logging.info(message)


def view_logs():

    print("\n==== APPLICATION LOGS ====\n")

    try:

        with open("logs/app.log", "r") as file:

            logs = file.readlines()

            if not logs:

                print("No logs found.")
                return

            for log in logs:

                print(log.strip())

    except FileNotFoundError:

        print("Log file not found.")


def export_logs_csv():

    print("\n==== EXPORT LOGS CSV ====\n")

    try:

        with open("logs/app.log", "r") as f:

            lines = f.readlines()

        if not lines:

            print("No logs to export.")
            return

        with open("data/logs.csv", "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(["Log Entry"])

            for line in lines:

                writer.writerow([line.strip()])

        print("Logs exported successfully!")

    except FileNotFoundError:

        print("Log file not found.")