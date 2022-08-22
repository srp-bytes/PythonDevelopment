monthConversions = {
    "jan": "january",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "june": "june"
}

print()
print("print all items in a dictionary: ")

print(monthConversions.items())

print()
print("Get value for a key: mar")

print(monthConversions.get("mar"))

print()

print("print values in dictionary: ")

print(monthConversions.values())

print()

print("Insert a key which is not available in the dictionary: ")

monthConversions.update({"july": "july"})

print()

print("Print values in dictionary after update: ")

print(monthConversions)

print()

print("Print keys from dictionary using for loop: ")

for ele in monthConversions:
    print(ele)