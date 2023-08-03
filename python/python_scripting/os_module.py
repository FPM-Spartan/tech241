"""
---OS MODULE---
"""

# Using OS to do fun (citation needed) things!!!!!

import os

# os.system('echo "Hello World!"')
# # use os to echo to the terminal

#Use OS to make and change directories

# create directory
# dir name
directory = "test_dir"
# parent dir name
parent_dir = "C:/Users/Pete/"
# don't need to declare variables, can just throw the strings into the below line. But it is good practice.
# path
path = os.path.join(parent_dir, directory)
# # create dir
# os.mkdir(path)

"""Putting a new file in the new directory"""

filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    toFile = "Contents of file is written here"
    file1.write(toFile)

print("File " + filename + " created in" + directory + " folder")
