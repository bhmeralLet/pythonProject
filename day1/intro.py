# Conditional Step
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Done')
# Repeated Step
v = 5
while v > 0:
    print(v)
    v = v - 1
print('Take Off')
# Numeric expressions
# Precedence Rules -> Parenthesis -> Power -> Multiplication, D, R -> Addition, S -> Left to Right
y = 2
y = y + 2
print(y)
z = 45 * 4
print(z)
d = z / 100
print(d)
l = 43
k = l % 10
print(k)
# Power
print(9 ** 2)

# type() -> showing the data type of the variable
print(type(k))
# Integer division produces a floating point result
print(9/2)
# can use int() and float() to convert between strings and integers
str = '123'
str = int(str)
print(str + 1)

# we can instruct python to pause and read data from the user using the input() function . it returns string
# similar to the Scanner
nam = input('Who are you')
print("Welcome", nam)

