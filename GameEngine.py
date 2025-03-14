import GuessingGameNumbers
import GuessingGameWords
import Hangman

# Function to run the game depending on which button was pressed
def number_guessing_game():
    GuessingGameNumbers.start_number_guessing_game()  

def word_guessing_game():
    GuessingGameWords.start_word_guessing_game()    

def hangman():
    Hangman.start_hangman_game()  