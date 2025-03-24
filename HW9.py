#Task 1

class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def output_data(self):
        return f"Model: {self.model}, Year: {self.year}, Manufacturer: {self.manufacturer}, Engine Capacity: {self.engine_capacity}L, Color: {self.color}, Price: ${self.price}"

# Example usage:
car = Car("Model S", 2022, "Tesla", 3.0, "Red", 79999)
print(car.output_data())

