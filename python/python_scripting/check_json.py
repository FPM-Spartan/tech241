# check json

import os
import sys
import json

# how to check json is valid
if len(sys.argv) > 1: # in the terminal, how many arguments are there? If when the file is run in the terminal, if they give me more than one argument, do something.
    if os.path.exists(sys.argv[1]): # check to see if it is actually a file or not, does it exist. 1 is in square brackets because that's how you access brackets inside a list.
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is VALID!")
    else:
         print(sys.argv[1] + " not found.")
else:
    print("Usage: check_json.py <file>")