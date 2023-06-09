print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
ionut_proof = False
step_1 = input("You're at a crossroad. Which path do you take? Left or Right?").lower()
if step_1 == "left":
    step_2 = input("Now you found a river, what do you do? Swim or Go Around?").lower()
    ionut_proof = True
    if step_2 == "swim":
        step_3 = input("You found a chest with a lock, what do you do? Pick it or Break it?").lower()
        ionut_proof = True
        if step_3 == "pick it":
            print("Congrats! You found 300 robux in the chest!")
            ionut_proof = True
        elif step_3 == "break it":
            print("Sadly, you broke your hand with the rock. GAME OVER ")
            ionut_proof = True
        else:
            print("te bat")
    elif step_2 == "go around":
        print("You walked for 1001 days and nights and didn't find a bridge. You died of starvation and dehydration. GAME OVER ")
        ionut_proof = True
    else:
        print("te bat")
elif step_1 == "right":
    print("You found yourself in Galați and got your kidney stolen. GAME OVER ")
    ionut_proof = True

if not ionut_proof:
    print("Smartass, choose one of the two options listed >:(")
