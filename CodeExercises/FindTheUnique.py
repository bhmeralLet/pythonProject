# Write a  method that can find the unique characters from the String
#  unique("AAABBBCCCDEF")  ==>  "DEF"



def find_the_unique():
    w_dict = dict()
    word = input("Enter the word: ")
    unique_l = list()
    non_unique_l = list()
    for i in word:
        w_dict[i] = word.count(i)
    for k, v in w_dict.items():
        if v == 1:
            unique_l.append(k)
        else:
            non_unique_l.append(k)
    print('Unique Characters: ', unique_l)
    print('Non-unique Characters: ', non_unique_l)



find_the_unique()