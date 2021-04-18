import random
from typing import Tuple
from distribution import normal_cdf, inverse_normal_cdf
from hypothesistesting import normal_probability_above, normal_probability_below, normal_approximation_to_binomial


# Alternative way of performing Hyphotesis Testing.
# Compute the probability that we would see a value at least as extreme as the one we actually observed.

def two_sided_p_value(x: float, mu: float = 0, sigma: float = 1) -> float:
    """How likely are we to see a value at least as extreme as x (in either direction) if
       our values are from an N(mu, sigma)?"""
    if x > mu:
        # x is greater than the mean, so the tail is everything greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # x is less than the mean, so the tail is everything less than x
        return 2 * normal_probability_below(x, mu, sigma)


mu0, sigma0 = normal_approximation_to_binomial(1000, 0.5)

# Example: if we were to see 530 heads, we would compute.
# Note that we use 529.5 instead of 530 as a Continuity Correction
tspv = two_sided_p_value(529.5, mu0, sigma0)

# If the p-value is greater than the % of significance, we do not reject the null
# (e.g. 0.062 is greater than a 5% significance, then in case of obtaining that p-value, we do not reject the null)

# Also applies for one-sided tests
upper_pvalue = normal_probability_above
lower_pvalue = normal_probability_below

# For our one-sided test, if we saw 525 heads we would compute:
upper_pvalue_test = upper_pvalue(524.5, mu0, sigma0)

# IMPORTANT: Make sure data is roughly normally distributed before using normal_probability_* to compute p-values
# Start by plotting the data and use statistical tests for normality

# SIMULATION

extreme_value_count = 0

for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1

# p-value was 0.062 => ~62 extreme values out of 1000
assert 59 < extreme_value_count < 65, f"{extreme_value_count}"
