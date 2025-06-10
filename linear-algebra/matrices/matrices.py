import numpy as np

# General type of matrix 
# https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array
general_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("General Matrix:")
print(general_matrix)

# Square Matrix
square_matrix = np.array([
    [2, 0, 1],
    [1, 3, 4],
    [5, 6, 0]
])
print("Square Matrix:")
print(square_matrix)

# Verify the type of matrices
# https://numpy.org/doc/stable/reference/generated/numpy.shape.html
def is_square(matrix):
    return matrix.shape[0] == matrix.shape[1] # Compare the number of rows and columns

print("Is square matrix?", is_square(square_matrix))   # True
print("Is general matrix square?", is_square(general_matrix))  # False
