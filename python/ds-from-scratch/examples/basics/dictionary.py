# Pythonic way to declare a dictionary
d1 = {}
d2 = {"a": 1, "b": 2, "c": 3}

# Read key. Cause exception if not found
try:
    d2["e"]
except KeyError as ke:
    print(f"Yup, e does not exist, hence exception {ke}")

# Read key. Specify default value if not found
print(f"Default value: {d2.get('e', 0)}")

# Check existence of key
print(f"Is f in d2? {'f' in d2}")

# Keys, values, items
print(f"Keys: {d2.keys()}")
print(f"Values: {d2.values()}")
print(f"Items: {d2.items()}")

# Dictionary keys must be hashable. Tuples can be keys, lists cannot
d2[(1, 2, 3)] = 9

print(f"{d2}")
