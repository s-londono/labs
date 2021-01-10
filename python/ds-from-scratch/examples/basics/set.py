# Build a set
s1 = set()
s2 = {1, 2, 3, 4, 5}

l1 = range(1, 5)
s3 = set(l1)

# Set lookup is very fast
print(f"Set has 1 {1 in s2}")

# Sets can be used to find dictinct elements in a collection
l2 = [1, 2, 3, 1, 3, 4, 6, 3, 2, 1, 6, 8]
s4 = set(l2)

print(f"Distinct in l2: {list(s4)}")
