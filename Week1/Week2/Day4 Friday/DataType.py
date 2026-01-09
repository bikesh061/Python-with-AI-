#Datatype
# info = {
#     'class name' : 'Classroom',    #String
#     'class no' : 11,               #Integer
#     'class area' : 44.5,           #Float
#     'is class available' : True,    #bool
#     'student' : ['Bikesh','Anil', 'Kapil'],    #list
# }
from logging import INFO

#Task : take inout for class name, class no, class area, is class available and student list and store them in the above
# manner.

#After storing a dictionary print the class name, class no, class area ,print evry student name using loop(for or while)
#ans print yes the class is available and no if the class is unavailable

info = {
       'class name' : 'None',
       'class no' : None,
       'class area' : None,
       'is class avilable' : None,
       'student': None,
       }


class_name = input('enter class name :')
class_no = int(input('enter class number :'))
class_area = float(input('enter class area : '))
class_availability = bool(input('enter class avialability status: '))
students_ =[]
while True:
    student_name = input("enter student's name :" )
    students_.append(student_name)
    des = input('Do u want to enter more student? (no if u want to exit : ')
    if des.strip.lower() == 'no':
        break
info['class name'] = class_name
info['class no'] = class_no
info['is class avialble'] = class_availability
info['students'] = students_

print(f'class name : {info['class name']}')
print(f'Class no: {info['class no']}')
print(f'class area : {info['class area']}')
if info['is class avialble']:
    print('class is available')
else:
    print(f'class name : {info['class name']}')
    print(f'class no : {info['class no']}')
    print(f'class are : {info['class info']}')
    if info['is class available']:
        print('class is available!')
    else:
        print('class is unavialable')
        print(f'student in class {info['class name']}' )
    for student in info['students']:
        print(student)