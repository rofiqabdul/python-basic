import numpy as np

x = np.arange(2, 6).reshape(4)
print(x)

list_array = [12.23, 13.32, 100, 36.32]
array_from_list = np.array(list_array)

print(list_array)
print(array_from_list)

array_2d = np.arange(2, 11).reshape(3,3)

print(array_2d)

null_vektor = np.zeros(10)

print(null_vektor)

null_vektor[6] = 11

print(null_vektor)

array_26 = np.arange(12, 38).reshape(26)

print(array_26)

print(np.flip(array_26))