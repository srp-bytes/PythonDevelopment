course = "learning PYTHON"

print("Demo string: " + course)
print()
print("course.upper(): "+ course.upper())
print()
print("course.lower(): "+ course.lower())
print()
print("course.capitalize():" + course.capitalize())
print()
print("course.removesuffix(""python"")" + course.removesuffix("PYTHON"))
print()
print("course.removeprefix(""learning"")" + course.removeprefix("learning"))
print()
print("PYTHON" in course)
print()
print("print start index of Substring search: " + str(course.find("YTH")))
print()

temp = " string starts and ends with spaces"
print()
print(temp)
print()
print("Now trimming the spaces from the string using strip()" + temp.strip())

print()
print("Indexed access of a string using range(start, end): ")
print()

for idx in range(0, len(course)):
    print(course[idx])

print()
print("Printing each character in a string using in keyword")
print()

for char in course:
    print(char)


print()

first = "Tom"
last = "Harry"

full = f"{first} {last}"
print(full)


