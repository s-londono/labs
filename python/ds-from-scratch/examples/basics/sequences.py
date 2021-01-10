# Lists can hold heterogeneous data types
lheter1 = ["a", 1.3, [0, 1, 2]]

l1 = [1, 2, 3]

# Combine lists and create a new list with the result
l2 = l1 + [4, 5, 6]

# Append mutates the list by adding a single element at the end of the list
l2.append(0)

# Extend mutates the list by adding several elements
l2.extend([7, 8, 9])

# Remove an element by position
del(l2[5])

# Indexing and slicing
sel_last = l2[-1]
sel_3_to_end = l2[3:]
sel_last_5 = l2[-5:]
sel_first_3 = l2[:3]
sel_pairs = l2[::2]

# Invert a slice of last four
sel_inv_last_4 = l2[4::-1]

# Invert a list
l2_inv = l2[::-1]

# Clone a list
l2_clone = l2[:]

# Convert string to a list (by default, separator is space)
l3 = "a,b,c,d,e".split(",")

# Sum all elements in the list and get its length
sum1 = sum(l2)
len1 = len(l2)

# Check for list membership
has_2 = 2 in l2

# Unpack ilst
v1, v2, v3 = ["a", "b", "c"]

# Common idiom: use underscore for values to be thrown away
_, v4 = [1, 2]

# TUPLES: LISTS' IMMUTABLE COUSINS

tp1 = 1, 2, 3
tp2 = (4, 5, 6, 7)


# Use tuples to return multiple values from functions
def tp_returner(x, y):
    return (x + y), (x * y)


tp3, tp4 = tp_returner(4, 5)

# Multiple assignment
v5, v6 = (1, 3)


