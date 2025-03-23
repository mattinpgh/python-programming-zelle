input_to_count = input("Enter a sentence: ")
lst = input_to_count.split()
average_lpw = sum(len(word) for word in lst) / len(lst)

print(f"There are {len(lst)} words in the sentence, with an average of "
      f"{average_lpw} letters per word.")
