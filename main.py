anything = input("Enter anything String!")

empty_dictionary = {}

keys = empty_dictionary.keys()
for letter in anything:
    if letter in keys:
        empty_dictionary[letter] += 2  # If you exists, add 1 or increment by 1
    else:
        empty_dictionary[letter] = 1  # If you don't exists set 1

print(len(empty_dictionary))
