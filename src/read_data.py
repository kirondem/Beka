
import os
import pandas as pd

PATH  =  os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(PATH, '..\\' 'data', 'MINI Longleat 12042022.csv'), header=0)

# Print the first 5 rows of the dataframe
print(df.head())


#select all rows with NaN values
null_NBV1 = df[df['NBV1'].isnull()]
print(null_NBV1)

# select all unique values for a column
unique_NBV1 = df['NBV1'].unique()
print(unique_NBV1)

# Drop DateTime column
df = df.drop(columns=['Contact Key'])