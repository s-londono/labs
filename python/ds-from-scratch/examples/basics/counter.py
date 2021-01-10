from collections import Counter

# Turns a sequence of values into a defaultdict(int)-like object mapping keys to counts
# Gives a very simple way to solve word_counts problem
document = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
word_counts = Counter(document)
print(f"Word counts: {word_counts}")

# Count the elements of a string
c1 = Counter("abcdeabcdabcaba")

# Count of letter a
c1_count_a = c1["a"]

# The three most common letters
c1.most_common(3)

# List all unique elements
c1_unique = sorted(c1)

# List all elements with repetitions
c1_s_rpt = "".join(sorted(c1.elements()))

# Sum of all counts
c1_sum_counts = sum(c1)

# Update individual counts
for e in "reikjavik":
    c1[e] += 1

# Clear counts for an element (There c1["b"] == 0 afterwards)
del c1["b"]

# Join counters (update a counter by adding counts from another one)
c2 = Counter("stockolm")
c1.update(c2)

# Empty the counter
c1.clear()

# Note: If a count is set to zero or reduced to zero, it will remain in the counter until
# the entry is deleted or the counter is cleared. After the second line, 'b' is still in, but its count is zero
c3 = Counter("aaabbc")
c3["b"] -= 2
