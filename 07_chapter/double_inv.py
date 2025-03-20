"""
Use a while loop to determine how long it takes for 
an investment to double at a given interest rate.

input: annualized interest rate
output: number of years

formula: interest = principal * rate * time

"""


def main():
    while True:
        try:
            interest_rate = float(input("Please enter an interest rate as a decimal value: "))
            break
        except ValueError:
            print("Enter a valid decimal value, for example 0.01 for 1%")

    investment = 1000
    target_value = investment * 2
    years = 0

    while investment <= target_value:
        investment += (investment * interest_rate)
        years += 1

    print(f"An investment at {interest_rate} doubles at {years} years.")


if __name__ == "__main__":
    main()
