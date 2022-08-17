numbers = [1, 2, 3, 4, 5, 6]

numbers.append(7)

print("Numbers after append")
print(numbers)

numbers.pop(2)

print("Numbers after pop")
print(numbers)


numbers.insert(0, 0)

print("Numbers after insert")
print(numbers)

print("Print index for number 4 in the list: "+ str(numbers.index(4)))

numbers.reverse()

print("Reverse the list: "+ str(numbers))


numbers.sort()

print("Sort the list: "+ str(numbers))

print("using 4 in numbers: " + str(4 in numbers))