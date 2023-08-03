"""
SCRIPTING BASICS
"""

# Libraries and Modules

# Modules are a collection of functions.
# A library is a collection of modules. Much bigger than a module.

"""SEVEN "CORE" modules in Python"""

import sys
# system

print(sys.version)

# import os
# # operating system (good for files and folders)
#
# print(os.getcwd()) # get current working directory
#
import subprocess
# # subprocess module lets this file work with other files
# runs an external file when executed
# subprocess.run(["python", "hello_world_test.py"]) # can specify directory if not in same directory

import math

pi = math.pi
pi_string = str(pi)
print("The Value of pi is " + pi_string)

import random

# for RNG

randnum = random.randrange(1, 10)

print(randnum)

"""VERY IMPORTANT ONE >>>"""
import datetime

whatisthedate = datetime.datetime.now()
print(whatisthedate)

import json

# json is a language used mainly for getting stuff from APIs and other languages/systems etc

x = {
    "name": "John",
    "city": "Glasgow",
    "age": 28
}

y = json.dumps(x)
print(type(x)) # dict
print(type(y)) # string

