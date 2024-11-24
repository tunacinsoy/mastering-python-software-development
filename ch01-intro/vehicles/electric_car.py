from vehicles.car import Car


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_level = 0

    def increase_charge(self, added_charge):
        self.charge_level += added_charge

    def get_info(self):
        return f"{super().get_info()}, Electric Car, {self.battery_capacity} kWh, {self.charge_level}% left to use."
