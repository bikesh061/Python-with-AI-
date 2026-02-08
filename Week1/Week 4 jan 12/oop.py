# OOP (Object Oriented Programming)

# class

class bike:

    color = None
    headlight = None
    Wheel = 2
    Spoiler = True

    #Constructor
    def __init__(self,color,headlight,Wheel):
        self.color = color
        self.headlight = headlight
        self.spoiler = spoiler

    # methods
    def accelerate(self):
        print('bike is accelerating')

    def brake(self):
        print('bike is stop')

# Creating an object od the class.
myBike = bike('red','square','60km/h', True)
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
