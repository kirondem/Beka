
import os
import pandas as pd

PATH  =  os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(PATH, '..', '..',  'data', 'MINI Longleat 12042022.csv')

#file_path = "C:\\Work\\Beka\\data\\MINI Longleat 12042022.csv"

df = pd.read_csv(file_path, header=0)

# Print the first 5 rows of the dataframe
print(df.tail(10))

#Get all columns
print(df.columns)

# Get shape of the dataframe
print(df.shape)

#Get unique values in a column
print(df['Customer Vehicle Relation Type Code (Contact Vehicle UK)'].value_counts())

#select all rows with NaN values
null_NBV1 = df[df['NBV1'].isnull()]
print(null_NBV1)

# select all unique values for a column
unique_NBV1 = df['NBV1'].unique()
print(unique_NBV1)

# Drop DateTime column
df = df.drop(columns=['Contact Key'])