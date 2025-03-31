def square_each(lst):
    for idx, item in enumerate(lst):
        try:
            lst[idx] = item ** 2
        except TypeError as e:
            raise TypeError(f"Item {item} at index {idx} could not be squared") from e
    return lst

def to_numbers(lst):
    for idx, item in enumerate(lst):
        try:
            lst[idx] = int(item)
        except (ValueError, TypeError) as e:
            raise TypeError(f"Item '{item}' at index {idx} cannot be converted"
                            " to an integer") from e
    return lst

def main():
    user_input = input("Enter a list of numbers to square: ").split()
    print(square_each(to_numbers(user_input)))

main()