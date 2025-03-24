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

#Task 2
class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def output_data(self):
        return f"Title: {self.title}, Year: {self.year}, Publisher: {self.publisher}, Genre: {self.genre}, Author: {self.author}, Price: ${self.price}"

# Example usage:
book = Book("1984", 1949, "Secker & Warburg", "Dystopian", "George Orwell", 9.99)
print(book.output_data())

#Task 3
class Stadium:
    def __init__(self, name, date_of_opening, country, city, seating_capacity):
        self.name = name
        self.date_of_opening = date_of_opening
        self.country = country
        self.city = city
        self.seating_capacity = seating_capacity

    def output_data(self):
        return f"Name: {self.name}, Date of Opening: {self.date_of_opening}, Country: {self.country}, City: {self.city}, Seating Capacity: {self.seating_capacity}"

# Example usage:
stadium = Stadium("Camp Nou", "1957-09-24", "Spain", "Barcelona", 99354)
print(stadium.output_data())
