# access elements of array
# array[row_index, col_index]

import numpy as np

array = np.array([1,2,3,4,5])

print(array[1])
print(array[0:5])
print(array[0:2])
print(array[2:4])

arr_2d = np.array([[1,2,3], [4,5,6]])

print(arr_2d[0,1])
print(arr_2d[:,1])
print(arr_2d[1,0:3])
print(arr_2d[0,1:3])

arr_3d = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])

print(arr_3d[1,1,1])
print(arr_3d[0,1,1])
print(arr_3d[0,0,1])
print(arr_3d[1,1,0:3])
print(arr_3d[0,1,0:3])

arr = np.array([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

print(arr[18:])