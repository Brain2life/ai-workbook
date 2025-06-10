# Matrix multiplication is done via `@` operator or matmul function.
# For more information, see https://www.datacamp.com/doc/numpy/matrix-multiplication

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
scalar = 2

print("A + B =\n", A + B)
print("A - B =\n", A - B)
print("2 * A =\n", scalar * A)
print("A @ B =\n", A @ B)  # matrix multiplication
