# Function are reusable block of code.

#it take inout and gives certain output

#Function take input and gives output

# The parameter are the variable that is declared when defining a function,
# argument are the values that we pass when calling the funcion.  #

# def my_function(x):
#     y = 2*x
#     print(f'When x is {x}, y is {y}')
#   Calling funct  ion and argument
# my_function(2)
# my_function(3)
# my_function(4)
# my_function(5)
g = 67

def my_function(x, y):
    z = 2*x+y
    print(f'when x is {x},y is {y} then z is {z}')
my_function(1,2)
my_function(4,5)
my_function(1,4)
my_function(6,8)

# Task : Take 1st name and last name as input parameter for the function and
# print " my name is First_name Last_name"

def Full_Name(first_name, last_name):
    return first_name + " " + last_name
    print(len(" "))



name = Full_Name("bikesh", "Shakya")
print(name)