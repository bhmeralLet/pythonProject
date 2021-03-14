# Write a  method that can remove the duplicated values from String
# Ex:  removeDup("AAABBBCCC")  ==> ABC

def remove_dep_v1():
    word = input('Enter a word: ')
    duplicated_l = list()
    # finding the number of letters and replacing with empty string
    for i in word:
        count = word.count(i)
        if count > 1:
            word = word.replace(i, '')
            # because the replace method replaces all of the duplicated value adding it to the list
            duplicated_l.append(i)

    # adding the non-duplicated letters to the list
    # the reason for the below codes are to order the words the way they were
    # down below another method without the below codes the input difference is  aBcDeE : DeEaBc
    for i in word:
        duplicated_l.append(i)
    word = ''
    for i in duplicated_l:
        word += i
    print(word)


remove_dep_v1()  # ---> aBcDeE
# aaBBccDeE


# def remove_dep_v2():
#    word = input('Enter a word: ')
#   duplicated_l = list()
    # finding the number of letters and replacing with empty string
#    for i in word:
#        count = word.count(i)
#        if count > 1:
#            word = word.replace(i, '')
#            # because the replace method replaces all of the duplicated value adding it to the list
#            duplicated_l.append(i)
#    for i in duplicated_l:
#        word += i
#    print(word)
# remove_dep_v2()