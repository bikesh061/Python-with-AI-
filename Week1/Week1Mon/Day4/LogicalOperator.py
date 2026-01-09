#logical Operator
#True -> 1
#False -> 0

#Logical AND (*)
print(bool(True * False  * True))

#AND
print(int(True and False and False))

#Logical OR (+)
print(bool(False + True + False))

# Actual Or
print(int(True or False or True))  #1+0+1 = bool(True)

#Not Operator
print(not (False or True))

#Application of logical operators
num = 5
if not True:
    print("hello ji")
elif num <= 10 and num > 4:
    print("Num is "+str(num))