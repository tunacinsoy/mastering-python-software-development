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
