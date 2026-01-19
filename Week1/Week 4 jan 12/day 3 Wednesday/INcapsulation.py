#encapsulation

# protecting the attributes

class Bike:
    #Attributes
    wheels = 2
    headlight_status = False

    #Constuctor

    def __init__(self, color, headlight, speed, spoiler, fuel):
        self.__color = color
        self._headlight = headlight
        self.speed = speed
        self.fuel = fuel
        self.spoiler = spoiler

    #Getter (Accessor)
    def get_color(self):
        return self.__color

    #Setter (Mutator)
    def set_color(self, color):
        self.__color = color



myBike = Bike('red','square','60KM/H',True,'50L')
#private variable can't be access outside class

# print(myBike.color)