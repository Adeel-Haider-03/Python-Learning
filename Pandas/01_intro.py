import pandas as pd

data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

# df=pd.DataFrame(data, columns=['Name', 'Age', 'City'])
# print(df)


#series

# s=pd.Series([10, 20, 30, 40, 50])  #default index
s=pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e']) #custom index
print(s)

#key/value pair
s2=pd.Series(data)   #key as index and value as data
print(s2)


#series vs dataframe
#series is 1D, dataframe is 2D
#series is like a column, dataframe is like a whole table