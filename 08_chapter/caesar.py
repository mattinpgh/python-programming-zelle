def encode(string, key):
    key = key % 26
    encoded_string = ""
    for char in string:
        if char == " ":
            encoded_string += " "
            continue

        if char.isupper():
            char = int(ord(char)) + key
            if char > 90:
                char -= 26
        elif char.islower():
            char = int(ord(char)) + key
            if char > 122:
                char -= 26
        else:
            char = int(ord(char))

        encoded_string += chr(char)

    return encoded_string

def decode(encoded_string, key):
    key = key % 26
    decoded_string = ""
    for char in encoded_string:
        if char == " ":
            decoded_string += " "
            continue

        char = int(ord(char))
        if chr(char).isupper():
            char -= key
            if char < 65:
                char += 26
        elif chr(char).islower():
            char -= key
            if char < 97:
                char += 26
            
        decoded_string += chr(char)
    return decoded_string


def main():
    while True:
        action = input("Enter 1 to encode a message, 2 to decode: ")
        if action in ["1", "2"]: break

    while True:
        valid = True
        phrase = input("Enter a message to encode or decode (letters and spaces only): ")
        print(phrase)

        for character in phrase:
            if not character.isalpha() and not character == " ":
                print("Characters and spaces only")
                valid = False
        if valid:
            break

    while True:
        try:
            key = int(input("Enter the integer key to encode or decode the message: "))
            break
        except ValueError:
            print("The key must be an integer.")

    if action == "1":
        new_phrase = encode(phrase, key)
    else:
        new_phrase = decode(phrase, key)

    print(f"Complete: {phrase} is now {new_phrase}. Retain the key: {key}")

main()
