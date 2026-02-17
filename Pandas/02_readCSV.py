import pandas as pd


data=pd.read_csv('data.csv') 
# print(data)  #if large datset, it will print only the first and last few rows

# print(data.to_string())  #to print the whole dataframe without truncation

print(data.head())  #to print the first 5 rows
print(data.tail())  #to print the last 5 rows
print(data.info())  #to get a summary of the dataframe
print(data.describe())  #to get statistical summary of the dataframe
print(data.head(10))  #to print the first 10 rows