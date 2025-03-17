# A program to select the largest of three numbers


def main():
    value_a = float(input("Enter the first number: "))
    value_b = float(input("Enter the second number: "))
    value_c = float(input("Enter the third number: "))
    highest = float("-inf")

    for value in [value_a, value_b, value_c]:
        if value > highest:
            highest = value

    return highest

if __name__ == "__main__":
    print(main())