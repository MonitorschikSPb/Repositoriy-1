import pandas as pd
import numpy as np
my_list = [1, 2, 3, 4, 5]
s1 = pd.Series(my_list)
print(s1) #создание объекта Series из списка
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df1 = pd.DataFrame(my_array, columns=['A', 'B', 'C'])
print(df1) #создание объекта DataFrame из массива NumPy
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
s2 = pd.Series(my_dict)
print(s2) #создание объекта Series из словаря