"""
CONTROL FLOW
"""

# Like giving Python a recipe or an order to do things

# Done usually by conditional statements.

# CONDITIONAL STATEMENTS

# like asking a question and then making decisions based on the answers

# eg: if I am hungry, then go make a sandwich. If not, then go and watch tv instead.

# we need a goal to start using them, so lets go with automated ticket system age verification

age = int(input("Type your age: "))

# if age >= 18:       #colon needed so python understands the context for the next line. What i write next is going
# to be connected to the line above print("You can watch all movies!")      # indentation is needed for the line after
# conditional statement.

# if age < 18:
#     print("Sorry, you cannot watch 18 rated movies.")

# This works, but it is not the way to write control blocks.
# It is ugly, clunky, and if you have a lot, it can become hard to follow

if age >= 18:
    print("You can watch any movie!")
elif age >= 15:
    print("Sorry, you cannot watch 18 rated movies, but you can watch all other movies.")
elif age >= 12:
    print("Sorry, you can only watch U, PG, or 12 rated movies.")
elif age >= 7:
    print("Sorry, you can only watch U and PG movies.")
else: # Else is the catch-all statement. If you run through all of the above and do not meet any of the conditions, then else will apply.
    print("You can only watch U rated movies")

# There are no case or switch statements in Python
