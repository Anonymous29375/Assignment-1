import FreeSimpleGUI as psg
import random
import wallet

psg.theme('LightBlue7')

coins = wallet.get_coins()

# Get the outcome for each box
def outcome_for_luck_box():
    choice = random.choice(["Gain 10 coins", "Lose 7 coins"])

    if choice == "Gain 10 coins":
        wallet.adjust_coins(10)
    else:
        wallet.adjust_coins(-7)

    return choice

def outcome_for_take_a_chance_box():
    choice = random.choice(["Gain 15 coins", "Gain 20 coins", "Lose 20 coins"])

    if choice == "Gain 15 coins":
        wallet.adjust_coins(15)
    elif choice == "Gain 20 coins":
        wallet.adjust_coins(20)
    else:
        wallet.adjust_coins(-20)

    return choice

def outcome_for_extreme_luck_box():
    choice = random.choice(["Win 50 coins", "Unlock a free game"])

    if choice == "Win 50 coins":
        wallet.adjust_coins(50)
    else:
        wallet.adjust_coins(0)

    return choice

def outcome_for_temporary_box():
    return "Gain an extra 10 coins if you win your next game"

# Making layout for the shop
layout = [
    [psg.Text('Welcome to the shop!', font=('Bahnschrift Semibold Condensed', 25), size=20, expand_x=True, justification='center')],
    [psg.Image('StoreImage.png', expand_x=True, expand_y=True)],
    [psg.Text(f'You have {coins} coins', font=('Bahnschrift Semibold Condensed', 20), size=20, expand_x=True, justification='center', key="available_coins")],
    [
        psg.Button('Luck Box\nCost: 5 coins\nYou need 13 coins to buy', key='luck_box', size=(20, 3), disabled = coins < 13), psg.Text(text='', size=(5, 1)),
        psg.Button('Take A Chance Box\nCost: 7 coins\nYou need 27 coins to buy', size=(20, 3), key='take_a_chance', disabled = coins < 27), psg.Text(text='', size=(5, 1)),
        psg.Button('Extreme Luck Box\nCost: 25 coins\nYou need 25 coins to buy', size=(20, 3), key = 'extreme_luck', disabled = coins < 25), psg.Text(text='', size=(5, 1)),
        psg.Button('Temporary Box\nCost: 15 coins\nYou need 15 coins to buy', size=(20, 3), key = 'temporary_box', disabled = coins < 15)
    ],
]

# Making window for the shop
window = psg.Window("Shop", layout)

while True:
    event, values = window.read()

    if event == psg.WIN_CLOSED:
        break

    # If the Luck Box Button is Pressed
    if event == 'luck_box':
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
            coins = wallet.adjust_coins(-5)
            window['available_coins'].update(f'You have {coins} coins')

    # If the Take a Chance Box Button is Pressed
    elif event == 'take_a_chance':
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
            coins = wallet.adjust_coins(-7)
            window['available_coins'].update(f'You have {coins} coins')
    
    # If the Extreme Luck Box Button is Pressed
    elif event == 'extreme_luck':
        outcome = outcome_for_extreme_luck_box()

        # Window for confirmation of the purchase
        layout_confirm = [
            [psg.Text("Outcomes: Win 50 coins, or unlock a free game.")],
            [psg.Image('LuckBox.png', subsample=4)],  
            [psg.Text("Please confirm your purchase.")],
            [psg.Button('Confirm'), psg.Button('Cancel')]
        ]

        confirm_window = psg.Window("Confirm Purchase", layout_confirm)

        confirm_event, confirm_values = confirm_window.read()
        confirm_window.close()

        if confirm_event == 'Confirm':
            psg.popup(f"You bought the Extreme Luck Box!\nOutcome: {outcome}", title="Purchase Confirmed", button_color=('black', 'lightblue'))
            coins = wallet.adjust_coins(-25)
            window['available_coins'].update(f'You have {coins} coins')

    # If the Temporary Box Button is Pressed
    elif event == 'temporary_box':
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
            coins = wallet.adjust_coins(-15)
            window['available_coins'].update(f'You have {coins} coins')

window.close()