# Write a method that check if a string is build out of the same letters as another string
#   same("abc",  "cab"); -> true
#   same("abc",  "abb"); -> false

def same_letters():
    msg = "The words consist of same letters: "
    word_1 = input('Enter the first word: ')
    word_2 = input('Enter the second word: ')

    if len(word_1) != len(word_2):
        return msg, False

    if sorted(word_1) == sorted(word_2):
        return msg, True
    else:
        return msg, False


print(same_letters())