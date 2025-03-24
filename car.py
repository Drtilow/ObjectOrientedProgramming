# Definice třídy Car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"Značka: {self.brand}, Model: {self.model}, Rok: {self.year}"

# Vytvoření objektů třídy Car
car1 = Car("Tesla", "Model S", 2022)
car2 = Car("Ford", "Mustang", 2021)

# Výpis atributů objektů
print(car1.car_info())
print(car2.car_info())
