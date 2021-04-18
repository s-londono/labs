from typing import Tuple
import math
from pvalues import two_sided_p_value


# A/B Tests compares two alternatives (A and B). E.g. Which advertisement is more likely to get clicked? A or B?
# Say Na: people who see add A, Nb: people who see add B, na: people who saw add A and clicked, nb: people who saw
# add B and clicked.
# Think of each view as a Bernoulli trial. Then: na/Na aprox. normally distributed, nb/Nb aprox. normally distributed.
# With parameters:

def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
    p = n/N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


# Assuming that those two normals are independent, their difference should also be normal with mean: pb - pa and
# std. deviation: sqrt(sa² + sb²). This means we can test the null hypothesis that pa and pb are the same (that is,
# pa - pb = 0) by using the statistic (which approximately should have Standard Normal distribution if pa = pb):

def a_b_test_statistic(Na: int, na: int, Nb: int, nb: int) -> float:
    pA, sigmaA = estimated_parameters(Na, na)
    pB, sigmaB = estimated_parameters(Nb, nb)
    return (pB - pA) / math.sqrt(sigmaA ** 2 + sigmaB ** 2)


# For example, comparing experiment A: 200 clicks out of 100 with B: 180 clicks out of 1000, the statistic equals:
z = a_b_test_statistic(1000, 200, 1000, 180)

# The probability of seeing such a large difference if the means were actually equal is:
pe = two_sided_p_value(z)
