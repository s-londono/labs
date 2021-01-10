import matplotlib.pyplot as plt
import numpy as np

# Print numbers very close to 0 as 0
np.set_printoptions(suppress=True)

# 1. Linear Equations System Ax = b:
# 3x + y = 1
# 2x + y = 1
A = np.array([[3, 1], [2, 1]])
b = np.array([1, 1])

Ainv = np.linalg.inv(A)

x = Ainv.dot(b)

print(x)

# 2. Overspecified system
x2 = np.arange(-10, 10)

y2_1 = 3*x2 + 5
y2_2 = -x2 + 3
y2_3 = 2*x2 + 1

plt.plot(x2, y2_1)
plt.plot(x2, y2_2)
plt.plot(x2, y2_3)

plt.xlim(-12, 12)
plt.ylim(-12, 12)

plt.axhline(y=0, color="grey")
plt.axvline(x=0, color="grey")

plt.show()

# 3. Same number of variables and equations. With solution vs. no solution (parallel)
y3_1 = 2*x2 + 7
y3_2 = -3*x2 + 2

# Use subplot to chart in two sections of the same figure. Function-oriented plotting
plt.subplot(1, 2, 1)
plt.plot(x2, y3_1)
plt.plot(x2, y3_2)

y3_3 = 2*x2 + 7
y3_4 = 2*x2 + 12

plt.subplot(1, 2, 2)
plt.plot(x2, y3_3)
plt.plot(x2, y3_4)

plt.show()

