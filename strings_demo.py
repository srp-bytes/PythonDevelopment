course = "learning PYTHON"

print("Demo string: " + course)
print("course.upper(): "+ course.upper())
print("course.lower(): "+ course.lower())
print("course.capitalize():" + course.capitalize())
print("course.removesuffix(""python"")" + course.removesuffix("PYTHON"))
print("course.removeprefix(""learning"")" + course.removeprefix("learning"))
print("PYTHON" in course)

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