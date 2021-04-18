import math
from hypothesistesting import normal_two_sided_bounds

# We test hypotheses about the value of a distribution parameter (e.g. probability p of heads in a coin toss).
# - Confindence Interval (around the observed value of the parameter):
#   how confident we are about the estimate of the parameter of a distribution, based on observations.

# E.g. Coin toss. Bernoulli variable. Average of the number of heads (a Bernoulli variable).
# If we observe 525 heads out of 1000 flips, then estimated p = 0.525.
# From the Central Limit Theorem, the average of those Bernoulli variables should be aprox. Normal, with mean p and
# std. dev. math.sqrt(p * (1 - p) / 1000). We don't know p, so we use the estimate:

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)

# This is not entirely justified, but people seem to do it anyway...
# Using the Normal approximation, we conclude that we are "95% confident" that the following interval contains the
# true parameter p:
lo, hi = normal_two_sided_bounds(0.95, mu, sigma)

# So, if 0.5 falls within our confidence interval, we do not conclude that the coin is unfair.
