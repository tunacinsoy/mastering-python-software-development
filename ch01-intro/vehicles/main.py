"""
main.py: Entrypoint of the vehicles package.

Description:
    This script serves as an entrypoint for the vehicles package,
    initializing classes that are defined in modules car and electric_car.

Usage:
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

# Import Car class, greet function, and VERSION variable from vehicles.car module
from vehicles.car import Car, greet, VERSION

from vehicles.electric_car import ElectricCar


print(greet())
my_car = Car("Mercedes", "A200", 2016)
my_car.accelerate(50)
print(f"Your car's speed is: {my_car.speed} kph.")
my_car.decelerate(30)
print(f"Your car's speed is: {my_car.speed} kph.")
print(my_car.get_info())
print(VERSION)
print()

electric_car = ElectricCar("Tesla", "Model 3", 2022, 75)
electric_car.increase_charge(50)
print(electric_car.get_info())


def print_car_info(Car):
    print(Car.get_info())


print_car_info(my_car)  # Prints: Mercedes, A200, 2016 , 20 kph
print_car_info(
    electric_car
)  # Prints: Tesla, Model 3, 2022 , 0 kph, Electric Car, 75 kWh, 50% charge left to use.

# The print_car_info function can work with both Car and ElectricCar
# objects, demonstrating polymorphism in action.
