print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster.")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
  elif age > 18 and age < 45:
    bill = 12
  elif age >= 45 and age <=55:
    bill = 0
  else:
    bill = 7
  wants_photo =input("Do you want a photo? ").lower()
  if wants_photo == "yes" and bill != 0:
    bill += 3
  print(f"Your bill is ${bill}.")
else:
  print("You aren't allowed to ride the rollercoaster.")
