print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster.")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
  elif age > 18:
    bill = 12
  else:
    bill = 7
  wants_photo =input("Do you want a photo? ").lower()
  if wants_photo == "yes":
    bill += 3
  print(f"Your bill is ${bill}.")
else:
  print("You aren't allowed to ride the rollercoaster.")
