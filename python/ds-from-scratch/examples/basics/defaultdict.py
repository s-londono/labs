from collections import defaultdict

# When you try to lookup a key it doesn't contain, it first adds a value for it using a zero-argument function
# you provided upon creation (can be a custom function or even a lambda).
# Useful for collecting results by some key
d1 = defaultdict(list)
d2 = defaultdict(lambda: [0, 0])

for i in range(1, 50):
    if i % 2 == 0:
        d1["pair"].append(i)
    else:
        d1["impair"].append(i)

print(d1)

d2["n"][1] = 1
