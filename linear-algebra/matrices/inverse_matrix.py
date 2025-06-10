# Calculate Inverse Matrix
# To verify result: A * A(-1) = I should be identity matrix

import numpy as np

A = np.array([[4, 2], [7, 6]])

# Compute the determinant of a matrix 
det_A = np.linalg.det(A)

print("Determinant:", det_A)  # Should be 10

# Compute the inverse of a matrix
inverse_A = np.linalg.inv(A)

print("Inverse of A:\n", inverse_A)