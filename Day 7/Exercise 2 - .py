#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
is_end_of_game = False
#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all 
# the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while not is_end_of_game:
    guess = input("Guess a letter: ").lower()
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index]=guess
    print(display)
    if "_" not in display:
        is_end_of_game = True
        print("You win!")