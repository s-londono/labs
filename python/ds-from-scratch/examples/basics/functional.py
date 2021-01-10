
# Functions partial, map, reduce and filter are best avoided. Whenever possible, replace them with more Pythonic
# ways such as comprehensions, for loops etc.

# Zip and argument unpacking.

# Zip: stick two or more iterables together into a single iterable of tuples. Zip is lazy
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

zip_l1_l2 = [z for z in zip(list_1, list_2)]

# If the zipped lists are of different lengths, stops as soon as the first list ends
list_3 = ["j", "k", "l"]
zip_l1_l3 = [y for y in zip(list_1, list_3)]

# Unzip a list of tuples using the 'argument unpacking' trick
# Argument unpacking here is equivalent to: zip(('a', 1), ('b', 2), ('c', 3))
numbers, letters = zip(*zip_l1_l2)


def add(a, b):
    return a + b


# Argument unpacking
res = add(*[1, 2])



