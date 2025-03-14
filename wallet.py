import json

WALLET_FILENAME = 'wallet.json'

def create_if_not_exist() -> None:
    # Make sure wallet file exists
    try:
        with open(WALLET_FILENAME, 'x') as file:
            file.write('{ "money": 5 }')
    except FileExistsError:
        # Ignore if file already exists
        pass

def get_money() -> float:
    with open(WALLET_FILENAME, 'r') as file:
        data = json.load(file)
        return float(data['money'])
    
def save_money(money: float) -> None:
    with open(WALLET_FILENAME, 'w') as file:
        wallet_data = {}
        wallet_data['money'] = money
        json.dump(wallet_data, file)