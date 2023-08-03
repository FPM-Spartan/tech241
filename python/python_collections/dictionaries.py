# Dictionaries

# Key - Value pairs

# Key is the name/reference, Value is the data stored

# MAKING a dictionary

student_1 = {
    "name": "Peter",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "git", "data_types", "collections"]
}

print(student_1)
print(type(student_1))

# How to access parts of a dictionary

print(student_1["stream"])
print(student_1["completed_lesson_names"][:3])

# changing a value

# student_1["completed_lesson_names"] = 3
# print(student_1["completed_lesson_names"])

# student_1["completed_lesson_names"].remove("data_types")
# print(student_1["completed_lesson_names"])

# Dictionary Methods

print(student_1.keys())
print(student_1.values())

