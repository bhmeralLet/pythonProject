# List constants are surrounded by square brackets
# A list element can be any Python object

lotto = [2,14,31,43,124]
print(lotto)
lotto[1] = 23
print(lotto)

print(len(lotto)) # number of things in the list

# range -> returns a list of numbers that range from zero to one less than the parameter
# can help creating loops
l = range(3, 12, 2)
for n in l:
    print(n)

print('========++++++++++++=========')


friends = ['Joe', 'Lily', 'Jorge']
for i in range(len(friends)):
    friend = friends[i]
    print('Happy Birthday: ' + friend)

print('========++++++++++++=========')


# Concatenating lists using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
# lists can be sliced using :
d = [1, 2, 3, 4, 5, 6, 7, 8]
print(d[0:3])
print(d[7:])

print('========++++++++++++=========')

# List from scratch
shpList = list()
shpList.append('egg')
shpList.append('milk')
shpList.append('flour')
print(shpList)

print('========++++++++++++=========')
# logical operator
list = [1,2,3,4]
print(4 in list)
print(5 not in list)

print('========++++++++++++=========')

# ordering
letters = ['g', 'c', 'b', 'a']
letters.sort()
print(letters)

print('========++++++++++++=========')

nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))
print(sum(nums))

# split -> breaks a string into and produces a list of strings.
# by default it splits by spaces you can give parameter to split based on what you want
sentence = 'Dab on fools'
words = sentence.split()
print(words)

