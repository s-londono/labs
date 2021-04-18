from collections import Counter
import matplotlib.pyplot as plt
import math
import random
from distribution import normal_cdf

# CENTRAL LIMIT THEOREM
# A random variable defined as the average of a large number of independent and identically distributed random
# variables is itself approximately normally distributed

# An easy way to illustrate this is by looking at binomial random variables, which have two parameters n and p.
# A Binomial(n, p) random variable is the sum of n independent Bernoulli(p) random variables, each of which equals 1
# with probability p and 0 with probability 1 - p.

# The mean of Bernoulli(p) is p and its std. dev is sqrt(p * (1 - p)). The CTL says that as n gets large, a
# Binomial(n, p) is approximately normal with mean np and std. dev. sqrt(n * p * (1 - p))

# Thus, if you want to know the probability that a fair coin turns up more than 60 heads in 100 flips, you can estimate
# it as the probability that a Normal(50, 5) is greater than 60, which is easier than computing the
# Binomial(100, 0.5) CDF

def bernoulli_trial(p: float) -> int:
    """Returns 1 with probability p and 0 with probability 1 - p"""
    return 1 if random.random() < p else 0


def binomial_trial(n: int, p: float) -> int:
    """Returns the sum of n Bernoulli(p) trials"""
    return sum(bernoulli_trial(p) for _ in range(n))


def binomial_histogram(p: float, n: int, num_points: int) -> None:
    """Picks points from a Binomial(n, p) and plots their histogram"""
    data = [binomial_trial(n, p) for _ in range(num_points)]

    # Use a bar chart to show the actual binomial samples
    histogram = Counter(data)

    plt.bar([x - 0.4 for x in histogram.keys()], [v / num_points for v in histogram.values()], 0.8, color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # Use a linear chart to show the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()


if __name__ == "__main__":
    binomial_histogram(0.75, 100, 20000)
