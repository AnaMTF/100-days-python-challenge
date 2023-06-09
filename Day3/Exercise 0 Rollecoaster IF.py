print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
if height >= 120:
  print("You can ride the rollercoaster.")
  if age <= 12:
    print("You have to pay $5.")
  elif age >= 18:
    print("You have to pay $12.")
  else:
    print("You have to pay $7.")
else:
  print("You aren't allowed to ride the rollercoaster.")
