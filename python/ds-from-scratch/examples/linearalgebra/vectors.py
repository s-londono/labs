# WARNING: Using lists as vectors is terrible for performance. In production code, you would want to use the NumPy
# library, which includes a high-performance array class with all sorts of arithmetic operations included
import math
from typing import List

# Define the type Vector of decimal numbers
Vector = List[float]

# A vector
height_weight_age = [70, 170, 40]


def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w)

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def substract(v: Vector, w: Vector) -> Vector:
    """Substracts corresponding elements"""
    assert len(v) == len(w)

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    assert vectors, "No vectors provided"

    # Check that vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors)

    # The i-th element of the result is the sum of every vector[i]
    return [sum(v[i] for v in vectors) for i in range(num_elements)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


# Dot Product: If w has magnitude 1, the dot product measures how far the vector v extends in the w direction.
# In other words, the length of the vector you'd get if you project v onto w
def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "Vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """Returns the length of v"""
    return math.sqrt(sum_of_squares(v))


def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1)**2 + (v_2 - w_2)**2 + ... + (v_n - w_n)**2"""
    return sum_of_squares(substract(v, w))


def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return magnitude(substract(v, w))


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert substract([1, 2, 3], [4, 2, 6]) == [-3, 0, -3]
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
assert dot([1, 2, 3], [4, 5, 6]) == 32
assert sum_of_squares([1, 2, 3]) == 14
assert magnitude([3, 4]) == 5
