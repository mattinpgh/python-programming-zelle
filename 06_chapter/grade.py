"""
Calculate a grade based off a quiz score
"""


def main():
    try:
        score = int(input("Enter your quiz score: "))
    except ValueError:
        return "Scores must be integers between 0 and 5"
    if score == 5:
        return "Grade: A"
    elif score == 4:
        return "Grade: B"
    elif score == 3:
        return "Grade: C"
    elif score == 2:
        return "Grade: D"
    elif score == 1:
        return "Grade: F"
    elif score == 0:
        return "Grade: F"
    else:
        return "Invalid score"


if __name__ == "__main__":
    print(main())