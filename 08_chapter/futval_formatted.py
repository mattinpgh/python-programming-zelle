def main():
    principal = float(input("Enter the amount of the initial investment: "))
    apr = float(input("Enter the APR as a decimal value (0.05 instead of 5%): "))
    num_years = int(input("Enter the number of years of the investment: "))

    print("Year      Value\n" + "-"*19)
    for year in range(1, num_years + 1):
        principal = principal * ((1 + apr))
        print(f"  {year}      ${principal:0.2f}")

main()