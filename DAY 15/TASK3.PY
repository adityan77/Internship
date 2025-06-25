# Selection and Indexing:

# Select only the Name column.

# Select the first 3 rows using .iloc.

# Select people older than 30.
import pandas as pd
data = {
    'Name': ['Adi', 'Prasad', 'Piyush','Jayesh'],
    'Age': [25, 30, 35,34],
    'City': ['Nashik', 'Mumbai', 'Bangalore','Delhi'],
    # 'Id':[34,305,402]
}
df=pd.DataFrame(data)
# print(df['Name'])
print(df.Name)

print(df.iloc[0:3])
print('-----------------------------------')
print(df[df['Age']>=30])
