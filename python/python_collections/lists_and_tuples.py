# lists and tuples

# lists are called arrays in most other programming languages.

# making a list in python

# shopping_list = ["eggs", "bacon", "bananas", "bread", "haggis"]
#
# print(type(shopping_list))
# print(shopping_list)
#
# # accessing certain parts of a list
#
# print(shopping_list[-1])
#
# # change a specific element of the list?
#
# shopping_list[4] = "orange juice"
# print(shopping_list)
#
# # list methods
#
# # add to the end of a list
# shopping_list.append("butter")
# print(shopping_list)
# print(shopping_list[5])
#
# # remove from list
#
# shopping_list.remove("butter")
# print(shopping_list)
#
# # pop
# # pop gets rid of the last item in the list if left blank, or will remove the index number if specified
#
# shopping_list.pop()
# print(shopping_list)
#
# shopping_list.pop(2)
# print(shopping_list)

# List can have mixed data types

mixture = [1, 2, 3.5, "one", "two", "three", "four"]
print(mixture)

# list slicing

print(mixture[1:3]) # number you start with is included, one you end with IS NOT
# output is [2, 3.5]

print(mixture[::3]) #[1, "one", "four"]

# tuples

# tuples are immutable, so they cannot be changed. They use () instead of []

essentials = ("bread", "eggs", "milk")
print(essentials)
print(essentials.count("bread")) #count how many times the string appears in the tuple

# essentials[0] = "beans" # DOES NOT WORK



