# Conditional Structures
# Indentation :
#         increase indent after an if statement or for statement
#         maintain indent to indicate the scope of the block (lines effected by the if/for)

# if
x = 5
if x > 2:
    print('Bigger than 2')
print('done with 2')
print("============")

# else
x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print("============")

# else if
x = 10
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All Done')
print("============")

# try/except
# similar to try/catch
# after catching any exception it will immediately goes to expect block and the code under the exception wont execute.
try:
    print(10 / 0)
except ArithmeticError:
    print("Arithmetical Error Occurred")


