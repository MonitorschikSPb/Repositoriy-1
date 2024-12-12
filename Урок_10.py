import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Создание объекта Series
s1 = pd.Series([1, 2, 3, 4, 5])
#Создание объекта DataFrame из списка
df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
#Создание объекта DataFrame из массива NumPy
arr = np.random.randint(1, 10, (5, 2))
df2 = pd.DataFrame(arr, columns=['C', 'D'])
#Получение не пересекающихся элементов в двух объектах Series
s2 = pd.Series([4, 5, 6, 7, 8])
diff_s = pd.concat([s1[~s1.isin(s2)], s2[~s2.isin(s1)])
#Получение не пересекающихся элементов в двух столбцах одного DataFrame
df_diff = df1.loc[~df1['A'].isin(df2['C'])]
#Частота уникальных элементов в объекте Series
s3 = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
freq = s3.value_counts()
freq.plot(kind='bar')
plt.show()
#Объединение двух DataFrames вертикально
df_concat_v = pd.concat([df1, df2], axis=0)
#Объединение двух DataFrames горизонтально
df_concat_h = pd.concat([df1, df2], axis=1)
#График зависимости одного столбца от другого для DataFrame
df1.plot(x='A', y='B', kind='scatter')
plt.show()