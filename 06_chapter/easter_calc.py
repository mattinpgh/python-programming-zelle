"""
A script for calculating the date of easter
"""


def get_int_from_user(prompt=""):
    while True:
        try:
            x = int(input(f"{prompt}: "))
            return x
        except ValueError:
            print("Enter a valid integer.")


def calculate_easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = ((19 * a) + 24) % 30
    e = ((2 * b) + (4 * c) + (6 * d) +5) % 7
    date = 22 + d + e

    if year in [1954, 1981, 2049, 2076]:
        date -= 7

    if date > 31:
        month = "April"
        date -= 31
    else:
        month = "March"

    return month, date 


def main():
    year = get_int_from_user("Enter a year between 1900 and 2099")
    month, date  = calculate_easter(year)

    print(f"Easter in {year} is on {month} {date}")


if __name__ == "__main__":
    main()