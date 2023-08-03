"""
Control Flow Task 3 - Loops and lists Task
"""

hello_count = 0

# for hello_count in range(0, 10):
#     if hello_count <= 10:
#         print("Hiya!")
#     else:
#         break
#
# list_names = []
#
# for i in range(10):
#     name = input("Enter a name: ")
#     list_names.append(name)
# print("List of names", list_names)
#
# list_names_lower =[]
#
# for name in list_names:
#     lower_case_name = name.lower()
#     list_names_lower.append(lower_case_name)
#
# print("Original List of names: ", list_names)
# print("Lower case list of names", list_names_lower)


num_list = list(range(1,101))

evens =[]

for num in num_list:
    if num % 2 == 0:
        evens.append(num)

print("Evens: ", evens)