# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(name):
    print(f"Hello {name}" )
    print(f"How are you doing {name}?")
    print(f"See you later {name}!")

input_name = input("What is your name? ")
greet(input_name)