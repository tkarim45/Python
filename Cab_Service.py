class Vehicle:

    # Class Attributes or Global Variables
    noofcabs = 0
    noofpassengers = 0
    minimumrate = 50

    """When you use __int__ method, you can access variables only after you
    create an object. These variables are called Instance Variables or local
    variables. One which is defined outside of methods are called Class Variables
    or global variables. You can access these variables anywhere in the class."""
    def __init__(self, name, km_run, pick_n_drop, cab_fare, no_of_passengers):
        # Instance Attributes or Local Variables
        self.name = name
        self.km_run = km_run
        self.pick_n_drop = pick_n_drop
        self.cab_fare = cab_fare
        Cab.noofcabs = Cab.noofcabs + 1
        Cab.noofpassengers += no_of_passengers

    @property
    def email(self):
        return self.name + '@gmail.com'

    @email.setter
    def email(self, name):
        self.name = name

    # Instance Method
    def rate_per_km(self):
        return self.cab_fare / self.km_run

    """Method overriding allows us to have a method in the child class with
     the same name as in the parent class but the definition of the child 
     class method is different from parent class method."""
    def message(self):
        print("Parent class method")

    # Class Method
    """ alternative method of a constructor and is used when we want to access 
    the property of the class and not a specific instance of that class"""
    @classmethod
    def no_of_cabs(cls):
        return cls.noofcabs

    @classmethod
    def avg_no_of_passengers(cls):
        return int(cls.noofpassengers / cls.noofcabs)

    """It is mainly useful for creating helper or utility functions"""
    @staticmethod
    def billValidation(pay):
        return int(pay) > 0

    """It allows you to define a function or method with flexibility so
    that you can call it with only some of the arguments and no need to
    specify the other arguments. You can also call it with all the arguments."""
    @staticmethod
    def phrase(string="I am a Programmer"):
        return string

    def __del__(self):
        print('Destructor called, Employee deleted.')

# Inheritance
class Cab(Vehicle):

    def __init__(self, name, km_run, pick_n_drop, cab_fare, no_of_passengers, cabtype, modelno):
        super().__init__(name, km_run, pick_n_drop, cab_fare, no_of_passengers)

        # Instance Attributes or Local Variables
        self.cabtype = cabtype

        # two underscores '__' it becomes private single underscore '-' it becomes protected
        self.__modelno = modelno

    def message(self):
        print("Child Cab class method")

# Inheritance
class Bus(Vehicle):
    def __init__(self, name, km_run, pick_n_drop, cab_fare, no_of_passengers, color):
        super().__init__(name, km_run, pick_n_drop, cab_fare, no_of_passengers)

        # Instance Attributes or Local Variables
        self.color = color

    def message(self):
        print("Child Bus class method")


"""Any code that is inside if __name__ == '__main__': will be executed when
you run your .py file. If you import module import Mymodule, the code inside 
if __name__ == '__main__': won't be run """

if __name__ == '__main__':
    parent = Vehicle("ZM", 120, ['lhr', 'hyd'], 6700, 6)
    first = Cab("Mn", 100, ['lhr', 'khr'], 5000, 6, 'SUV', 537521732187)
    second = Bus("TM", 60, ['lhr', 'isl'], 500, 6, 'Black')
    # second = Cab("TM", 60, ['lhr', 'isl'], 500, 6, '')
    # third = Cab("ZM", 120, ['lhr', 'hyd'], 6700, 6)

    print(first.name)
    print(second.name)
    # print(second.name)
    # print(third.name)

    print(Cab.no_of_cabs())
    print(Cab.avg_no_of_passengers())

    print(first.billValidation(first.cab_fare))
    print(second.billValidation(second.cab_fare))

    print(first.cabtype)
    print(second.color)

    print(parent.message())
    print(first.message())
    print(second.message())

    print(parent.phrase("Hello World"))
    print(parent.phrase())

    # print(first.modelno)
    print(first._Cab__modelno)

    # Getter
    print(first.email)
    first.name = "HG"

    print(first.email)
    # Setter
    first.email = "MN"

    print(first.name)
    print(first.email)


