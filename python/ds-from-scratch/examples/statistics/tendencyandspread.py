import math
from typing import List
from collections import Counter
from examples.linearalgebra.vectors import sum_of_squares

# CENTRAL TENDENCIES
# Where is the data centered
# - Mean: Smooth, but very sensitive to outliers


def mean(xs: List[float]) -> float:
    """Halfpoint between a set of values"""
    return sum(xs) / len(xs)


def _median_odd(xs: List[float]) -> float:
    """If len(x) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    """If len(x) is even, the median is the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2


def median(v: List[float]) -> float:
    """Finds the middle-most value of v"""
    return _median_odd(v) if len(v) % 2 == 1 else _median_even(v)


def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in x"""
    p_index = int(len(xs) * p)
    return sorted(xs)[p_index]


def mode(xs: List[float]) -> List[float]:
    """Most frequent value"""
    counter = Counter(xs)
    max_occurs = max(counter.values())
    return [x_i for x_i, occurs in counter.items() if occurs == max_occurs]


# DISPERSION
# Measure how spread out our data is

def date_range(xs: List[float]) -> float:
    """Distance between the most extreme values"""
    return max(xs) - min(xs)


def de_mean(xs: List[float]) -> List[float]:
    """Distance from each point to the mean"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]) -> float:
    """Variance"""
    assert len(xs) >= 2, "Variance requires at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    # Divide by (n - 1) in order to obtain an unbiased estimator
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(xs: List[float]) -> float:
    """The standard deviation is in the same units of the data"""
    return math.sqrt(variance(xs))


def interquartile_range(xs: List[float]) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile. Not affected by a small number of outliers"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)


assert mean([1, 3, 9, -5]) == 2.0, "Incorrect mean value"
assert median([1, 10, 2, 9, 5]) == 5, "Incorrect median"
assert median([1, 9, 2, 10]) == (2 + 9) / 2, "Incorrect median"

num_friends = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 9]

assert quantile(num_friends, 0.1) == 1, "10th percentile should be 1"
assert quantile(num_friends, 0.25) == 3, "25th percentile should be 3"
assert set(mode(num_friends)) == {8, 9}
assert date_range(num_friends) == 10, "Range should  be 10"
