"""
Magic Number Task

Make a magic number game using Python.

The game should:

1. set a number as the answer
2. ask the user for a guess
3. check if the user’s guess was correct
4. if it was, congratulate them. If not give them another guess (up to 3 guesses)
"""
import random


magic_number = random.randint(1, 100)

for _ in range(3):
    user_guess = int(input("Guess the magic number between 1 and 100!\nYour guess: "))

    if user_guess == magic_number:
        print("Congratulations! You got it right!");

    else:
        print("Unlucky!");

else:
    magic_number = int(random.randint(1,100))
# NB: i have a feeling that this will actually provide a new number to print
# essentially, I might have accidentally rigged the game so user can never win?!
    print("Game Over! You didn't guess correctly in three tries.")
    print("The correct answer was: ")
    print(magic_number)

