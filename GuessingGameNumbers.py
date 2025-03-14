import random
import PySimpleGUI as psg

psg.theme('LightBlue7')

def number_guessing_popup():
    number_to_guess = random.randint(1, 100)
    max_attempts = 8
    attempts = 0
    guessed_numbers = []  

    # Layout for Number Guessing Game popup
    layout = [
        [psg.Text("Welcome to the Number Guessing Game!", font=('Helvetica', 14))],
        [psg.Text(f"I am thinking of a number between 1 and 100. You have {max_attempts} attempts.", font=('Helvetica', 12))],
        [psg.Text("Enter your guess:", font=('Helvetica', 12))],
        [psg.InputText("", size=(5, 1), key="guess", font=('Helvetica', 14), justification='center')],
        [psg.Button("Guess", font=('Helvetica', 14)), psg.Button("Exit", font=('Helvetica', 14))],
        [psg.Text("", key="feedback", font=('Helvetica', 12))],
        [psg.Text("", key="attempts", font=('Helvetica', 12))],
    ]

    # Creating the window for the Number Guessing Game
    window = psg.Window("Number Guessing Game", layout, finalize=True)

    while attempts < max_attempts:
        event, values = window.read()

        if event == psg.WIN_CLOSED or event == "Exit":
            break

        if event == "Guess":
            guess = values["guess"]

            # If the player does not guess a number
            if not guess.isdigit():
                window['feedback'].update("Please enter a valid number.")
                continue

            guess = int(guess)

            # If the player does not guess a number between 1 and 100
            if guess < 1 or guess > 100:
                window['feedback'].update("Please guess a number between 1 and 100.")
                continue

            # If the player guesses a number more than once
            if guess in guessed_numbers:
                window['feedback'].update("You have already guessed this number, please try another one.")
                window['guess'].update("")  # Clear the input the player made
                continue

            guessed_numbers.append(guess)  # Add the guess to the list of guessed numbers
            attempts += 1

            # Clears the input after the player guesses
            window['guess'].update('')

            # If the player guesses an incorrect number
            if guess < number_to_guess:
                window['feedback'].update("Too low! Try again.")
            elif guess > number_to_guess:
                window['feedback'].update("Too high! Try again.")
            else:
                # Outcomes of correct guesses
                window['feedback'].update(f"Correct! The number was {number_to_guess}.")
                window['attempts'].update(f"You guessed it in {attempts} attempts!")
                window['feedback'].update(f"Congratulations! You've won 5 coins!")
                break  

            # Updates how many attempts the player has left
            window['attempts'].update(f"Attempts left: {max_attempts - attempts}")

    # If the player runs out of attempts
    if attempts == max_attempts and guess != number_to_guess:
        window['feedback'].update(f"Sorry! You've used all {max_attempts} attempts. The correct number was {number_to_guess}.")
    
    # Do not close unless the player closes the popup
    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == "Exit":
            break

    window.close()

def start_number_guessing_game():
    number_guessing_popup()





