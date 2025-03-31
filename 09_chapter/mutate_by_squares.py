"""
modify a list by squaring each element
"""


def square_each(lst):
    for idx, item in enumerate(lst):
        try:
            lst[idx] = item ** 2
        except TypeError as e:
            raise TypeError(f"Item {item} at index {idx} could not be squared") from e

lrst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_each(lrst)

print(lrst)