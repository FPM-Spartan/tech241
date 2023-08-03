"""
Age verification
"""
user_prompt = True

while user_prompt:
    age = input("Input your age: ")
    if age.isdigit() and 120 > int(age) >= 18:
        print("You can watch any movie!")
        user_prompt = False
    elif age.isdigit() and 18 > int(age) >= 15:
        print("Sorry, you cannot watch 18 rated movies, but you can watch all other movies.")
        user_prompt = False
    elif age.isdigit() and 15 > int(age) >= 12:
        print("Sorry, you can only watch U, PG, or 12 rated movies.")
        user_prompt = False
    elif age.isdigit() and 12 > int(age) >= 7:
        print("Sorry, you can only watch U and PG movies.")
        user_prompt = False
    elif age.isdigit() and 7 > int(age) >= 3:
        print("You can only watch U rated movies")
        user_prompt = False
    elif age.isdigit() and 3 > int(age) >= 1:
        print("Sorry, you cannot watch any movies; You are a baby.")
        user_prompt = False
    else:
        print("Please enter a whole number between 1 and 120.")

print(f"your age is {age}.")


