# key value pair
# dictionaries are like lists except that they use keys instead of numbers to look up values
purse = dict()
purse['money'] = 12
purse['tissues'] = 1
print(purse)
print(purse['money'])

counts = dict()
names = ['rick', 'joel', 'maramusa', 'lily']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

counts = dict()
names = ['Rick', 'Joel', 'Emo', 'Emo']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


# get() -> to see if a key is already in a dictionary if the key is in the dictionary the key`s value will return
# if the key is not defined the given value will return

dic = dict()
dic['one'] = 1
dic['two'] = 2
dic['three'] = 3
print(dic.get('four', 0))


# f_handle = open('kek.txt')
# l_word = f_handle.read().split()
# index = 0
# words = dict()
# for word in l_word:
#    if l_word[index] not in words:
#        words[word] = 1
#    else:
#        words[word] = words.get(word, 0) + 1
# print(words)



f_handle = open('kek.txt')
l_word = f_handle.read().split()
words = dict()
for word in l_word:
    words[word] = words.get(word, 0) + 1
print(words)


# count = dict()
# line = input('Enter a line of text: ')
# words = line.split()
# for word in words:
#    count[word] = count.get(word, 0) + 1
# print(count)


# retrieving lists of Keys and Values
jjj = {'Leroy': 1, 'Natasha': 2, 'Ziya': 3}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

for key, value in jjj.items():
    print(key, value)