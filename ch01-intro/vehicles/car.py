"""
car.py: Module for car object

Description:
    This module contains the class definition for the car object.

Usage:
    # This module should be called/tested from the main.py script.
    cd ..
    python -m vehicles.main

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


class Car:
    # Constructor initializes object's attributes when it is created
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def decelerate(self, decrement):
        self.speed -= decrement

    def get_info(self):
        return f"{self.make}, {self.model}, {self.year} , {self.speed} kph"


def greet():
    return "Hello from the car module!"


VERSION = "1.0"
