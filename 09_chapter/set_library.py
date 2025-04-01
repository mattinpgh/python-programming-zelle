"""
Create the following set functions from scratch. Do not use actual sets, but
make lists behave as if they were sets:

make_set(elements)
add_element(set, element)
delete_element(set, element)
member(set, element) (True is element in set)
intersection(set1, set2)
union(set1, set2)
subtract(set1, set2)
"""

def make_set(elements):
    new_set = []
    for item in elements:
        if item not in new_set:
            new_set.append(item)
    return new_set


def add_element(set, element):
    if element not in set:
        set.append(element)
    return set


def delete_element(set, element):
    if element in set:
        set.remove(element)
    return set


def member(set, element):
    return element in set


def intersection(set1, set2):
    return [item for item in set1 if item in set2]


def union(set1, set2):
    union_builder = set1.copy()
    for item in set2:
        if item not in set1:
            union_builder.append(item)
    return union_builder


def subtract(set1, set2):
    return [item for item in set1 if item not in set2]