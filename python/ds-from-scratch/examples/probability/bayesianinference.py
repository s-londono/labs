import math

# An alternative approach to inference, which treats the unknown parameters as random variables.
# 1. Start with an a-prior distribution for the parameters
# 2. Then use the observed data and the Bayes Theorem to get an updated posterior distribution for the parameters
# Rather than making probability judgments about the tests, make probability judgements about the parameters

# E.g.: For a coin flip, the unknown parameter is the probability of heads. Use a Beta distribution as "prior"


def B(alpha: float, beta: float) -> float:
    """A normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)


def beta_pdf(x: float, alpha: float, beta: float) -> float:
    """Beta distribution. Centers its weight at alpha / (alpha + beta)"""
    if x <= 0 or x >= 1:
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)


# Example:
# Assume a prior distribution on p. If we have a strong belief that the coin lands heads 55% of the time, and we
# choose alpha equals 55, beta equals 45.
# Then we flip our coin a bunch of times and see h heads and t tails. Baye's theorem tells that the posterior
# distribution for p is again a Beta distribution, but with parameters alpha + h and beta + t
# If you flipped the coin more and more times, the prior would matter less and less until eventually you'd have (nearly)
# the same posterior distribution no matter which prior you started with

# This allows to make probability statements about hypotheses: "Based on the prior and the observed data, there is
# only 5% likelihood the coin's heads probability is between 49% and 51%". This is philosophically very different from
# a statement like "If the coin were fair, we would expect to observe data so extreme only 5% of the time"

# Using Bayesian inference to test hypotheses is considered somewhat controversial. In part because the mathematics
# can get somewhat complicated, and in part because of the subjective nature of chosing a prior

