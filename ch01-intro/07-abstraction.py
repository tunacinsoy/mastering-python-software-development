"""
abstraction.py: Python script to demonstrate OOP concept abstraction.

Description:
    Abstraction is the process of hiding the complex implementation details and
    showing only the necessary features of an object. Abstract classes and
    methods in Python can be created using the abc module (Abstract Base Classes)

    In Python, a class is considered an abstract class when it:
    * Inherits from the ABC class (Abstract Base Class) provided by the abc module.
    * Contains one or more abstract methods (methods decorated with @abstractmethod).

Usage:
    `python 07-abstraction.py`

Arguments:
    None

Author:
    Tuna Cinsoy

Last Modification Date:
    2024-12-07

Version:
    1.1.0

License:
    MIT License
"""

from abc import ABC, abstractmethod
import math


# The Shape class becomes an abstract base class (ABC) because it inherits ABC class.
# Trying to instantiate Shape directly will raise a TypeError.
# However, it is not a necessary for abstract classes to have at least one abstactmethod in order to be an abstract class.
class Shape(ABC):
    # We cannot directly instantiate abstract classes however abstract classes can aslo have init function.

    def __init__(self, name: str):
        self.name = name

    # @abstractmethod used to define a method that MUST be implemented by any subclass of an abstract base class.
    # It enforces that the subclass provides its own implementation of the method.
    @abstractmethod
    def get_area(self):
        # pass is useful when planning or defining a function, class, or loop that you intend to implement later.
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height, name):
        super().__init__(name)
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * math.pow(self.radius, 2)

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius


shapes = [Rectangle(4, 5, "rectangle"), Circle(3, "circle")]

print(type(Rectangle))

shape3 = Rectangle(4, 7, "rectangle3")
print(type(shape3))


for shape in shapes:
    # type(shape) returns the type of it as an object, however, if we say type(shape).__name__ it will returns its type as string.
    print(
        f"The {type(shape).__name__} has area {shape.get_area():.3f}, and perimeter {round(shape.get_perimeter())}"
    )
