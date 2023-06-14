# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

is_leap = True

if year%4 == 0:
    is_leap = True
    if year%100 == 0:
        is_leap = False
        if year % 400 == 0:
            is_leap = True
else:
    is_leap = False

if is_leap:
    print ("Leap year.")
else:
    print("Not leap year.")
