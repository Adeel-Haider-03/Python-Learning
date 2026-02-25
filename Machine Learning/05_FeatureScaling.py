import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler #used for feature scaling

scale=StandardScaler() #create an instance of the StandardScaler class

df=pd.read_csv('data.csv')

X=df[['Volume', 'Weight']]  #independent variables

print("Before scaling:")
print(X)

