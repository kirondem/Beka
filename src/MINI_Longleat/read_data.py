
import os
import pandas as pd

PATH  =  os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(PATH, '..', '..',  'data', 'MINI Longleat 12042022.csv')

#file_path = "C:\\Work\\Beka\\data\\MINI Longleat 12042022.csv"

# 1) Read the data from the csv file into a pandas dataframe
df = pd.read_csv(file_path, header=0)

# 2)  Get shape of the dataframe
no_of_rows_colums = df.shape
print(no_of_rows_colums)

# 3) Get all columns
columns = df.columns
columns = list(columns)
print(columns)

# 4) Print the first 5 rows of the dataframe
first_X_rows = df.head()
print(first_X_rows)

# 5) Print the last 10 rows of the dataframe
last_X_rows = df.tail(10) 
print(last_X_rows)

# 6) select all unique values for a column
unique_NBV1 = df['NBV1'].unique()
print(unique_NBV1)

# 7) Get unique values in a column
unique_with_count_NBV1 = df['NBV1'].value_counts()
print(unique_with_count_NBV1)


# 8) select all rows with NaN values
null_NBV1 = df[df['NBV1'].isnull()]
print(null_NBV1)

# 9) Drop Contact Key column
df = df.drop(columns=['Contact Key'])
# Print the first 5 rows of the dataframe
first_X_rows = df.head()
print(first_X_rows)