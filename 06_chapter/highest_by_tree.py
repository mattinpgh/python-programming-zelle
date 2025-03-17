# Determine the highest of four values using a decision tree


def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    d = int(input("Enter the fourth number: "))

    if a > b:
        if a > c:
            if a > d:
                max_val = a
            else:
                max_val = d
        else:
            if c > d:
                max_val = c
            else:
                max_val = d
    else:
        if b > c:
            if b > d:
                max_val = b
            else:
                max_val = d
        else:
            if c > d:
                max_val = c
            else:
                max_val = d

    print(f"The highest value is {max_val}")


if __name__ == "__main__":
    main()