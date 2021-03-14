#
# @param count
# enter how many common word you wanna see
def common_words_infile(count):
    f_handle = open('word.txt')
    words = f_handle.read().split(' ')

    if count > len(words):
        print('There isn`t that many words in the file')
        print('Please enter a number lower than this ->', len(words))
        exit(0)
    common_list = list()
    w_dict = dict()
    for i in words:
        w_dict[i] = words.count(i)
    for k, v in w_dict.items():
        common_list.append((v, k))
    common_list = sorted(common_list, reverse=True)
    for i in range(count):
        print(common_list[i:i + 1])

common_words_infile(57)