def get_input():
    while True:
        valid = True
        name = input("Enter a name to calculate its value (letters/spaces only): ")
        name_lst = name.strip().split()
        for item in name_lst:
            if not item.isalpha():
                valid = False
                print("Letters only: no digits, or special characters.")
                break
        if valid:
            return name, name_lst

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    name, name_lst = get_input()
    name_value = 0

    for word in name_lst:
        for char in word:
            name_value += alphabet.index(char.lower()) + 1

    print(f"The value of {name} is {name_value}.")

main()