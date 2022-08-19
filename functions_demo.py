def add_numbers(num1: int, num2: int):
    return num1 + num2


def returning_multiple_numbers(num1, num2=3):
    return num1, num2, num1 + num2


def args_demo(*tup):
    total = 1
    for number in tup:
        total *= number
    print(total)


def save_user(**user):
    print(user)


print(add_numbers(1, 2))
print()

number_tuple = returning_multiple_numbers(1, 2)
print(number_tuple)

print()
print("Demo passing multiple args to a function")
args_demo(2)
args_demo(2, 3, 4, 5)

print()
save_user(id=1, name='python', age=25)