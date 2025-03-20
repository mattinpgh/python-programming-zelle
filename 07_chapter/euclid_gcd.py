"""
Determine the greatest common divisor using Euclid's algorithm
"""

def apply_euclid(m, n):
    new_m = n % m
    new_n = m
    return new_m, new_n


def main():
    the_first = int(input("Input the first integer: "))
    the_second = int(input("Input the secondf integer: "))
    m = the_first
    n = the_second

    while m != 0:
        m, n = apply_euclid(m, n)

    print(f"The greatest common divisor of {the_first} and {the_second} is {n}.")

if __name__ == "__main__":
    main()
