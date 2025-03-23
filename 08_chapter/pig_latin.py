def get_word_place(phrase, word):
    phrase = phrase.split()
    for element in phrase:
        if element == word:
            return phrase.index(element)


def is_vowel(char, first_place=False):
    if first_place:
        vowels = ['a', 'e', 'i', 'o', 'u']
    else:
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if char.lower() in vowels:
        return True
    return False


def first_vowel(word):
    for idx, character in enumerate(word):
        if idx == 0:
            if is_vowel(character, True):
                return idx, character
        else:
            if is_vowel(character):
                return idx, character
    return None, None


def translate_word_to_pl(word):
    idx, char = first_vowel(word)
    if idx is None:
        return word
    
    new_word = ""
    punc = ""
    for char in word:
        if not char.isalpha() and char == word[-1]:
            punc = char
            continue
        new_word += char

    if idx == 0:
        return f"{new_word}way{punc}"
    
    consonant_cluster = new_word[:idx]
    new_base = new_word[idx:]
    return f"{new_base}{consonant_cluster}ay{punc}"


def translate_phrase_to_pl(phrase):
    translated_list = [translate_word_to_pl(word) for word in phrase.split()]
    translated_list[0] = translated_list[0].title()
    return translated_list


def main():
    phrase_to_translate = input("Enter a phrase to translate to pig latin. ")
    # phrase_to_translate = "Translate this here phrase, if you don't mind."
    translated_phrase = translate_phrase_to_pl(phrase_to_translate)
    translated_phrase = " ".join(translated_phrase)
    print(translated_phrase)


main()