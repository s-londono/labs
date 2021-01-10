# GENERATORS
# Use when you just need to iterate over a collection with for and in, but never to access elements by an index.
# Helps when storing all the elements of the collection would be expensive and wasteful.
# Iterators can be iterated over just like lists, but generate their values lazily on demand
# E.g. the range function is a generator

# Flip-side of laziness: you can iterate through a generator only once.
# To iterate again, it's necessary to re-create the iterator

# 1st way to create generators: Function with the yield keyword

def abc_gen():
    s_ltrs = "abcdefghijklmnopqrstuvwxyz"
    i = 0

    while i < len(s_ltrs):
        print(f"Iteration #{i}")
        yield s_ltrs[i]
        i += 1


# Ivoking the function just creates an instance of the generator
print(f"Generator: {abc_gen()}")

# Note that the while loop in the generator function only iterates until the break hits (5 times),
# otherwise it runs until exhausting the while loop
for ix, ltr in enumerate(abc_gen()):
    print(f"Letter: {ltr}")

    if ix > 4:
        break

# 2nd way to create generators: Use comprehensions wrapped in parentheses

# Generator comprehensions do not do any work until you iterate over them
evens_below_20 = (i for i in range(20) if i % 2 == 0)

# Pythonic way to draw a generator and enumerate its values
for ix, ev in enumerate(evens_below_20):
    print(f"Index: {ix}. Event: {ev}")

