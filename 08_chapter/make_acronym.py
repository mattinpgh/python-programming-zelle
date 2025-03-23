def main():
    word = input("Write the word to acronymize: ")
    lst = word.split()
    acronym = ""
    for element in lst:
        acronym += element[0].upper()

    print(acronym)

main()