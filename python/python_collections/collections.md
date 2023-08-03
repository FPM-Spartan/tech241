# Notes on Collections - Week 2 Tuesday

https://github.com/LSF970/basic_markdown_guide

## Lists and Tuples

Lists are how you can store a collection of data in a single variable.

```python
shopping_list = [
    "eggs", "bacon", "bananas", "bread", "haggis"
]
```
You can access specific parts of a list by using
```python
print(shopping_list[1])
```
Output: bacon

You can change parts of a list by specifying the index and then stating the change.
```python
shopping_list[4] = "orange juice"
# This changes haggis to orange juice in the list.
```

There are many different methods that can be applied to list for greater functionality.

* .append adds an item to the end of a list
* .remove removes an item from a list
* .pop gets rid of the last item in the list if the index is left blank, or removes a specific item if its index is specified.
* There are many many more methods, but these are some very useful common ones.

Lists can have mixed data types. Lists can also be sliced.

```python
mixture = [1, 2, 3.5, "one", "two", "three", "four"]
print(mixture[1:3]) # number you start with is included, one you end with IS NOT
# output is [2, 3.5]
```

### Tuples

Tuples are immutable lists, so the data within cannot be changed.
Tuples use () instead of []
```python
essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread")) #count how many times the string appears in the tuple

# essentials[0] = "beans" # DOES NOT WORK
```



## Dictionaries

Dictionaries are similar to lists and tuples, but are more complex.

They operate on **Key - Value pairs**

A **key** acts as the name or reference and has a 1-1 relationship with a value.

A value is the data stored for a key. It can be any data type, and can also be a list, set etc.

example dictionary:
```python
student_1 = {
    "name": "Peter",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "git", "data_types", "collections"]
}
```
You can access certain parts of a dictionary like this:
```python
print(student_1["stream"])
print(student_1["completed_lesson_names"][:3])
```
Change/remove a value like this:
```python
student_1["completed_lesson_names"] = 3
student_1["completed_lesson_names"].remove("data_types")
```

There are also methods for dictionaries:
```python
print(student_1.keys())
print(student_1.values())

```



## Sets

Sets are unordered lists, essentially. They also use posh brackets {}
```python
car_parts = {"wheels", "windows", "exhaust", "steering wheel"}
```

Again, you can add to and remove from a set.

```python
# add to a set

car_parts.add("doors")
print(car_parts)

# remove from a set

car_parts.remove("doors")
print(car_parts)

```

### Frozen Sets

These are sets that are immutable, so the data within cannot be changed.

*an unordered set of data that cannot be changed? Sounds like that would be very niche in its use cases!*
Yup, absolutely. Still cool though!

```python
x = frozenset(["jungle", "dubstep", "house", "garage"])
print(x)
```

##### End