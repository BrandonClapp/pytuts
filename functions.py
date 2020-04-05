def print_numbers(a, b, c):
    print(f"The numbers are: {a} {b} {c}")
    # print("The numbers are: " + a + " " + b + " " + c)


def add_numbers(a, b):
    return a + b


print_numbers(1, 2, 3)
print_numbers(99, 98, 97)

sum = add_numbers(2, 4)
print("Result of adding numbers: " + str(sum))
