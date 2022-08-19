str_demo = "print each character using a for loop"
list_demo = [1, 2, 3, 4, 5]

for chr in str_demo:
    print(chr)

for num in list_demo:
    print(num)

names = ["Kracken", "Seattle", "Austin", "John", "Mary"]

print()

for name in names:
    if name.startswith("J"):
        print("Found name which starts with J")
        break

print()

for name in names:
    if name.startswith("Z"):
        print("Found name which starts with Z")
        break

else:
    print("for-else executed as match was not found for the name")
