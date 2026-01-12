 #Datatype
# info = {
#     'class name' : 'Classroom',    #String
#     'class no' : 11,               #Integer
#     'class area' : 44.5,           #Float
#     'is class available' : True,    #bool
#     'student' : ['Bikesh','Anil', 'Kapil'],    #list
#       'new info' : {'name' : 'Bikesh'} #Dictionary vitra dictionary rakhna milxa
#
from logging import INFO

#Task : take inout for class name, class no, class area, is class available and student list and store them in the above
# manner.

#After storing a dictionary print the class name, class no, class area ,print evry student name using loop(for or while)
#ans print yes the class is available and no if the class is unavailable

info1 = {
'class name' : None,                 #String
    'class no' : None,               #Integer
    'class area' : None,             #Float
    'is class available' : None,     #bool
    'students' : None,               #list of students
}
#input class information
class_name = input("Enter class name: ")
class_no = int(input("enter a class no: "))
class_area = float(input("enter a class area: "))
class_availability = bool(input("enter class  avalability: ")) #Handle availability properly
# Input students
students_ = []
while True:
    student_name = input("enter student name: ")
    students_.append(student_name)
    des = input('Do u want to enter more students? : (no if you want to exit): ')
    if des.strip().lower() == 'no':
        break
# Store data in dictionary
info1['class name'] = class_name      #dictioanry ma add
info1['class no'] = class_no
info1['class area'] = class_area
info1['is class available'] = class_availability
info1['students'] = students_

#print class Infromation
print(f'Class name : {info1['class name']}')
print(f'Class no : {info1['class no']}')
print(f'Class area : {info1['class area']}')
if info1['is class available']:
      print('class is avilable!')
else:
    print('class is unavailable!')
print(f"Students in class {info1['class name']}:")
for student in info1['students']:
    print(student)