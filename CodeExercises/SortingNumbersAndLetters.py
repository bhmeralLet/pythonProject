# Given alphanumeric String, we need to split the string into substrings of
# consecutive letters or numbers, sort the individual string and append them back together
# Ex:
# Input:  "DC501GCCCA098911"
# OutPut: "CD015ACCCG011899"


def sort():
    word = 'DC501GCCCA098911'
    w_list = list()
    sorted_list = list()
    sorted_word = ''
    index = 0
    for i in word:
        sorted_word += i
        if i.isalpha() and index < len(word) - 1:
            if word[index + 1].isnumeric():
                sorted_word += ','
        if i.isdigit() and index < len(word) - 1:
            if word[index + 1].isalpha():
                sorted_word += ','
        index += 1

    w_list = sorted_word.split(',')
    sorted_word = ''
    print(w_list)

    for i in w_list:
        sorted_list += sorted(i)

    for i in sorted_list:
        sorted_word += i

    print(sorted_list)
    print(sorted_word)

sort()