#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random as rnd	 
#Write the rest of your code below this line 👇

heads_tails = rnd.randint(0,1)

if heads_tails == 0:
    print("Heads")
else:
    print("Tails")
