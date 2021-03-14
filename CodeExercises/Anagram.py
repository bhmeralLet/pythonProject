# started working on before knowing that sorted can be used on strings (kekw)

from collections import Counter

def anagram_v1():
    str_1 = input("Enter the first word: ").lower()
    str_2 = input("Enter the second word: ").lower()
    index = 0
    d_str_1 = dict()
    d_str_2 = dict()

    if len(str_1) != len(str_2):
        print("Not anagram")
        exit(0)

    while True:
        count_1 = str_1.count(str_1[index])
        count_2 = str_2.count(str_2[index])
        d_str_1[str_1[index]] = count_1
        d_str_2[str_2[index]] = count_2
        index += 1
        if index == len(str_1) - 1:
            break


    if d_str_1 == d_str_2:
        print('anagram')
    else:
        print('not anagram')

anagram_v1()


# improved version lowering unnecessary code
def anagram_v2():
    str_1 = input("Enter the first word").lower()
    str_2 = input("Enter the second word").lower()
    index = 0
    l_str_1 = list()
    l_str_2 = list()

    if len(str_1) != len(str_2):
        print("Not anagram")
        exit(0)

    while True:
        l_str_1.append(str_1[index: index + 1])
        l_str_2.append(str_2[index: index + 1])
        index += 1
        if index == len(str_1) - 1:
            break

    print(l_str_1)
    print(l_str_2)
    if l_str_1.sort() == l_str_2.sort():
        print('Anagram')
    else:
        print('not anagram')

# anagram_v2()

# from internet
# function to check if two strings are
# anagram or not
def check(s1, s2):
    # implementing counter function
    if (Counter(s1) == Counter(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


# driver code
s1 = "listen"
s2 = "silent"
# check(s1, s2)

# from internet
def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

    # driver code


s1 = "listen"
s2 = "silent"
# check(s1, s2)