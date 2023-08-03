"""
POKEMON GAME
"""

from random import randint
import json
import requests


def attack():
    roll_to_attack = randint(0, 3)
    return roll_to_attack


def defend():
    roll_to_defend = randint(0, 3)
    return roll_to_defend


def fetch_pokemon_data():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100")
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print("Failed to fetch Pokemon data from the API.")
        return []


def display_available_pokemon(pokemon_data):
    print("Available Pokemon:")
    for index, pokemon in enumerate(pokemon_data):
        print(f"{index + 1}. {pokemon['name'].capitalize()}")


def get_pokemon_details(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "health": data["stats"][0]["base_stat"],
            "damage": data["stats"][1]["base_stat"],
        }
    else:
        print(f"Failed to fetch details for {pokemon_name.capitalize()} from the API.")
        return None


while True:
    # Game setup
    pokemon_data = fetch_pokemon_data()
    display_available_pokemon(pokemon_data)

    player1_selection = input("\nPlayer1: Select a Pokemon (enter the number): ")
    player1_pokemon = get_pokemon_details(pokemon_data[int(player1_selection) - 1]["name"])

    player2_selection = input("\nPlayer2: Select a Pokemon (enter the number): ")
    player2_pokemon = get_pokemon_details(pokemon_data[int(player2_selection) - 1]["name"])

    if player1_pokemon is None or player2_pokemon is None:
        # Handle the case when fetching Pokemon details fails
        print("Failed to set up the game. Please try again.")
        continue

    player1_role = player1_pokemon["name"]
    player2_role = player2_pokemon["name"]

    player1_hp = player1_pokemon["health"]
    player2_hp = player2_pokemon["health"]

    game_on = True

    while game_on:
        print(f"\nplayer1 current health: {player1_hp}")
        print(f"player2 current health: {player2_hp}\n")

        # player1 Turn
        if player1_hp <= 0:
            print("Game over! Player2 wins")
            game_on = False
        else:
            print(f"Player1 Attack Turn")
            attack_roll = attack()
            print(f"Your roll: {attack_roll}")

            defend_roll = defend()
            print(f"Player2's roll: {defend_roll}")

            if attack_roll > defend_roll:
                damage = (attack_roll - defend_roll) + player1_pokemon['damage']
                player2_hp -= damage
                print(f"{damage} damage inflicted! Player2's health point: {player2_hp}")
            elif attack_roll == defend_roll:
                print("No damage!")
            else:
                player1_hp -= 1
                print(f"1 damage taken, your health point: {player1_hp}")

        # Player2 Turn
        if player2_hp <= 0:
            print("Game over! Player1 wins")
            game_on = False
        else:
            print(f"\nPlayer2 Attack Turn")
            attack_roll = attack()
            print(f"Your roll: {attack_roll}")

            defend_roll = defend()
            print(f"Player1's roll: {defend_roll}")

            if attack_roll > defend_roll:
                damage = (attack_roll - defend_roll) + player2_pokemon['damage']
                player1_hp -= damage
                print(f"{damage} damage inflicted! Player1's health point: {player1_hp}")
            elif attack_roll == defend_roll:
                print("No damage!")
            else:
                player2_hp -= 1
                print(f"1 Damage taken, your health point: {player2_hp}")

    next_game = input("\nWould you like to play again? (yes/no): ")
    if next_game == "yes":
        game_on = True
        continue
    else:
        break