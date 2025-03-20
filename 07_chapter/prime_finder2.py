"""
Find out if a number is prime by checking for divisors between 2 and sqrt(n)
"""

from math import sqrt

def check_prime(x):
    if x in [2, 3]:
        return True

    if x % 2 == 0 or x % 3 == 0:
        return False

    i = 3
    while i <= sqrt(x):
        if x % i == 0:
            return False
        i += 2

    return True


def main():
    while True:
        try:
            n = int(input("Enter a positive integer higher than 1: "))
        except ValueError:
            print("The number must be an integer.")
            continue
        if n > 1:
            break

    prime_list = []
    while n >= 2:
        if check_prime(n):
            prime_list.append(n)
        n -= 1
    
    print(prime_list)

if __name__ == "__main__":
    main()
