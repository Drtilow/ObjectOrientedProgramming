class Device:
    def __init__(self, brand, model, power, price):
        self.brand = brand
        self.model = model
        self.power = power
        self.price = price

    def output_data(self):
        return f"Brand: {self.brand}, Model: {self.model}, Power: {self.power}W, Price: ${self.price}"

class CoffeeMachine(Device):
    def __init__(self, brand, model, power, price, water_tank_capacity):
        super().__init__(brand, model, power, price)
        self.water_tank_capacity = water_tank_capacity

    def output_data(self):
        return f"{super().output_data()}, Water Tank Capacity: {self.water_tank_capacity}L"

class Blender(Device):
    def __init__(self, brand, model, power, price, jar_capacity):
        super().__init__(brand, model, power, price)
        self.jar_capacity = jar_capacity

    def output_data(self):
        return f"{super().output_data()}, Jar Capacity: {self.jar_capacity}L"

class MeatGrinder(Device):
    def __init__(self, brand, model, power, price, grinding_capacity):
        super().__init__(brand, model, power, price)
        self.grinding_capacity = grinding_capacity

    def output_data(self):
        return f"{super().output_data()}, Grinding Capacity: {self.grinding_capacity}kg/h"

# Example usage:
coffee_machine = CoffeeMachine("DeLonghi", "ECAM22.110", 1450, 499, 1.8)
blender = Blender("Philips", "HR3571", 1000, 99, 2.0)
meat_grinder = MeatGrinder("Bosch", "MFW68660", 2200, 199, 4.3)

print(coffee_machine.output_data())
print(blender.output_data())
print(meat_grinder.output_data())