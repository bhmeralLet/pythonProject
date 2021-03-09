# can convert numbers in a string into a number with int()
# index value starts with 0


word = "bananarang"
index = 0
for i in word:
    print(i)
while index < len(word):
    print(index,word[index])
    index += 1


print('========++++++++++++=========')

word = 'Java'
index = 0
while True:
    count = word.count(word[index], index, len(word))
    print(word[index], count)
    index += 1
    if index == len(word) - 1:
        break

print('========++++++++++++=========')

# slicing Strings
# substring in Java
s = "Leroy Jenkins"
print(s[0:4])
print(s[6:15])
print(s[:])
# Unlike Java you won`t get index out of bound exception when giving end point

print('========++++++++++++=========')


# "in" as a logical operator
word = 'fevzi'
print('n' in word)
print('fev' in word)

print('========++++++++++++=========')

# len() -> length of the string
fruit = "ananas"
print('Length of the ananas ',len(fruit))

print('========++++++++++++=========')

# lower() -> lower case string
kenobi = "Hello there"
general = kenobi.lower()
print(general)

# upper() -> upper case string
kenobi = "Hello there"
general = kenobi.upper()
print(general)

print('========++++++++++++=========')

# find(self,optionalStartPoint,optionalEndPoint)
# -> searching for a substring within another string returns the position of the first occurrence
# if the substring does not exist it returns -1
fruit = 'ananas'
pos = fruit.find("a")
print(pos)

print('========++++++++++++=========')

# replace()
hello = "Hello There"
print(hello)
hello = hello.replace('Hello', 'Hi')
print(hello)

print('========++++++++++++=========')

# lstrip() & rstrip() -> removing white space at the left or right

# startswith() -> returns boolean
