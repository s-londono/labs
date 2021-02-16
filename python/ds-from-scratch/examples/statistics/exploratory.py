from collections import Counter
import matplotlib.pyplot as plt
import random

num_friends = [round(random.gauss(50, 20)) for _ in range(5000)]

# Plot a histogram describing the distribution of number of friends
friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 130])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()


# SIMPLE STATISTICS

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

# To know the values at specific positions
sorted_values = sorted(num_friends)
smallest_value_2 = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

