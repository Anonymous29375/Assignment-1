import PySimpleGUI as psg
import subprocess
import wallet

psg.theme('LightBlue7')

# Create the wallet on disk if it does not already exist
wallet.create_if_not_exist()

money = wallet.get_money()
print(money)

money += 20
wallet.save_money(money)
money = wallet.get_money()
print(money)


# Layout of the main window
layout = [
    [psg.Text(text='Welcome to the Luck Shop!',
              font=('Bahnschrift Semibold Condensed', 25), size=20, expand_x=True, justification='center')],
    [psg.Image('LuckShop.png', expand_x=True, expand_y=True, subsample=4)],
    [psg.Button('The Shop', size=(20, 2)), psg.Text(text='', size=(45, 1)), psg.Button('Games', size=(20, 2))],
]

# Making the main window
window = psg.Window('Luck Shop', layout)

while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break

    # Different popup depending on the button pressed
    if event == 'The Shop':
        subprocess.Popen(['python', 'ShopEngine.py'])
    elif event == 'Games':
        subprocess.Popen(['python', 'GamePopup.py'])

window.close()

if __name__ == "__main__":
    pass
