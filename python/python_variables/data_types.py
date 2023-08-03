# Data Types

# Numbers -> Integers, Float (Decimal), Complex (imaginary and real)
# Strings -> Characters or text
# Booleans -> True or False

# Operators

# Arithmetic Operators
# + (addition), - (subtraction), / (division), * (multiplication), % (remainder)

# Comparison Operators
# > Greater than
# < Less than
# == Equal to
# != Not equal to
# >= Greater than or equal to
# <= Less than or equal to

# Numeric Types

# Every programming language uses integers in some way

# a = 24
# b = 16
#
# print(a + b)
# print (a / b)
# print (a < b)
#
# FloatNum = 1.356
# IntNum = 4
#
# print(type(FloatNum + IntNum))
# # Floats and Ints can be used together as they are both numeric
#
# one_third = 1 / 3
# print(one_third)
# print(one_third * 3)
# # Python rounds it up

# Strings

# can use either double or single quotes for strings

#String Slicing

# What it sounds like, slicing up a string

hi = "hello world!"
# H E L L O   W O R L D !
# 0 1 2 3 4 5 6 7 8 9 10 11

print(hi[0:5])
print(hi[-2]) #negative number goes back from the end, imagine if it was looped

# String Methods
# super crucial but repetitive tasks built into Python (others are downloadable)

#len()
print(len(hi))

# .strip()
white_space = "lots of white space                                     "
print(len(white_space))
print(len(white_space.strip()))

# .lower()
example_text = "Here's some text with lots of text"
print(example_text.lower())
#converts all alphabetical characters into lower text

# .upper()
# same as .lower but converts to UPPER CASE

# .count()
print (example_text.count("text"))
# count how many times this particular set of characters in this particular order occurs
# in exmaple_text, the word "text" appears twice, so returns 2.

# .replace()
# replace character in string with another
print(example_text.replace("with", ","))


# CONCATENATION & CASTING
# Adding multiple strings together

x = 2
y = 5.4
z = "this is a string"
zz = "this is also a string"

print (z + " " + zz)

# Cannot add numeric and string together

#CASTING
# converting numeric types to string
print(str(x) + " " + str(y) + " " + z)

# String to numeric casting

int_string = "6"

print(int(int_string))
print(float(int_string))
print(type(int(int_string)))
print(type(float(int_string)))

# F-Strings

name = "lassie"
years = 7
height_cm = 60.2
print (f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS!")

pi = 3.14159265359
print(f"Pi to e decimal places: {pi:.3f}")

# percentages
score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:.2%}")