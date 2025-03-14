import random
import PySimpleGUI as psg

psg.theme('LightBlue7')

# List of words to guess
def choose_word():
    words = ['school', 'python', 'banana', 'chocolate', 'chicken', 'apple', 'elephant', 'excited', 'divide', 'store', 'sell', 'accidental', 'recognize', 'comfort', 'police', 'bean']
    return random.choice(words)

# Display the correct letters guessed in the word
def display(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

# Defining the hangman popup
def hangman_popup():
    word = choose_word()
    guessed_letters = []
    attempts = 8
    coins = 0

    # Layout for the Hangman game popup
    layout = [
        [psg.Text("Welcome to Hangman!", font=('Helvetica', 14))],
        [psg.Text("Word to guess:", font=('Helvetica', 12)), psg.Text("", key="word_to_guess", font=('Helvetica', 16))],
        [psg.Text("Attempts left:", font=('Helvetica', 12)), psg.Text(str(attempts), key="attempts", font=('Helvetica', 14))],
        [psg.Text("Guessed letters:", font=('Helvetica', 12)), psg.Text("", key="guessed_letters", font=('Helvetica', 14))],
        [psg.InputText("", size=(5, 1), key="guess", font=('Helvetica', 14), justification='center')],
        [psg.Button("Guess", font=('Helvetica', 14)), psg.Button("Exit", font=('Helvetica', 14))],
        [psg.Text("", key="result", font=('Helvetica', 14))],
    ]

    # Window for hangman popup
    window = psg.Window("Hangman Game", layout, finalize=True, modal=True)

    # While the player has not run out of attempts
    while attempts > 0 and display(word, guessed_letters).count('_') > 0:
        window['word_to_guess'].update(display(word, guessed_letters))  
        window['attempts'].update(str(attempts))
        window['guessed_letters'].update(", ".join(guessed_letters))

        event, values = window.read()

        if event == psg.WIN_CLOSED or event == "Exit":
            window.close()
            return

        if event == "Guess":
            guess = values["guess"].lower()

            # If the player does not guess a valid letter
            if len(guess) != 1 or not guess.isalpha():
                window['result'].update("Please enter a valid letter.")
                continue

            # If the player has already guessed a letter
            if guess in guessed_letters:
                window['result'].update(f"You already guessed '{guess}'!")
                window['guess'].update('')
                continue

            guessed_letters.append(guess)

            # If the player guesses a letter right
            if guess in word:
                window['result'].update(f"Good job! '{guess}' is in the word.")
            # If the player guesses a letter wrong
            else:
                window['result'].update(f"Oops! '{guess}' is not in the word.")
                attempts -= 1

            # Update the displayed word to show correct guesses
            current_display = display(word, guessed_letters)
            window['word_to_guess'].update(current_display)

            # If the player guesses the word right
            if current_display == word:
                window['result'].update(f"Well done! You got the word right. You have won {coins + 20} coins!")
                coins += 20  
                window['guess'].update('') 
                break

            window['guess'].update('')  

        window.refresh()

    # If the player runs out of attempts
    if attempts == 0:
        window['result'].update(f"Sorry! You've run out of attempts. The word was '{word}'.")

    event, values = window.read()
    window.close()

def start_hangman_game():
    hangman_popup()

