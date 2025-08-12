import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

array_2d = array.reshape(6, 2)
print(array_2d)
print(array_2d.shape)

array_3d = array.reshape(2, 2,3)
print(array_3d)
print(array_3d.shape)

array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,10])

array3 = np.concatenate((array1, array2))
print(array3)

array_2d_1 = np.array([[1,2], [3,4]])
array_2d_2 = np.array([[5,6], [7,8]])

array_2d_3 = np.concatenate((array_2d_1, array_2d_2), axis = 0)
print(array_2d_3)

array_2d_4 = np.concatenate((array_2d_1, array_2d_2), axis = 1)
print(array_2d_4)

array_2d_5 = np.vstack((array_2d_1, array_2d_2))
print(array_2d_5)

array_2d_6 = np.hstack((array_2d_1, array_2d_2))
print(array_2d_6)