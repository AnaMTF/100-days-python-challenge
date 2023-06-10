rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

human_choice = int(input(
    "What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors\nInput:"
))
computer_choice = random.randint(0, 3)
is_draw = False
is_win = False
is_loss = False
#Display human choice
if human_choice == 0:
  print(rock)
  if computer_choice == 0:
    is_draw = True
    print("Computer chose:")
    print(rock)
  elif computer_choice == 1:
    is_loss = True
    print("Computer chose:")
    print(paper)
  else:
    is_win = True
    print("Computer chose:")
    print(scissors)
elif human_choice == 1:
  print(paper)
  if computer_choice == 0:
    is_win = True
    print("Computer chose:")
    print(rock)
  elif computer_choice == 1:
    is_draw = True
    print("Computer chose:")
    print(paper)
  else:
    is_loss = True
    print("Computer chose:")
    print(scissors)
else:
  print(scissors)
  if computer_choice == 0:
    is_loss = True
    print("Computer chose:")
    print(rock)
  elif computer_choice == 1:
    is_win = True
    print("Computer chose:")
    print(paper)
  else:
    is_draw = True
    print("Computer chose:")
    print(scissors)
if is_draw:
  print("It's a draw!")
if is_win:
  print("You win!")
if is_loss:
  print("You lose!")
