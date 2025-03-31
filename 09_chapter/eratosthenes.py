"""
Find all primes up to n using the sieve of eratosthenes
"""


def get_list_of_multiples(lst, x):
    return [y for y in lst if y % x == 0]


def remove_multiples_from_list(mult, original):
    return [num for num in original if num not in mult]


def main():
    n = input("Enter a number: ")
    try:
        n = int(n)
    except (TypeError, ValueError) as e:
        raise TypeError(f"{n} cannot be converted to an integer.") from e

    lst = list(range(2, n))
    prime_lst = []

    while lst:
        prime_lst.append(lst[0])
        lst = [x for x in lst if x % lst[0] != 0]

    print(prime_lst)


if __name__ == "__main__":
    main()
