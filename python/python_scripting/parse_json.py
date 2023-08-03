"""PARSE JSON"""

# Parsing? turning a string into a data structure and vice versa

# import json
#
# json = json.loads(open('example.json').read()) # opens and reads json from a file, stores it in a variable
# value = json['name'] # input what key you want, from our example.json: name, ip etc
# print(value) # outputs Test, because that was the value paired with the 'name' key.
# print(type(json)) # <class 'dict'>. we have turned it into a python dictionary

# a more advanced example

import json
import os

# script to make an absolute path of the json file
script_dir = os.path.dirname(__file__) # gets the file location
print("The script is located at: " + script_dir)
script_absolute_path = os.path.join(script_dir, 'example.json') # adds the file to the end of the file location
print("The script absolute path is: " + script_absolute_path)

# Script to parse JSON

json = json.loads(open(script_absolute_path).read())
value = json["name"]
print(value)

#loop through the JSON
for key in json:
    value = json[key]
    print("The key and value are {} = {}".format(key, value)) # .format adds the specified variables into the space left in the posh brackets in the string.


