import numpy as np

# BROADCASTING
# https://numpy.org/doc/stable/user/theory.broadcasting.html#array-broadcasting-in-numpy
# Broadcasting describes how numpy treats arrays with different shapes during arithmetic operations. Subject to certain
# constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes.
# Provides a means of vectorizing array operations so that looping occurs in C instead of Python. It does this without
# making needless copies of data. But there are also cases where broadcasting is a bad idea because it leads to
# inefficient use of memory that slows computation

# The Broadcasting Rule:
# In order to broadcast, the size of the trailing axes for both arrays in an operation must either be the same size
# or one of them must be one

# Add arrays having different shapes
v1 = np.arange(0, 5)
m1 = np.ones((5, 5))

r1 = v1 + m1

v2 = np.arange(0, 5)
m2 = np.ones((5, 1))

r2 = v2 + m2

# Fails
m3 = np.ones((5, 3, 4))
m4 = np.ones((5, 1))

r3 = m3 + m4
