# needs debugging for numbers that decimal point is bigger than or equal to 5
# it rounds the number and result gets more
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number /= 10
        number = int("{:.0f}".format(number))
    print(total)

sum_of_digits(22)

