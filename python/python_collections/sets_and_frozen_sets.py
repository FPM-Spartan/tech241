# Sets and Frozen Sets

# {} - list but unordered

car_parts = {"wheels", "windows", "exhaust", "steering wheel"}
print(car_parts)

# add to a set

car_parts.add("doors")
print(car_parts)

# remove from a set

car_parts.remove("doors")
print(car_parts)

# Frozen sets

# frozen sets are immutable sets, you cannot add and remove from them
# very niche. Unordered group of items that cannot be changed

x = frozenset(["jungle", "dubstep", "house", "garage"])
print(x)