# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ''

for letter in range (0, nr_letters):
    password = password + (letters[random.randint(0, len(letters) -1 )])
for symbol in range (0, nr_symbols):
    password = password + (symbols[random.randint(0, len(symbols) -1)])
for number in range (0, nr_numbers):
    password = password + (numbers[random.randint(0, len(numbers) -1)])

print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

sum_password = nr_letters+nr_numbers+nr_symbols
password = ''
choice = 0
for index in range (0, sum_password):
    choice = random.randint(0,2)
    if  choice == 0:
        if nr_letters > 0:
            password = password + (letters[random.randint(0, len(letters) -1 )])
            nr_letters -=1
    elif choice == 1:
        if nr_symbols > 0:
            password = password + (symbols[random.randint(0, len(symbols) -1)])
            nr_symbols -=1
    else :
        if nr_numbers > 0:
            password = password + (numbers[random.randint(0, len(numbers) -1)])
            nr_numbers -=1
print(password)
#first try :D yay


#how the instructor did it


#Eazy Level
password = ""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)
 
print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
