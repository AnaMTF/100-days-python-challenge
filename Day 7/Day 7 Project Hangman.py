#Step 5
import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

list_of_wrong_guesses = []
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    ok = False
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            ok = True
    if not ok:
        lives = lives - 1
        print(stages[lives])
        if guess not in list_of_wrong_guesses:
            list_of_wrong_guesses.append(guess)
        print(f"Wrong guesses: {list_of_wrong_guesses}")
    if lives == 0:
        end_of_game = True
        print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("""Art by Joan Stark
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\ /.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\ .   '
      *            *..*         :
jgs     *
        *""")
        print("You win.")
