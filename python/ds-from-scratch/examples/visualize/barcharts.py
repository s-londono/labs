from collections import Counter
from matplotlib import pyplot as plt

# Barcharts: Show how some quantity varies among some discrete set of items

movies = ["Ben-Hur", "Annie Hall", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [11, 5, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")
plt.ylabel("# of Academy Awards")

# Label x-axis with movie names at bar centers
plt.xticks(range(len(movies)), movies)

plt.show()

# Clear the current figure
plt.clf()

# A bar chat is also useful to plot a histogram of bucketed numeric values
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

# Shift bars right by 5. Give each bar its correct height. Give each bar a width of 10
plt.bar([x + 5 for x in histogram.keys()], histogram.values(), 10, edgecolor=(0, 0, 0))

# X-axis from -5 to 105, y-axis from 0 to 5
plt.axis([-5, 105, 0, 5])

# X-axis labels at 10, 20, ..., 100
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()

# Clear the current figure
plt.clf()

# Be judicious when using plt.axis. When creating bar charts it is considered especially bad form for your y-axis not
# to start at 0, since this is an easy way to mislead people
mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science")

# If you don't do this, matplot lib will label the x-axis 0, 1 and then add a +2.013e3 off in the corner (still needed?)
# Refer to: https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ticklabel_format
plt.ticklabel_format(useOffset=False)

# Misleading y-axis! only shows the part above 500. Should be 0 - 506
plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Look at the 'Huge increase'!")
plt.show()
