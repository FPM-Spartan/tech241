"""
POKEMON GAME
"""

from random import randint
import json
import requests





role_class = {"warrior": {"health": 25,
                          "damage": 1},
              "healer": {"health": 20,
                         "damage": 2},
              "mage": {"health": 15,
                       "damage": 4},
              "ranged": {"health": 17,
                         "damage": 3},
              "hunter": {"health": 17,
                         "damage": 3}}


def attack():
    roll_to_attack = randint(0, 3)
    return roll_to_attack


def defend():
    roll_to_defend = randint(0, 3)
    return roll_to_defend


while True:
    # Game set up
    player1_role = input("""Player1: select a character
    warrior
    healer
    mage
    ranged
    hunter: """)
    print(f"Player1: {player1_role}")

    player2_role = input("""\nPlayer2: select a character
    warrior
    healer
    mage
    ranged
    hunter: """)
    print(f"Player2: {player2_role}\n")

    # players selection
    if player1_role in role_class.keys():
        player1 = player1_role

    if player2_role in role_class.keys():
        player2 = player2_role

    player1_hp = role_class[player1_role]["health"]
    player2_hp = role_class[player2_role]["health"]

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
                damage = (attack_roll - defend_roll) + (role_class[player1_role]['damage'])
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
                damage = (attack_roll - defend_roll) + (role_class[player2_role]['damage'])
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