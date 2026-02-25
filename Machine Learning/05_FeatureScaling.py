import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler #used for feature scaling

scale=StandardScaler() #create an instance of the StandardScaler class

df=pd.read_csv('data.csv')

#convert Volume into litres
df['Volume']=df['Volume']/1000


# print("Before scaling:")
# print(df)

#now the Volume and weight have different scales, we need to scale them before fitting the model

X=df[['Volume', 'Weight']]  #independent variables

scaled_x=scale.fit_transform(X) #fit the scaler to the data and transform it

# print("After scaling:")
# print(scaled_x)


Y=df[['CO2']] 

regr=linear_model.LinearRegression() #create a linear regression model
regr.fit(scaled_x,Y) #fit the model to the scaled data

#when we scale features we have to use the same scaler to transform the new data before making predictions
prediction=scale.transform([[2.3, 1300]]) #scale the new data using the same scaler
print("Scaled prediction input:", prediction)

predicted_co2=regr.predict([prediction[0]]) 
print("Predicted CO2:", predicted_co2)