import pandas as pd

# data=pd.read_csv('data.csv')
# print(data.info())
# data.dropna(inplace=True)  #to drop rows with missing values, inplace=True modifies the original dataframe
# print(data.info())

#other way to handle missing values is to fill them with a specific value, for example,a number or the mean of the column, median etc

data=pd.read_csv('data.csv')
# print(data.info())

# data.fillna(0)  #to fill missing values with 0
# print(data.info())

# print(data['Calories'].to_string())
data['Calories'].replace('NaN',0, inplace=True)  #to fill missing values with 0
# data['Calories'].fillna(data['Calories'].mean(), inplace=True)  #to fill missing values with the mean of the column
print(data['Calories'].to_string())