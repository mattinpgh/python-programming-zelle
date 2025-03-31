"""
Write a function that removes duplicate values from a list
"""

def remove_duplicates(lst):
    deduped = set(lst)
    return list(deduped)

print(remove_duplicates([1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 8, 9]))