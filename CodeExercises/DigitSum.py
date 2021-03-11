
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number /= 10
        number = int("{:.0f}".format(number))
    print(total)

sum_of_digits(36)

