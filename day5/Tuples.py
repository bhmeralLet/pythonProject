# another kind of sequences that functions much like a list
# Unlike a list, once you create a tuple, you cannot alter its contents
# count() and index() only works for tuples
# comparison operators work with tuples
x = ('Glenn', 'Sally', 'Joseph')
for iter in x:
    print(iter)

print('========++++++++++++=========')

(x, y) = (4, 'fred')
print(y)

print('========++++++++++++=========')


# sorting list of Tuples
d = {'b': 10, 'c': 1, 'a': 22}
print(d.items())
print(sorted(d.items()))

print('========++++++++++++=========')

b = {'b': 15, 'd': 2, 'e': 22}
s = sorted(b.items())
for k, v in s:
    print(k, v)

print('========++++++++++++=========')

c = {'a': 10, 'b': 1, 'c': 22}
l_list = list()
for k, v in c.items():
    l_list.append((v, k))
print(c.items())
print(l_list)

l_list = sorted(l_list, reverse=True)
print(l_list)

# top 10 most common words in a file