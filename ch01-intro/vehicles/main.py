from vehicles.electric_car import ElectricCar
from vehicles.car import Car


my_car = Car("Mercedes", "A200", 2016)
my_car.accelerate(50)
print(my_car.speed)
my_car.decelerate(30)
print(my_car.speed)
print(my_car.get_info())

electric_car = ElectricCar("Tesla", "Model 3", 2022, 75)
print(electric_car.get_info())
