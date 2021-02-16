from typing import List
from examples.linearalgebra.vectors import dot
from examples.statistics.tendencyandspread import de_mean, standard_deviation


# COVARIANCE
# Paired analogue of variance. Measures how two variables vary in tandem from their means.
# - Units are unclear, not easy to interpret.
# - Scale is not meaningful. Hard to say what counts as a 'large' covariance. Altered by scale of one of the variables.

def covariance(xs: List[float], ys: List[float]) -> float:
    """Joint variation of two variables with respect to their means. When x and y tend to have the same signs,
       the correlation would be possitve, when x and y tend to have opposite signs, the correlation would be negative.
       If there is no such relation, te correlation would tend to zero"""
    assert len(xs) == len(ys), "xs and ys must have the same number of elements"

    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


# CORRELATION
# - Is unitless and always lies between -1 (perfect anticorrelation) and 1 (perfect correlation).
# - Very sensitive to outliers.

def correlation(xs: List[float], ys: List[float]) -> float:
    """Measures how much xs and ys vary in tandem about their means"""
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)

    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0    # If no variation, correlation is zero


