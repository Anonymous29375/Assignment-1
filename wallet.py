import json
import os

WALLET_FILENAME = "wallet.json"

def reset():
    if os.path.isfile(WALLET_FILENAME):
        os.remove(WALLET_FILENAME)

    create_if_not_exist()


def create_if_not_exist() -> None:
    # Make sure wallet file exists
    try:
        with open(WALLET_FILENAME, "x") as file:
            file.write('{ "coins": 5, "unlocked_games": [] }')
    except FileExistsError:
        # Ignore if file already exists
        pass


def read_wallet() -> dict:
    with open(WALLET_FILENAME, "r") as file:
        wallet = json.load(file)
        return wallet


def get_coins() -> int:
    wallet = read_wallet()
    return int(wallet["coins"])


def save_coins(coins: int) -> None:
    wallet = read_wallet()
    with open(WALLET_FILENAME, "w") as file:
        wallet["coins"] = coins
        json.dump(wallet, file)


def adjust_coins(coins: int) -> int:
    total_coins = get_coins()
    total_coins += coins

    if total_coins < 0:
        total_coins = 0

    save_coins(total_coins)
    return total_coins


def is_game_unlocked(game: str) -> bool:
    wallet = read_wallet()
    return game in wallet["unlocked_games"]

def are_all_games_unlocked() -> bool:
    wallet = read_wallet()
    return 'Word Guessing Game' in wallet["unlocked_games"] and 'Hangman' in wallet["unlocked_games"]


def unlock_game(game: str) -> list:
    wallet = read_wallet()
    with open(WALLET_FILENAME, "w") as file:
        wallet["unlocked_games"].append(game)

        # Make sure all game names are distinct
        wallet["unlocked_games"] = list(set(wallet["unlocked_games"]))
        json.dump(wallet, file)
