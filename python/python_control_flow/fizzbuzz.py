"""
FIZZBUZZ
"""

# user_num = int(input("Please enter a number between 1 and 100: "))
# if (user_num % 2) == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

for user_num in range(1, 100):
    if user_num % 5 == 0 and user_num % 3 == 0:
        print("FizzBuzz")
    elif user_num % 5 == 0:
        print("Buzz")
    elif user_num % 3 == 0:
        print("Fizz")
    else:
        print(user_num)

user_num = 1
while user_num < 100:
    if user_num % 5 == 0 and user_num % 3 == 0:
        print("Fizzbuzz")
    elif user_num % 5 == 0:
        print("Buzz")
    elif user_num % 3 == 0:
        print("Fizz")
    else:
        print(user_num)
    user_num += 1
