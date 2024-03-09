import random 
from Hangman_words import word_list
from Hangman_logo_stages import logo, stages
import os

print(logo)
print("\nWelcome to the HANGMAN game!")
chosen_word = random.choice(word_list)   # initial condition for choosing word 
word_length = len(chosen_word)   
lives = 6

display_list = []
for _ in chosen_word:     # Loop for displaying blanks
    display_list.append('_')
sdisplay_list = " ".join(display_list)
print(sdisplay_list)

endofgame = False

while endofgame == False:
      
    guess = (input("\nGuess a letter: ")).lower()
    os.system('cls') 
    if guess in display_list:
        print("You've already guessed that letter!")     # Condition for already guessed
    
    for position in range(word_length):  # Condition for right guess
        letter = chosen_word[position]
        if letter == guess:
            display_list[position] = letter
    
    if guess not in chosen_word:  # Condition for wrong guess
        lives -= 1
        print("\nYou've gussed a wrong letter you loose a life")
        if lives == 0:
            endofgame = True
            print(f"\nYou loose! (The answer was: {chosen_word})")

    sdisplay_list = " ".join(display_list)  # Displaying letters after cls
    print("\n"+sdisplay_list)

    if "_" not in display_list: # After guessing all the letters
        endofgame = True 
        print("\nYou win!")
    # livesleft = lives
    print(f"\nLives left: {lives}")
    print(stages[lives])