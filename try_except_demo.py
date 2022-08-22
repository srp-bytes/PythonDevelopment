try:
    number = int(input("Enter a number: "))
    print("User input number: " + str(number))
except ValueError as err:
    print("Invalid number entered and encountered an " + str(err))



