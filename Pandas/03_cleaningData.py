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
# data['Calories'].replace('NaN',0, inplace=True)  #to fill missing values with 0
# # data['Calories'].fillna(data['Calories'].mean(), inplace=True)  #to fill missing values with the mean of the column
# print(data['Calories'].to_string())
# print(data['Duration'].to_string())

#replace the value at index 69 in the 'Duration' column with 45
# data.at[69,'Duration']=45

# data.loc[69,'Duration']=50

#why .loc doesn't work here? because .loc is used for label-based indexing,
# and the index 69 is not a label but a positional index. To use .loc, you would need to set the index of the DataFrame to a column that contains unique labels, or use .iloc for positional indexing.

data.iloc[69, data.columns.get_loc('Duration')]=50  #to replace the value at index 69 in the 'Duration' column with 45
print(data['Duration'].to_string())