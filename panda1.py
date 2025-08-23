import pandas as pd
import numpy as np

dataset = {
    'bikes': ["Bullet", "java", "hero"],
    'cc': [350, 200, 125]
}

print(pd.DataFrame(dataset))

d = {
    'a': 1,
    'b': 2,
    'c': 3
}
ser = pd.Series(data = d, index = ['a', 'b', 'c'])

print(ser)

a = [1, 7, 2]
var = pd.Series(a)

print(var)

b = [1, 2, 3]
varB = pd.Series(b, index = ["a", "b", "c"])

print(varB)

data = {
    'col1': [1, 2],
    'col2': [3, 4]
}
df = pd.DataFrame(data = data)

print(df)

arr = np.random.randint(1, 100, (10, 4))
print(arr)

df_arr = pd.DataFrame(arr, columns = ['a', 'b', 'c', 'd'])

print(df_arr)