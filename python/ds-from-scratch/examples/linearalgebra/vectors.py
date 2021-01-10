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


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert substract([1, 2, 3], [4, 2, 6]) == [-3, 0, -3]
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
assert dot([1, 2, 3], [4, 5, 6]) == 32
