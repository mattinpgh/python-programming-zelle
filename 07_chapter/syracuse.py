"""
An implementation of the Syracuse Sequence
"""


def if_odd(x):
    return 3 * x + 1


def if_even(x):
    return x // 2


def even_or_odd(x):
    return if_even(x) if x % 2 == 0 else if_odd(x)


def main():
    while True:
        try:
            user_input = int(input("Enter a positive integer. To quit, enter 0: "))
            if user_input == 0:
                print("Exiting the program.")
                return
            elif user_input < 0:
                print("Please enter a positive integer.")
                continue
            else:
                break 
        except ValueError:
            print("Enter a valid integer.")

    sequence = []
    current = user_input
    
    while current >= 1:
        sequence.append(current)
        current = even_or_odd(current)

    print(f"The Syracuse Sequence for {user_input} is {sequence}.")

if __name__ == "__main__":
    main()
