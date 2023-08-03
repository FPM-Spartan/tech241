# if I were a Millionaire I would buy...

# define a list
wishlist = ["big house", "big kitchen", "vintage guitar", "workshop", "big tv", "drum kit"]

# print list and check type
print(wishlist)
print(type(wishlist))

# print 1st element
print(wishlist[0])

# print second element
print(wishlist[1])

# print last item with negative index
print(wishlist[-1])

# replace first item
wishlist[0] = "modest house"
print(wishlist)

# replace another item
wishlist[3] = "hot tub"
print(wishlist)

# add an item
wishlist.append("rare vinyls")
print(wishlist)

# remove an item
wishlist.remove("big tv")
print(wishlist)

# remove last item without specifying
wishlist.pop()
print(wishlist)
