from Chef import Chef
from Student import Student
from ChineseChef import  ChineseChef

student = Student("john", 21, "CS", 3.1)
print(student)
student.print_student_details()

myChef = Chef()

myChef.make_salad()
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()

myChineseChef.make_salad()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()
