class Dog:
    """When you use __int__ method, you can access variables only after you
    create an object. These variables are called Instance Variables or local
    variables. One which is defined outside of methods are called Class Variables
    or global variables. You can access these variables anywhere in the class."""
    # class variable shared across all instances
    # used when there are things common between instances
    animal_legs = 4

    # protected Variable
    _property = "taimour"

    # private variable
    __property_owner = "taimour"

    # init act as a constructor in python
    # self means the class objects itself
    # aname, abreed etc. are instance variable only unique to that instance
    def __init__(self, aname, abreed, acoat, acolor):
        self.name = aname
        self.breed = abreed
        self.coat = acoat
        self.color = acolor

    # print details are function attribute of the class
    # self.name is also the attribute of the class too
    def printdetails(self):
        print(f'Name: {self.name} \nBreed: {self.breed}\nCoat: {self.coat}\nColor: {self.color}')

    """ alternative method of a constructor and is used when we want to access 
    the property of the class and not a specific instance of that class"""
    @classmethod
    def something(cls):
        return cls.animal_legs

    # Class method can access and modify the class state. Static Method cannot access or modify the class state
    @staticmethod
    def check(breed):
        if breed == "German Shephard":
            return True
        else:
            return False

    # It is used to produce readable representation of the object.
    def __str__(self):
        return 'Name: ' + self.name + '\n' + 'Breed: ' + self.breed + '\n' + 'Coat: ' + self.coat + '\n' + 'Color: ' + self.color

# This is how Inheritance in python
class police_dog(Dog):
    def __init__(self, aname, abreed, acoat, acolor, weight, exp):
        self.name = aname
        self.breed = abreed
        self.coat = acoat
        self.color = acolor
        self.weight = weight
        self.exp = exp

    def print(self):
        print(f'Name: {self.name} \nBreed: {self.breed}\nCoat: {self.coat}\nColor: {self.color}\nWeight: {self.weight}\nExp: {self.exp}')


if __name__ == '__main__':
    # max is the class Instance
    max = Dog("Max", "German Shephard", "Single", "Black and Brown")

    # mee = Dog.something()
    # print(mee)

    # print(Dog.check(max.breed))
    # print(mee.printdetails())

    maximus = police_dog("Max", "German Shephard", "Single", "Black and Brown", 45, 2)
    # print(maximus.print())

    # This is how you access protected variable
    # print(Dog._property)

    # this is how to access private variable
    # print(Dog._Dog__property_owner)

    # print(max)
