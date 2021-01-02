import pandas as pd
import numpy as np

#reading the file.
df = pd.read_csv('./data/vehicles.csv')

#counting null values.
null_values = df.isnull().sum()

#max and min values for numerical columns.
numerics = ['float64', 'int64']
new_df = df.select_dtypes(include = numerics)

print('Data frame shape is:', df.shape)
print()
print('Data frame lenght is:', len(df.index))
print()
print('Columns are:', df.columns)
print()
print('Columns type are:', df.dtypes)
print()
print('The amount of null values per column is:', null_values)
print()
print('The maximum value in each column is:', new_df.max())
print()
print('The minimum value in each column is:', new_df.min())



