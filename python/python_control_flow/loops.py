"""
Loops
"""

# For Loops and While Loops

# for and foreach in other languages
# in python we just use for

# list_data = [1, 2, 3, 4, 5]
# embedded_lists = [[1, 2, 3], [4, 5, 6]]
# dict_data = {
#     1: {"Name": "Bronson", "money": "$0.05"},
#     2: {"Name": "Masha", "money": "$3.66"},
#     3: {"Name": "Rosco", "money": "$1.14"}
# }
#
# for num in list_data:
#     print(num * 2)

# Nested loops

# a loop within a loop

# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

# looping through dictionaries

# for item in dict_data.values():
#     for embed_value in item.values():
#         print(embed_value)
print("\n")
# a loop that only returns the money

# for items in dict_data.values():
#     print(items["money"])

# loops and if statements

# this is where the really powerful stuff begins

# for num in list_data:
#     if num == 3:
#         print("You have found three!")
#     elif num > 3:
#         print("Gone too far!")
#     else:
#         print("Too soon!")

# While loops
# they monitor a condition. checks if something is still the case.

# x = 0
#
# # while x < 10:
# #     print(f"it's working -> {x}")
# #     x += 1
#
# # while x < 10:
# #     print(f"it's working -> {x}")
# #     if x == 4:
# #         break # pause/stop on the while loop
# #     x += 1

# Verifying User Input

user_prompt = True

while user_prompt:
    age = input("Input your age: ")
    if age.isdigit() and int(age) < 120 and int(age) != 0:
        user_prompt = False
    else:
        print("Please enter a whole number between 1 and 120.")

print(f"your age is {age}.")