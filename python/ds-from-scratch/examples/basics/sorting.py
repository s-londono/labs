l1 = [5, 32, 11, 10, 2, 7, 9, 0, 1, 9]

# Method sort does mutate the collection (sorts in place)
l2 = l1.sort()
print(f"List after sorting: {l1} vs {l2}")

l3 = [5, 32, 11, 10, 2, 7, 9, 0, 1, 9]

# Function sorted does not mutate the collection
l4 = sorted(l3)
print(f"List after sorting: {l3} vs {l4}")

# Reverse order
l5 = sorted(l3, reverse=True)
l1.sort(reverse=True)
print(f"List in reverse order: {l5} and {l1}")

# Order based on the result of a function
l6 = sorted(l3, key=lambda e: -e)
print(f"List sorted based on key: {l6}")
