from typing import Tuple
from distribution import normal_cdf, inverse_normal_cdf
import math

# H0: Null hyphesis vs. H1: Alternaive hypothesis. Determine which one is more likely as to the observations.
# Whenever a random variable follows a normal distribution, we can use normal_cdf to figure out the probability that its
# realized value lies within or outside a particular interval


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """Returns mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


# The normal CDF is the probabilith the variable is below a threshold
normal_probability_below = normal_cdf


# It's above the threshold if it's not below the threshold
def normal_probability_above(lo: float, mu: float = 0, sigma: float = 1) -> float:
    """The probability that N(mu, sigma) is greater than lo"""
    return 1 - normal_cdf(lo, mu, sigma)


# It's between if it's less than hi, but no less than lo
def normal_probability_between(lo: float, hi: float, mu: float = 0, sigma: float = 1) -> float:
    """The probability that an N(mu, sigma) is between lo and hi"""
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# It's outside if it's not between
def normal_probability_outside(lo: float, hi: float, mu: float = 0, sigma: float = 1) -> float:
    """The probability that an N(mu, sigma) is not between lo and hi"""
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability: float, mu: float = 0, sigma: float = 1) -> float:
    """Returns the z for which P(Z <= z) = probabiity"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability: float, mu: float = 0, sigma: float = 1) -> float:
    """Returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability: float, mu: float = 0, sigma: float = 1) -> Tuple[float, float]:
    """Returns the symmetric (about the mean) bounds that contain the specified probability"""
    tail_probability = (1 - probability) / 2

    # Upper bound should have probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # Lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound


# Let X be a random variable: number of tails obtained by flipping a coin n times (Binomial distribution).
# Say we chose to flip the coin n = 1000 times. Hypothesis: The coin is fair.
# If the hypothesis is true, X should be distributed aprox. normally with mean 500 and std. dev. 15.8:
mu0, sigma0 = normal_approximation_to_binomial(1000, 0.5)

# Significance (often 5% or 1%). How willing are we to make:
# - Type I errors: false positive. We reject H0 even though it's true.
# So if we choose a significance of 5%, the H0 should be rejected if the observed mean is outside of the bounds:

# 95% bounds based on assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu0, sigma0)

# Power of a test. Probability of not making a:
# - Type II error: false negative. We fail to reject H0 even though it's false.

# Actual mu and sigma based on p = 0.55 (coin is biased toward heads)
mu1, sigma1 = normal_approximation_to_binomial(1000, 0.55)

# A type 2 error will happen when X is still in our original interval
type_2_probability = normal_probability_between(lo, hi, mu1, sigma1)
power1 = 1 - type_2_probability

# Imagine that the null hypothesis is that the coin is not biased toward heads (p <= 0.5). We want a one-sided test that
# rejects the null hypothesis when X is much larger than 500 but not when X is smaller than 500.
# So, a 5% significance test involves finding the cutoff below which 95% of the probability lies:
hi = normal_upper_bound(0.95, mu0, sigma0)
type_2_probability = normal_probability_below(hi, mu1, sigma1)
power2 = 1 - type_2_probability

