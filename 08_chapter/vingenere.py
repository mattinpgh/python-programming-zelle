ALPHABET = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ .,?!"

def get_index(character):
    return ALPHABET.index(character)


def get_string(character_int):
    return ALPHABET[character_int]


def encode(phrase, text):
    encoded_message = ""
    enc_phrase = [get_index(char) for char in phrase]
    enc_phrase = [enc_phrase[i % len(phrase)] for i in range(len(text))]

    for idx, character in enumerate(text):
        shifted_character = (get_index(character) + enc_phrase[idx]) % len(ALPHABET)
        encoded_message += get_string(shifted_character)

    return encoded_message


def decode(phrase, text):
    decoded_message = ""
    enc_phrase = [get_index(char) for char in phrase]
    enc_phrase = [enc_phrase[i % len(phrase)] for i in range(len(text))]

    for idx, character in enumerate(text):
        shifted_character = (get_index(character) - enc_phrase[idx]) % len(ALPHABET)
        decoded_message += get_string(shifted_character)

    return decoded_message


def is_valid_input(text, allowed):
    for character in text:
        if character not in allowed:
            return False
    return True


def get_input():
    while True:
        passphrase = input("Enter a passphrase. Letters, spaces, and [.,?!] only: ")
        if not is_valid_input(passphrase, ALPHABET):
            print(f"You may only use the following: \n{ALPHABET}")
            continue

        message = input("Enter a message. Letters, spaces, and [.,!?] only: ")
        if not is_valid_input(message, ALPHABET):
            print(f"You may only use the following: \n{ALPHABET}")
            continue

        while True:
            action = input("Enter '1' to encode a message, '2' to decode: ")
            if action in ["1", "2"]:
                return action, passphrase, message
            print("Please enter either '1' or '2'.")


def main():
    action, passphrase, message = get_input()

    if action == "1":
        modified_message = encode(passphrase, message)
    else:
        modified_message = decode(passphrase, message)
        print(f"Your passphrase is {passphrase}")

    print(f"Your message is: {modified_message}")


if __name__ == "__main__":
    main()
