def print_triangle(amount):
    for i in range(amount):
        for j in range(i+1):
            print("* ", end='')
        print()


print_triangle(5)