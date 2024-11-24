"""
electric_car.py: Module for electric_car object

Description:
    This module contains the class definition for the electric_car object.
    It inherits the car module, and overrides its superclass' get_info(self) function.

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

from vehicles.car import Car


# ElectricCar(Car) indicates that this class inherits Car class
# Inheritance allows a class to inherit attributes and methods from another
# class. This promotes code reuse and allows for the creation of hierarchical
# relationships between classes.
class ElectricCar(Car):
    def __init__(self, make: str, model: str, year: int, battery_capacity: float):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_level = 0

    def increase_charge(self, added_charge: float):
        self.charge_level += added_charge

    def get_info(self):
        return f"{super().get_info()}, Electric Car, {self.battery_capacity} kWh, {self.charge_level}% charge left to use."
