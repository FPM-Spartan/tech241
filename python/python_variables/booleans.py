# Booleans

# a = True
# b = False
#
# # ALWAYS capitalise Booleans
#
# print(a == b) # False
# print(a!= b) # True
# print(a >= True) # True
# print(b <= False) # True
#
# print(True and False) # False (must be both)
# print(True or False) # True (must be one of them)

# Booleans with data types

hi = "Hello world!"

# Boolean methods
print(hi.isalpha()) # False (spaces and punctuation are not alphabetical characters) (is it alphabetical)
print(hi.islower()) # False (lower case only = true)
print(hi.endswith("!")) # True (string ends with specified char)
print(hi.startswith("H")) # True (string starts with specified char)

# The value of 0

x = 0
y = -10
print(bool(x))
print(bool(y))

# 0 is always false, any other number is true

# Value of None

# Not 0, not nothing --> It is a PLACEHOLDER

x = None
# None is capitalised

print(bool(None))
print(x == False)
print (x == True)

# None is independent of True or False

print(x == None) # This is not best practice

# Best practice for checking if something is None
print (x is None) # doesn't introduce booleans this way, and so doesnt risk complexities

