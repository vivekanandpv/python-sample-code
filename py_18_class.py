class Vehicle:
    '''Vehicle class represents all vehicles'''

    #   class variable is shared by all instances
    #   this is NOT a static variable of Java, but provides a default value
    #   objects can customize this
    description = 'default description of vehicle'

    def __init__(self, make, model):
        self.make = make
        self.model = model

    #   human readable string form
    def __str__(self):
        return f'Vehicle; make: {self.make}; model: {self.model}'

    #   unique string for system needs
    def __repr__(self):
        return f'{self.make}/{self.model}'

    #   instance methods get the current object as the first argument
    #   conventionally written as self, though self is not a keyword
    #   self is passed automatically when you call the method on an object
    def drive(self):
        print(f'Driving {self.make} {self.model}')

    #   usually, you provide APIs to deal with data
    #   Python doesn't provide any construct for private access
    #   Usually, the methods are prefixed with _ or __ to mark them as
    #   private implementations. The meaning is users should not depend on it
    def set_make(self, make):
        self.make = make

    #   class methods do get a class reference (conventionally as cls)
    @classmethod
    def class_method(cls):
        print(f'Executing a class method: {cls}')

    #   static method gets no reference either of class or of instace
    #   sometimes it is better to write such a method outside as a simple function
    @staticmethod
    def static_method(message):
        print(f'Executing a static method: {message}')


# creating an object or instance is by calling the class
vehicle_1 = Vehicle('Suzuki', 'Baleno')
vehicle_1.drive()
print(vehicle_1)  # __str__
print(repr(vehicle_1))  # __repr__
print(vehicle_1.description)    # class variable

vehicle_2 = Vehicle('Hyundai', 'Verna')
print(vehicle_2.description)

vehicle_1.description = 'Description of Baleno'  # changes only for this instance

print(vehicle_1.description)
print(vehicle_2.description)    # not changed!
