import random
import PySimpleGUI as psg
import wallet

psg.theme('LightBlue7')

# The theme options + words listed for themes
Themes = {
    "Animals": ['cat', 'dog', 'elephant', 'giraffe', 'lion', 'tiger', 'zebra'],
    "Foods": ['apple', 'banana', 'chocolate', 'pizza', 'sushi', 'hamburger', 'pasta'],
    "Countries": ['india', 'brazil', 'canada', 'france', 'germany', 'japan', 'australia'],
}

# A random word based on the theme selected
def choose_word(theme):
    return random.choice(Themes[theme])

# Give a hint if the word is guessed wrong
def provide_hint(word, guessed_words):
    if len(word) > 1 and word[1] not in guessed_words:
        return f"The second letter of the word is '{word[1].lower()}'."

# Word guessing popup for theme
def word_guessing_popup():
    theme_choice = select_theme()

    if not theme_choice:
        return

    word = choose_word(theme_choice).lower()
    attempts = 5
    guessed_words = []

    # Layout for word Guessing Game popup
    layout = [
        [psg.Text(f"Welcome to the Word Guessing Game! Theme: {theme_choice}", font=('Helvetica', 14))],
        [psg.Text("Guess the word in its entirety.", font=('Helvetica', 12))],
        [psg.Text("Attempts left:", font=('Helvetica', 12)), psg.Text(str(attempts), key="attempts", font=('Helvetica', 14))],
        [psg.Text("Guessed words:", font=('Helvetica', 12)), psg.Text("", key="guessed_words", font=('Helvetica', 14))],
        [psg.InputText("", size=(20, 1), key="guess", font=('Helvetica', 14), justification='center')],
        [psg.Button("Guess", font=('Helvetica', 14)), psg.Button("Exit", font=('Helvetica', 14))],
        [psg.Text("", key="result", font=('Helvetica', 14))],
        [psg.Text("", key="hint", font=('Helvetica', 12))],
    ]

    # Window for word guessing game
    window = psg.Window("Word Guessing Game", layout, finalize=True)

    # While player still has attempts
    while attempts > 0:
        window['attempts'].update(str(attempts))
        window['guessed_words'].update(", ".join(guessed_words))

        event, values = window.read()

        if event == psg.WIN_CLOSED or event == "Exit":
            break

        if event == "Guess":
            guess = values["guess"].lower()

            # If guess is not a word
            if len(guess) < 1 or not guess.isalpha():
                window['result'].update("Please enter a valid word.")
                continue

            # If player has already guessed a word
            if guess in guessed_words:
                window['result'].update(f"You already guessed the word '{guess}'!")
                continue

            guessed_words.append(guess)

            # If player guesses the word right
            if guess == word:
                window['result'].update(f"Congratulations! You guessed the word '{word}' correctly! You have won 10 coins!")
                window['hint'].update("")
                coins = wallet.get_coins()
                coins += 10
                wallet.save_coins(coins)
                break  
            else:
                # If player guesses a wrong word
                attempts -= 1
                window['result'].update(f"Oops! '{guess}' is not the word. Try again.")
                
                # Gives a hint when a word is wrong
                hint = provide_hint(word, guessed_words)
                window['hint'].update(hint)

            # If player runs out of attempts
            if attempts == 0:
                window['result'].update(f"Oh no! Looks like you could not guess the word. The word was '{word}'.")

            window['guess'].update('')

    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == "Exit":
            break

    window.close()

# Theme window picker layout
def select_theme():
    theme_layout = [
        [psg.Text("Select a theme for your Word Guessing Game:", font=('Helvetica', 14))],
        [psg.Button(theme, size=(20, 2)) for theme in Themes.keys()],
        [psg.Button("Cancel", size=(20, 2))],
    ]

    # Window for theme picker
    theme_window = psg.Window("Select Theme", theme_layout, finalize=True)

    event, values = theme_window.read()
    theme_window.close()

    if event == psg.WIN_CLOSED or event == "Cancel":
        return None

    return event

# Function to run game in GameEngine.py
def start_word_guessing_game():
    word_guessing_popup()


