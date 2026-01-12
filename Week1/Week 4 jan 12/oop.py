# OOP (Object Oriented Programming)

# class

class bike:

    color = None
    headlight = None
    Wheel = 2
    Spoiler = True

    # methods
    def accelerate(self):
        print('bike is accelerating')

    def brake(self):
        print('bike is stop')

# Creating ans object od the class.
myBike = bike()
#
# #Accesing attribute of an object
# # print(myBike.color)
#
# #Changing the value of an attribute
# myBike.color = 'red'
# print(myBike.color)

#using methods
myBike.accelerate()
myBike.brake()
