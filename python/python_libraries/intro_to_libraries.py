"""
Intro to Python Libraries
"""

# Libraries are collections of pre-built pieces of code, made by someone else
# This is basically synth presets/VSTs but for Python code
# We can import these libraries to make our own code easier to understand, be less complex, and faster to write

# EG: import random

# use  import  to get access to a library in a python file.

# import random # this lights up when used. Useful so you can get rid of libraries you aren't using, for speed and efficiency

# import random as r

# print(random.randint(1, 100))

# from random import randint as rint # good for speed, and don't have to specify the library you want to use a thing from

# use comma to import multiple items from a library, or multiple libraries


from random import randint, random
import math

print(random())

num_float = 23.66

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)