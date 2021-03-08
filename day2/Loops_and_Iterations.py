# Repeated steps
# while
n = 5
while n > 0:
    print(n)
    n -= 1
print('Blast off')

# break
# ends the current loop and jumps to the statement immediately following the loop
while False:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# continue
# ends the current iteration and jumps to to the top of the loop and starts the next iteration

while True:
    n = input('Enter number')
    n = int(n)
    if n % 2 != 0:
        print('Odd')
    else:
        print('Even')
    ans = input('do you want to continue... ')
    if ans == 'no':
        break
    else:
        continue

