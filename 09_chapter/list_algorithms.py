"""
Create algorithms for:
    count
    isin
    index
    reverse
    sort
"""

def matt_count(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def matt_isin(element, lst):
    for item in lst:
        if item == element:
            return True
    return False


def matt_get_index(element, lst):
    for idx, item in enumerate(lst):
        if item == element:
            return idx
    return None


def matt_reverse(lst):
    new_lst = []
    for idx in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[idx])
    return new_lst


