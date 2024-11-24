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

Date:
    2024-11-24

Version:
    1.0.0

License:
    MIT License
"""

from abc import ABC, abstractmethod
import math


# The Shape class becomes an abstract base class (ABC) because it contains at least one abstract method.
# Trying to instantiate Shape directly will raise a TypeError.
class Shape(ABC):

    # @abstractmethod used to define a method that must be implemented by any subclass of an abstract base class.
    # It enforces that the subclass provides its own implementation of the method.
    @abstractmethod
    def get_area(self):
        # pass is useful when planning or defining a function, class, or loop that you intend to implement later.
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * math.pow(self.radius, 2)

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius


shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print(
        f"The {type(shape).__name__} has area {shape.get_area():.3f}, and perimeter {round(shape.get_perimeter())}"
    )
