class Human:
    name = None
    age = 20
    is_married = None

    def say_hello(self):
        print("Hello")


adam = Human()
eva = Human()
eva.name = "Eva"

print(
    adam.name
)
print(
    eva.name
)
print(adam)
print(eva)

adam2 = adam
adam2.name= "TEST"

print()
print(
    adam.name
)
print(
    adam2.name
)
print(adam)
print(adam2)
