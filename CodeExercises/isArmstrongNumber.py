# b is a number that is the sum of its own digits each raised to the power of the number of digits.
# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.

# Checking if the number is armstrong or not and based on that it returns True or False
# @param number   the number you wanna check if its armstrong or not
def is_armstrong_number(number):
    msg = 'The ' + str(number) + ' is armstrong number :'
    total = 0

    for i in str(number):
        total += pow(int(i), len(str(number)))

    if total == number:
        return msg, True
    else:
        return msg, False


# // for not getting the decimal point
# where were you when I need it

def is_armstrong_number_v2(number):
    msg = 'The ' + str(number) + ' is armstrong number :'
    total = 0
    power = len(str(number))
    # assigning the number to a temporary value for the calculation
    # if we use the number parameter itself the number gonna change because of the division
    # and at the if condition we will get false
    temp = number
    while True:
        digit = temp % 10
        total += pow(digit, power)
        temp = temp // 10
        if temp == 0:
            break


    if total == number:
        return msg, True
    else:
        return msg, False



print(is_armstrong_number(1634))
print(is_armstrong_number_v2(1634))

