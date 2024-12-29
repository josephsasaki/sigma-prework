import datetime
from math import floor


def iso_format(str_date):
    # convert DD-MM-YYYY to YYYY-MM-DD
    numbers = str_date.split("-")
    numbers = numbers[::-1]
    return "-".join(numbers)


def main():
    # Get the date from the user
    str_date = input("date: ")
    # Try convert string date to date object
    try:
        user_date = datetime.date.fromisoformat(iso_format(str_date))
        # Get today's date
        today = datetime.date.today()
        # Find the difference as timedelta object
        difference = today - user_date
        # Print the number of years difference
        print(floor(difference.days / 365))
    except:
        print("Invalid date format provided. Write e.g. 01-01-1990.")


main()
