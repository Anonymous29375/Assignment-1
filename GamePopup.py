import PySimpleGUI as psg
import GameEngine

psg.theme('LightBlue7')

# Track if a game is unlocked or not
unlocked_games = {
    "Number Guessing Game": True,
    "Word Guessing Game": False,
    "Hangman": False,
}

# Making the game popup layout
def create_game_layout():
    layout = [
        [psg.Text("Games", font=('Bahnschrift Semibold Condensed', 25), justification='center', expand_x=True)],
        [psg.Column([  
            [psg.Button("Number Guessing Game\n(Free)" if not unlocked_games["Number Guessing Game"] else "Number Guessing Game\nUnlocked", size=(20, 2), key="Number Guessing Game")],
            [psg.Button("Word Guessing Game\nCost: 10" if not unlocked_games["Word Guessing Game"] else "Word Guessing Game\nUnlocked", size=(20, 2), key="Word Guessing Game")],
            [psg.Button("Hangman\nCost: 55" if not unlocked_games["Hangman"] else "Hangman\nUnlocked", size=(20, 2), key="Hangman")],
        ], justification='center')]
    ]
    return layout

# Buttons for unlocking the games
def custom_popup(message, title="Game Unlock"):
    layout = [
        [psg.Text(message, font=('Helvetica', 12), justification='center')],
        [psg.Button("Yes", size=(20,1)), psg.Text('', size=(25, 1)), psg.Button("No", size=(20,1))]
    ]
    
    popup_window = psg.Window(title, layout, finalize=True, modal=True)

    while True:
        event, values = popup_window.read()
        if event == psg.WIN_CLOSED or event == "No":
            popup_window.close()
            return "No"
        elif event == "Yes":
            popup_window.close()
            return "Yes"

# Window for the game popup
window = psg.Window("Game Popup", create_game_layout(), finalize=True)

while True:
    event, values = window.read() 

    if event == psg.WIN_CLOSED:  
        break
    
    # If the Number Guessing Game Button is Pressed
    if event == "Number Guessing Game" or event == "Number Guessing Game\nUnlocked":
        GameEngine.number_guessing_game()
        
    # If the Word Guessing Game Button is Pressed    
    elif event == "Word Guessing Game" or event == "Word Guessing Game\nUnlocked":
        # If the game is not unlocked
        if not unlocked_games["Word Guessing Game"]:
            response = custom_popup("Word Guessing Game costs 10 coins to unlock. Would you like to unlock this game?")
            if response == 'Yes':
                unlocked_games["Word Guessing Game"] = True
                psg.popup("You have unlocked the Word Guessing Game!")
                # Updates the game to say unlocked
                window["Word Guessing Game"].update("Word Guessing Game\nUnlocked")
        # If the game is unlocked
        else:
            GameEngine.word_guessing_game()  

    # If the Word Guessing Game Button is Pressed
    elif event == "Hangman" or event == "Hangman\nUnlocked":
        # If the game is not unlocked
        if not unlocked_games["Hangman"]:  
            response = custom_popup("Hangman costs 55 coins to unlock. Would you like to unlock this game?")
            if response == 'Yes':
                unlocked_games["Hangman"] = True
                psg.popup("You have unlocked Hangman!")
                # Updates the game to say unlocked
                window["Hangman"].update("Hangman\nUnlocked")
         # If the game is unlocked
        else:
            GameEngine.hangman()  

window.close()
