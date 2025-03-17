import FreeSimpleGUI as psg
import GameEngine
import wallet 

psg.theme('LightBlue7')



# Making the game popup layout
def create_game_layout(coins):
    layout = [
        [psg.Text("Games", font=('Bahnschrift Semibold Condensed', 25), justification='center', expand_x=True)],
        [psg.Image('GameImage.png', subsample=1)], 
        [psg.Text(f'You have {coins} coins', font=('Bahnschrift Semibold Condensed', 20), size=20, expand_x=True, justification='center')],
        [psg.Column([  
            [psg.Button("Number Guessing Game\n(Free)" if not wallet.is_game_unlocked("Number Guessing Game") else "Number Guessing Game\nUnlocked", size=(20, 2), key="Number Guessing Game")],
            [psg.Button("Word Guessing Game\nCost: 10" if not wallet.is_game_unlocked("Word Guessing Game") else "Word Guessing Game\nUnlocked", size=(20, 2), key="Word Guessing Game", disabled = coins < 10 and not wallet.is_game_unlocked("Word Guessing Game") )],
            [psg.Button("Hangman\nCost: 25" if not wallet.is_game_unlocked("Hangman") else "Hangman\nUnlocked", size=(20, 2), key="Hangman", disabled = coins < 25 and not wallet.is_game_unlocked("Hangman"))],
        ], justification='center')]
    ]
    return layout

def update_button_disabled():
    coins = wallet.get_coins()
    
    # Update button disabled state based on updated coins
    window['Word Guessing Game'].update(disabled=coins < 10)
    window['Hangman'].update(disabled=coins < 25)

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
        

coins = wallet.get_coins()

# Window for the game popup
window = psg.Window("Game Popup", create_game_layout(coins), finalize=True)

while True:
    event, values = window.read() 

    if event == psg.WIN_CLOSED:  
        break
    
    # If the Number Guessing Game Button is Pressed
    if event == "Number Guessing Game" or event == "Number Guessing Game\nUnlocked":
        GameEngine.number_guessing_game()
        update_button_disabled()

    # If the Word Guessing Game Button is Pressed    
    elif event == "Word Guessing Game" or event == "Word Guessing Game\nUnlocked":
        # If the game is not unlocked
        if not wallet.is_game_unlocked("Word Guessing Game"):
            response = custom_popup("Word Guessing Game costs 10 coins to unlock. Would you like to unlock this game?")
            if response == 'Yes':
                wallet.adjust_coins(-10)
                wallet.unlock_game("Word Guessing Game")
                psg.popup("You have unlocked the Word Guessing Game!")
                # Updates the game to say unlocked
                window["Word Guessing Game"].update("Word Guessing Game\nUnlocked")
        # If the game is unlocked
        else:
            GameEngine.word_guessing_game()
            update_button_disabled()  

    # If the Word Guessing Game Button is Pressed
    elif event == "Hangman" or event == "Hangman\nUnlocked":
        # If the game is not unlocked
        if not wallet.is_game_unlocked("Hangman"):  
            response = custom_popup("Hangman costs 25 coins to unlock. Would you like to unlock this game?")
            if response == 'Yes':
                wallet.adjust_coins(-25)
                wallet.unlock_game("Hangman")
                psg.popup("You have unlocked Hangman!")
                # Updates the game to say unlocked
                window["Hangman"].update("Hangman\nUnlocked")
         # If the game is unlocked
        else:
            GameEngine.hangman()  
            update_button_disabled()

window.close()
