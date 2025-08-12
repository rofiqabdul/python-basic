import numpy as np

array_zeros = np.zeros((4, 5))
print(array_zeros)

array_ones = np.ones((4, 5))
print(array_ones)

array_full = np.full((4,5), 3)
print(array_full)

array_of_identity_matrix = np.eye(4)
print(array_of_identity_matrix)

array_of_random_integer = np.random.randint(10,100,(3,3))
print(array_of_random_integer)

array_linspace = np.linspace(10, 21, 6)
print(array_linspace)

array_of_diagonal_matrix = np.diag([1,2,3,4,5])
print(array_of_diagonal_matrix)