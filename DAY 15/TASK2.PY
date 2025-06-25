# Create a DataFrame:

# Create a DataFrame with columns: Products, Price, and Stock.

# Add 5 sample rows.
import pandas as pd
data={
    'Products':['Laptop','Mobile','Mouse','Keyboard','Charger','Pen Drives','Stand'],
    'Price':['75000','25000','500','800','200','350','300'],
    'Stock':['5','3','12','12','20','15','20']
    }
df=pd.DataFrame(data)
# print(df)
print(df.to_string(index=False))

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
