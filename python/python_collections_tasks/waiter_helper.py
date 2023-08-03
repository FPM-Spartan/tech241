# help a waiter with the menu

# defining lists for each course
starters = ["bruscetta", "soup of the day", "fresh mussels", "garlic mushrooms", "olives"]

mains = ["moroccan chicken", "sunday roast", "all day breakfast", "steak pie", "sloppy steaks"]
# Note: watch "I Think You Should Leave with Tim Robinson" on Netflix if you don't know what a sloppy steak is...

desserts = ["ice cream", "apple crumble", "trifle", "tiramisu", "cheese board"]

#printing menu for customer

print("---MENU---")
print("\n")

print("Today's starters are: ")
print(*starters, sep = "\n")
print("\n")

print("Today's main courses are: ")
print(*mains, sep = "\n")
print("\n")

print("Today's desserts are: ")
print(*desserts, sep = "\n")
print(("\n"))

# asking for customer order for each course


starter_choice = input("What would you like for your starter? \nEnter choice: ")

if starter_choice in starters:
    print("For starters, you have ordered: " + starter_choice);

elif starter_choice not in starters:
    print("Unknown starter choice.");
    input("Please select only from the menu (case sensitive): ");

mains_choice = input("What would you like for your main course? \nEnter choice: ")

if mains_choice in mains:
    print("For main course, you have ordered: " + mains_choice);

elif mains_choice not in mains:
    print("Unknown main course choice.");
    input("Please select only from the menu (case sensitive): ");

dessert_choice = input("What would you like for your dessert? \nEnter choice: ")

if dessert_choice in desserts:
    print("For dessert, you have ordered: " + dessert_choice);

elif dessert_choice not in desserts:
    print("Unknown dessert choice.");
    input("Please select only from the menu (case sensitive): ");

print("\n")


# Order Summary:

print("Order Summary:\n")
print("You have ordered: " + starter_choice + ", " + mains_choice + ", and " + dessert_choice + ".")
print("Thank you for your order. Your food will arrive shortly.")






# I would appreciate feedback on if this is good practice for specifying output formatting!
# Would also appreciate feedback on the control flow aspect:
# if input does not match what is in the list, it will give the error message I have coded, but only once, and then move onto the next one.
