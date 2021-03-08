# in keyword
# the iteration variable moves through all of the values "in" the sequence

# none is to make the code work for every number
# we can`t give smallest number a data type can hold like in Java e.g. (Integer.MIN_VALUE, Integer.MAX_VALUE)
smallest = None
print("Smallest No." , smallest)
for i in [10,13,23,4,2,1,0]:
    if smallest is None or i < smallest:
        smallest = i
        print("Current Smallest No. of the Set", smallest)
print("Smallest No.", smallest)


count = 0
total = 0
for i in [1,7,8,4,17]:
    count += 1
    total += i
avg = total / count
print('Average is: ', avg)

divisible = False
for i in [3,13,16,21,33,9]:
    if i % 3 == 0:
        divisible = True
    else:
        divisible = False
    print(i," can divide by 3 :", divisible)

# "is" & "is not" -> logical expressions (mostly use in boolean and None)
# similar to == but it looks at the data type as well as data value

