"""
Calculate BMI and determine whether a person is in healthy range
"""


def get_int_from_user(prompt=""):
    while True:
        try:
            x = int(input(f"{prompt}: "))
            return x
        except ValueError:
            print("Enter a valid integer.")


def main():
    weight = get_int_from_user("Enter your weight in pounds")
    height = get_int_from_user("Enter your height in inches")
    bmi = (weight * 703) / (height ** 2)

    if bmi < 19:
        print(f"With a BMI of {bmi}, you are below the healthy range.")
    elif bmi < 26:
        print(f"With a BMI of {bmi}, you are within the healthy range.")
    else:
        print(f"With a BMI of {bmi}, you are above the healthy range.")


if __name__ == "__main__":
    main()
    