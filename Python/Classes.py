#Here we have created class named car and have added attributes like the brand and model name!.

class Car:
    def __init__(self,brand ,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Mercedes","cdi220d")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())