from abc import ABC, abstractmethod

#   all abstract classes inherit from ABC (Abstract Base Class) superclass


class Shape(ABC):
    def instance_method(self):
        print('instance method in Shape')

    #   subclasses must override the abstract methods
    #   Technically, you can still provide a method body
    #   but it is useless as the subclasses override anyway
    @abstractmethod
    def draw(self):
        print('Useless')


class Circle(Shape):
    #   a subclass of an abstract class can still choose not to implement
    #   the abstract method
    #   but this will be caught at the initialization time
    #   remember Python is a dynamically-typed language
    #   there is no static type-checking here
    def draw(self):
        #   pass doesn't work here, see the above comment
        print('Circle draws')


circle_1 = Circle()
circle_1.draw()
