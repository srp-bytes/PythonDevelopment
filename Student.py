class Student:

    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def print_student_details(self):
        str_age = str(self.age)
        str_gpa = str(self.gpa)
        print("Student attributes: " + self.name + "," + str_age + "," + self.major + "," + str_gpa)
