import FreeSimpleGUI as psg
import subprocess
import wallet

psg.theme('LightBlue7')

# Create the wallet on disk if it does not already exist
wallet.create_if_not_exist()

# Layout of the main window
layout = [
    [psg.Text(text='Welcome to the Luck Shop!',
              font=('Bahnschrift Semibold Condensed', 25), size=20, expand_x=True, justification='center')],
    [psg.Image('LuckShop.png', expand_x=True, expand_y=True, subsample=4)],
    [psg.Button('The Shop', size=(20, 2)), psg.Text(text='', size=(20, 1)), psg.Button('Reset Wallet', size=(20, 2), key='Reset'), psg.Text(text='', size=(20, 1)), psg.Button('Games', size=(20, 2))],
]

window = psg.Window('Luck Shop', layout)

while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break

    # Different popup depending on the button pressed
    if event == 'The Shop':
        subprocess.Popen(['python', 'ShopEngine.py'])
    elif event == 'Reset':
        # Confirm reset layout
        layout_confirm_reset = [
                    [psg.Text("Reset your wallet?")],
                    [psg.Button('Confirm'), psg.Button('Cancel')]
                ]

        # Show confirm window
        confirm_window = psg.Window("Confirm Reset", layout_confirm_reset)
        confirm_event, confirm_values = confirm_window.read()
        confirm_window.close()
        if confirm_event == 'Confirm':
            wallet.reset()
    elif event == 'Games':
        subprocess.Popen(['python', 'GamePopup.py'])

window.close()

if __name__ == "__main__":
    pass
