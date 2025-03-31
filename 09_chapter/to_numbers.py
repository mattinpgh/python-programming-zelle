"""
Convert each element in a list of strings to numbers
"""

def to_numbers(lst):
    for idx, item in enumerate(lst):
        try:
            lst[idx] = int(item)
        except (ValueError, TypeError) as e:
            raise TypeError(f"Item '{item}' at index {idx} cannot be converted"
                            " to an integer") from e

lrst = ["1", "2", "3", "4"]
for item in lrst:
    print(type(item))

to_numbers(lrst)

for item in lrst:
    print(type(item))