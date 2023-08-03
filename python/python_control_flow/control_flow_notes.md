# Control Flow Notes

Control flow is a method of telling Python what to do in a certain order and with specific conditions.

This is done using conditional statements - mainly **If**, **Elif** and **Else**.

You ask Python to do something IF a condition is true. You then specify what it should do if the conditions are not that, or are different, with ELIF.
ELSE is then used as a catch-all, for when none of the specified conditions are met.

##### NB: There are no case or switch statements in Python.

#### Example of conditional statements:

```python
if age >= 18:
    print("You can watch any movie!")
elif age >= 15:
    print("Sorry, you cannot watch 18 rated movies, but you can watch all other movies.")
elif age >= 12:
    print("Sorry, you can only watch U, PG, or 12 rated movies.")
elif age >= 7:
    print("Sorry, you can only watch U and PG movies.")
else:
    print("You can only watch U rated movies")
```

## For and While Loops

For loops are used to iterate over a sequence.

```python
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"Name": "Bronson", "money": "$0.05"},
    2: {"Name": "Masha", "money": "$3.66"},
    3: {"Name": "Rosco", "money": "$1.14"}
}

for num in list_data:
    print(num * 2)
```
Loops can be nested.

```python
for data in embedded_lists:
    print(data)
    for num in data:
        print(num)

```

You can loop through dictionaries:

```python
for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)
```

You can use if statements within loops and this is where the powerful stuff begins.

```python
for num in list_data:
    if num == 3:
        print("You have found three!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon!")
```

### While Loops

While loops **monitor** a condition, they check if something is still the case.

```python
x = 0

# while x < 10:
#     print(f"it's working -> {x}")
#     x += 1

# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break # pause/stop on the while loop
#     x += 1
```

### Verifying User Input
```python
user_prompt = True

while user_prompt:
    age = input("Input your age: ")
    if age.isdigit() and int(age) < 120 and int(age) != 0:
        user_prompt = False
    else:
        print("Please enter a whole number between 1 and 120.")

print(f"your age is {age}.")
```
