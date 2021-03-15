# }b is a number that is the sum of its own digits each raised to the power of the number of digits.

# Finds the armstrong number between the given range
# @param num_1  the starting point of the range
# @param num_2 the end point of the range
def generator(num_1, num_2):

    a_number_list = list()
    for number in range(num_1, num_2):
        power = len(str(number))
        total = 0
        temp_n = number
        while temp_n > 0:
            digit = temp_n % 10
            total += pow(digit, power)
            temp_n = temp_n // 10
        if total == number:
            a_number_list.append(number)
    print(a_number_list)
generator(0, 10000000)