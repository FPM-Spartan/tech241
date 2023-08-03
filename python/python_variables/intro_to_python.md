# h1

## h2

### h3

#### h4

##### h5

###### h6

# Intro to Python

three backticks in a row (the button beside 1) creates a codeblock 

Python is a dynamically typed language, so you do not have to state what type each variable is.

```python
a = 1
b = 2
c = 3.5
hi = "hello world!"
```
## variables in python
a way to store data within a program -> it becomes a reference to that data 
a variable can change

## how to set a variable

 a = 4 -> variable_name = variable_data
 
variables can be overwritten

variables can be overwritten with user input

## Data Types

### Operators

There are different categories of operators:

#### Arithmetic Operators:

* "+" (addition)
* "-" (subtraction)
* "/" (division)
* "*" (multiplication)
* "%"(remainder)

#### Comparison Operators

* ">" Greater than
* < Less than
* == Equal to
* != Not equal to
* ">=" Greater than or equal to
* <= Less than or equal to

### Numeric Data Types

Integers and Floats

Integers are whole numbers, Floats are decimal numbers.
They can be mixed together.

### Strings
Strings are characters wrapped in quote marks
You can slice strings:
```python
hi = "hello world!"
# H E L L O   W O R L D !
# 0 1 2 3 4 5 6 7 8 9 10 11

print(hi[0:5])
print(hi[-2]) #negative number goes back from the end, imagine if it was looped

```
You can use String Methods to do cool stuff with strings. EG:

* len displays length of a string
* .strip eliminates white space at the end of a string
* .upper and .lower convert alphabetical characters to upper and lower case respectively
* .count displays how many times a specific set of characters in a specific order occurs in the string (functionally, this is for finding words)
* .replace replaces a specific set of chars in a specific order with another.

## Concatenation and Casting
Concatenation is adding multiple strings together:
```python
x = 2
y = 5.4
z = "this is a string"
zz = "this is also a string"

print (z + " " + zz)
```
NB: Numeric data types and strings cannot be added together. This is where casting comes in.

### Casting

Casting is converting numeric data types to strings.
```python
x = 2
y = 5.4
z = "this is a string"
zz = "this is also a string"

print(str(x) + " " + str(y) + " " + z)
```

You can also change strings to numeric data types

```python
int_string = "6"

print(int(int_string))
print(float(int_string))
print(type(int(int_string)))
print(type(float(int_string)))

```

## F-Strings
Easier than casting, can combine multiple strings and perform methods on them at the same time.
```python
score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:.2%}")
```

## Booleans

**True** or **False** "(Remember to Capitalise)"

AND requires both to be true
OR requires one to be true

### Booleans with data types

```python
hi = "Hello world!"

# Boolean methods
print(hi.isalpha()) # False (spaces and punctuation are not alphabetical characters) (is it alphabetical)
print(hi.islower()) #False (lower case only = true)
print(hi.endswith("!")) #True (string ends with specified char)
print(hi.startswith("H")) # True (string starts with specified char)
```
0 always has a value of False
Any other number has a value of True

None is a Placeholder similar to Null in other languages.
It is not 0, it is not nothing. It is, however, Capitalised.
None is independent of True and False.

The best practice for checking if something is None is:
```python
x = None
print (x is None)
```
