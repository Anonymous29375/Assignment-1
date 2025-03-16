import FreeSimpleGUI as psg
import random

psg.theme('LightBlue7')

# Get the outcome for each box
def outcome_for_luck_box():
    return random.choice(["Gain 10 coins", "Lose 7 coins"])

def outcome_for_take_a_chance_box():
    return random.choice(["Gain 15 coins", "Gain 20 coins", "Lose 20 coins"])

def outcome_for_extreme_luck_box():
    return random.choice(["Win 50 coins", "Unlock a free game"])

def outcome_for_temporary_box():
    return "Gain an extra 10 coins if you win your next game"

# Making layout for the shop
layout = [
    [psg.Text('Welcome to the shop!', font=('Bahnschrift Semibold Condensed', 25), size=20, expand_x=True, justification='center')],
    [psg.Image('StoreImage.png', expand_x=True, expand_y=True)],
    [psg.Text('')],
    [
        psg.Button('Luck Box\nCost: 5 coins', size=(15, 2)), psg.Text(text='', size=(5, 1)),
        psg.Button('Take A Chance Box\nCost: 7 coins', size=(15, 2)), psg.Text(text='', size=(5, 1)),
        psg.Button('Extreme Luck Box\nCost: 50 coins', size=(15, 2)), psg.Text(text='', size=(5, 1)),
        psg.Button('Temporary Box\nCost: 25 coins', size=(15, 2))
    ],
]

# Making window for the shop
window = psg.Window("Shop", layout)

while True:
    event, values = window.read()

    if event == psg.WIN_CLOSED:
        break

    # If the Luck Box Button is Pressed
    if event == 'Luck Box\nCost: 5 coins':
        outcome = outcome_for_luck_box()

        # Window for confirmation of the purchase
        layout_confirm = [
            [psg.Text("Outcomes: Gain 10 coins or lose 7 coins.")],
            [psg.Image('LuckBox.png', subsample=4)],
            [psg.Text("Please confirm your purchase.")],
            [psg.Button('Confirm'), psg.Button('Cancel')]
        ]

        confirm_window = psg.Window("Confirm Purchase", layout_confirm)

        confirm_event, confirm_values = confirm_window.read()
        confirm_window.close()

        if confirm_event == 'Confirm':
            psg.popup(f"You bought the Luck Box!\nOutcome: {outcome}", title="Purchase Confirmed", button_color=('black', 'lightblue'))
        else:
            psg.popup("Purchase canceled!", title="Purchase Canceled", button_color=('black', 'darkblue'))

    # If the Take a Chance Box Button is Pressed
    elif event == 'Take A Chance Box\nCost: 7 coins':
        outcome = outcome_for_take_a_chance_box()

        # Window for confirmation of the purchase
        layout_confirm = [
            [psg.Text("Outcomes: Gain 15 coins, Gain 20 coins, or lose 20 coins.")],
            [psg.Image('LuckBox.png', subsample=4)],  
            [psg.Text("Please confirm your purchase.")],
            [psg.Button('Confirm'), psg.Button('Cancel')]
        ]

        confirm_window = psg.Window("Confirm Purchase", layout_confirm)

        confirm_event, confirm_values = confirm_window.read()
        confirm_window.close()

        if confirm_event == 'Confirm':
            psg.popup(f"You bought the Take A Chance Box!\nOutcome: {outcome}", title="Purchase Confirmed", button_color=('black', 'lightblue'))
        else:
            psg.popup("Purchase canceled!", title="Purchase Canceled", button_color=('black', 'lightblue'))
    
    # If the Extreme Luck Box Button is Pressed
    elif event == 'Extreme Luck Box\nCost: 50 coins':
        outcome = outcome_for_extreme_luck_box()

        # Window for confirmation of the purchase
        layout_confirm = [
            [psg.Text("Outcomes: Win 50 coins, Win 50 coins, or unlock a free game.")],
            [psg.Image('LuckBox.png', subsample=4)],  
            [psg.Text("Please confirm your purchase.")],
            [psg.Button('Confirm'), psg.Button('Cancel')]
        ]

        confirm_window = psg.Window("Confirm Purchase", layout_confirm)

        confirm_event, confirm_values = confirm_window.read()
        confirm_window.close()

        if confirm_event == 'Confirm':
            psg.popup(f"You bought the Extreme Luck Box!\nOutcome: {outcome}", title="Purchase Confirmed", button_color=('black', 'lightblue'))
        else:
            psg.popup("Purchase canceled!", title="Purchase Canceled", button_color=('black', 'lightblue'))

    # If the Temporary Box Button is Pressed
    elif event == 'Temporary Box\nCost: 25 coins':
        outcome = outcome_for_temporary_box()

        # Window for confirmation of the purchase
        layout_confirm = [
            [psg.Text("Outcomes: Gain an extra 10 coins if you win your next game.")],
            [psg.Image('LuckBox.png', subsample=4)],  
            [psg.Text("Please confirm your purchase.")],
            [psg.Button('Confirm'), psg.Button('Cancel')]
        ]

        confirm_window = psg.Window("Confirm Purchase", layout_confirm)

        confirm_event, confirm_values = confirm_window.read()
        confirm_window.close()

        if confirm_event == 'Confirm':
            psg.popup(f"You bought the Temporary Box!\nOutcome: {outcome}", title="Purchase Confirmed", button_color=('black', 'lightblue'))
        else:
            psg.popup("Purchase canceled!", title="Purchase Canceled", button_color=('black', 'lightblue'))

window.close()
