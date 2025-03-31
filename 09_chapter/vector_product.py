"""
Write a function to compute the inner product of two seme length lists. 

n - 1
SUM x1y1
i=0
"""


def inner_product(x, y):
    if len(x) != len(y):
        raise ValueError("Lists must be the same length")
    return sum(a * b for a, b in zip(x, y))
    """accumulator = 0
    for i in range(len(x)):
        accumulator += x[i] * y[i]
    return accumulator"""

print(inner_product([1, 2, 3], [4, 5, 6]))