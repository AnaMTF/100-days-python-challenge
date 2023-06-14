#Function with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

name = input("What is your name? ")
location = input("Where are you from? ")
greet_with(name, location)
#If the order of the arguments is not the same as in the function definition
greet_with(location = location, name = name)