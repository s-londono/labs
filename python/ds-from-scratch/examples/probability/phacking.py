import random
from typing import List

# A procedure that erroneously rejects the null hypothesis only 5% of the time will, by definition, 5% of the
# time erroneously reject the null hypothesis.
# If you are are setting out to find "significant" results, you usually can.

# P-Hacking is the deceitful trick of:
# - Testing many hypotheses, until finding one that appears significant.
# - Remove selected outliers to get a p-value below the value needed to reject the null hypothesis.

# To do good science, determine the hypothesis before looking at the data.
# Check: The Earth is Round, by Jacob Cohen


# SIMULATION: Number of rejections

def run_experiment() -> List[bool]:
    """Flips a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiments: List[bool]) -> bool:
    """Using 5% of the significance levels"""
    num_heads = len([flip for flip in experiments if flip])
    return num_heads < 469 or num_heads > 531


random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment for experiment in experiments if reject_fairness(experiment)])

assert num_rejections == 46



