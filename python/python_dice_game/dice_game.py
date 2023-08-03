"""
---DICE GAME---
"""

"""
---PSEUDOCODE---

1. Ask user if they are ready to play
    a. if yes then go next
2. Ask for player name
3. Roll the dice for player
    a. print score
4. Roll the dice for CPU
    a. print the score
5. declare a winner
6. offer to play again
"""
import random # I import the random library so that I can use rng to simulate rolling dice.



# Welcome, are you ready to play?
user_start_choice = input("---WELCOME TO THE DICE GAME---\n---ARE YOU READY TO PLAY?---\nEnter yes or no: ")

if user_start_choice.lower() != "yes": # I use .lower here to make sure that the user input works regardless of case used (as long as it is yes)
    print("No worries, goodbye!")
    exit()


while True: # This is for the "play again" functionality
    # This is where I ask the user for their name and explain to the user how the game works
    username = input("Great, let's start then! First of all, tell me your name: ")
    print("\nHello " + username +", you're up against the CPU in this game. Here's how the game works:")
    print("When promoted, input 'roll'.\nThe game uses RNG to roll two dice, first for you, then for the CPU.\nIt then displays both scores and declares a winner.")

    while True: # This part starts an infinite while loop, where the only way to break out of it is for the user to input "roll" (case unsensitive). Otherwise it will just throw an error and ask again.
        user_roll_choice = input("Okay " + username + ", when you're ready, type 'roll' to start the game! ")
        if user_roll_choice.lower() == "roll": # again, .lower used here to make case unsensitive
            print("Here we go!\n")
            break
        else:
            print("Unknown response. Type 'roll' to start the game: ")

    while True: # If the previous condition has been met ie roll has been entered, then the game now rolls the dice.
        user_roll_1 = random.randint(1, 6)
        user_roll_2 = random.randint(1, 6)
        cpu_roll_1 = random.randint(1, 6)
        cpu_roll_2 = random.randint(1, 6)
    # I modified my game to have two dice per turn. To do this, I just made another variable for each player's second roll.

        user_total = user_roll_1 + user_roll_2
        cpu_total = cpu_roll_1 + cpu_roll_2
    # I added both rolls for each player together

        print(username + " rolled: ", user_total)
        print("CPU rolled:",cpu_total)
     # displaying both scores

        if user_total > cpu_total: # if player wins
            print(username + " wins! Congrats!")
            break
        elif user_total < cpu_total: # if cpu wins
            print("CPU wins. Unlucky!")
            break
        else: # only other option is a tie
            print("It's a tie!") # if it is a tie, then the code loops back to do a reroll of the dice. if not a tie, the loop breaks.

    play_again = input("---GAME OVER. PLAY AGAIN? ENTER yes OR no:--- ") # The whole programme is inside a while true loop that allows user to play again if they wish
    if play_again.lower() != "yes":
        print("---END OF GAME---")
        break

    print("---NEW GAME SELECTED---")






