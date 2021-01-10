import numpy as np

m1 = np.random.rand(5, 8)

m2 = np.ones((5, 8))

t1 = np.random.randint(0, 20, (3, 2, 4))

t2 = np.random.randint(0, 20, (3, 2, 4, 1))

# 1. Transpose
m1_t = m1.T
t1_t = t1.T
t2_t = t2.T

# 2. Scalar addition & multiplication
m3 = m2 + 5
m4 = m2 * 2

# 3. Matrix sum
s1 = m3 + m4

# 4. Inner product
m9 = np.random.rand(3, 2)
v3 = np.array([2, 2])

r4 = m9 * v3
r5 = m9.dot(v3)
r6 = np.dot(m9, v3)

v4 = np.array([3, 2, 1])
r7 = np.dot(v4, m9)

# 5. Inner product is Associative and Distributive, not commutative
m10 = np.ones((4, 3))
m10[(0, 2), :] = 0

m11 = np.zeros((3, 2))
m11[:, 1] = 2

m12 = np.eye(2)

a1 = ((m10.dot(m11)).dot(m12)) == m10.dot(m11.dot(m12))

# 6. (A.B)^t = B^t.A^t
m6_1 = np.random.rand(4, 7)
m6_2 = np.random.rand(7, 2)

m6_r1 = (m6_1.dot(m6_2)).T
m6_r2 = m6_2.T.dot(m6_1.T)
print(np.round(m6_r1, decimals=2) == np.round(m6_r2, decimals=2))

# 7. Identity matrix
m7_1 = np.eye(5)
m7_2 = np.random.randint(0, 50, (4, 5))
m7_r1 = m7_2.dot(m7_1)
print(m7_r1 == m7_2)

# 8. Inverse matrix
# Singular Matrix: a matrix that has no inverse
m8_1 = np.array([[5, 4, 2], [4, 1, 9], [12, 5, 0]])
m8_2 = np.linalg.inv(m8_1)

print(np.round(m8_1.dot(m8_2)) == np.eye(m8_1.shape[0]))

