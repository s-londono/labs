import math
import matplotlib.pyplot as plt

SQRT_TWO_PI = math.sqrt(2 * math.pi)


# THE NORMAL DISTRIBUTION
def nommal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma)


def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    """The CDF of the Normal distribution cannot be written in an elementary manner, but we can write it using
        Python's ERF (Error Function)"""
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001) -> float:
    """Find approximate inverse using binary search. We need to invert normal_cdf to find the value corresponding to
       a specified probability (p-value). There's no simple way to compute its inverse, but normal_cdf is continuous
       and strictly increasing, so we can use a Binary Search. This function repeatedly bisects intervals until it
       narrows in on a Z that's close enough to the desired probability (p-value)"""
    # If not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    # normal_cdf(-10) is very close to 0, normal_cdf(10) is very close to 1
    low_z = -10.0
    hi_z = 10.0

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            hi_z = mid_z

    return mid_z


# Plot the PDF
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [nommal_pdf(x, sigma=1) for x in xs], "-", label="mu=0, sigma=1")
plt.plot(xs, [nommal_pdf(x, sigma=2) for x in xs], "--", label="mu=0, sigma=2")
plt.plot(xs, [nommal_pdf(x, sigma=0.5) for x in xs], ":", label="mu=0, sigma=0.5")
plt.plot(xs, [nommal_pdf(x, mu=-1) for x in xs], "-.", label="mu=-1, sigma=1")
plt.legend()
plt.title("Various Normal PDFs")
plt.show()

plt.clf()

# Plot the CDF
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], "-", label="mu=0,sigma=1")
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], "--", label="mu=0,sigma=2")
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ":", label="mu=0,sigma=0.5")
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], ":", label="mu=-1,sigma=1")
plt.legend(loc=4)
plt.title("Various Normal CDFs")
plt.show()
