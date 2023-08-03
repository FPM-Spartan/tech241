# Luke's JSON validity checker!

import os
import sys
import json

# How to check JSON is valid
if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is VALID!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: py check_json.py <file>")