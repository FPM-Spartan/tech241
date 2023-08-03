"""
Functions
"""

# code block that can be reused later in the program

# DRY

"""# creating a function"""

# def = define. Define the function and what it does. Make sure your name is descriptive.
# def print_something():
#     print("Something has been printed")
#
# print_something()
#
# def print_another(print_string):
#     print(print_string)
#
# print_another("This is a string")
# print_another("This is also a string")

"""# Greeting function"""

# def greeting(name):
#     print("Hello my name is " + name)
#
# greeting(input("Enter name: "))

"""# Return statement"""

# def addition(int1, int2):
#     return int1 + int2 # int1 + int2 has produced something, but we need to RETURN it, otherwise it doesn't get used.
#
#
# print(addition(2, 3))

"""Default arguments and parameters"""

# def addition(int1 = 2, int2 = 3): # you can set what each variable will equal as default
#     return int1 + int2 # int1 + int2 has produced something, but we need to RETURN it, otherwise it doesn't get used.
#
#
# print(addition())
# print(addition(10, 12)) # defaults can still be overridden

"""Multiple Arguments"""

def multi_args(*multibulti):
    print(type(multibulti))

    for arg in multibulti:
        print(arg)

multi_args(input("Input your args: "))

"""
FUNCTIONS BEST PRACTICES

Clear names, lower case, underscores
Arguments should be clear in their needs. Should be obvious.
Remember return! if you get None back, your code probably isn't returning a function somewhere.
Use comments to explain what a function is doing.
Consider type hints (optional, advanced)
"""