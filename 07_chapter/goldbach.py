"""
Check an even number to see if it is the sum of two prime numbers
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


def get_prime_list(user_input):
    prime_list = []
    n = user_input
    while n >= 2:
        if check_prime(n):
            prime_list.append(n)
        n -= 1

    return prime_list    


def get_addends(user_input, prime_list):
    list_of_addends = []

    # for x in prime_list[:(len(prime_list)//2)]:
    for x in prime_list:
        for y in prime_list:
            if x + y == user_input:
                highest = max(x, y)
                lowest = min(x, y)
                list_of_addends.append((highest,lowest))

    return list_of_addends


def dedup_addends(lst):
    deduped = set(lst)

    return list(deduped)

def main():
    while True:
        try:
            user_input = int(input("Enter a positive even integer: "))
        except ValueError:
            print("Your entry must be a positive, even integer.")
            continue
        if user_input > 1 and user_input % 2 == 0:
            break
        else:
            print("Your entry must be a positive, even integer.")


    prime_list = get_prime_list(user_input)
    addends = get_addends(user_input, prime_list)
    unique_addend_pairs = dedup_addends(addends)

    if addends:
        print(f"{user_input} is the sum of the following primes: {unique_addend_pairs}")
    else:
        print(f"There are not two primes which add up to {user_input}.")

if __name__ == "__main__":
    main()