from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('data.csv')
# print(df)

X=df[['Volume', 'Weight']]  #independent variables
Y=df['CO2']  #dependent variable

regr=linear_model.LinearRegression() #create a linear regression model
regr.fit(X,Y) #fit the model to the data

print('Coefficients:', regr.coef_) #coefficients for the independent variables, it shows how much the dependent variable (CO2) changes with a one-unit change in each independent variable (Volume and Weight), while keeping the other independent variable constant
#Coefficients: [0.00780526 0.00755095]
# this tell us if the engine size (Volume) increases by 1cm3, the CO2 emission increases by 0.00780526g.
# These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.

predicted_CO2 = regr.predict([[2300, 1300]]) #predict the CO2 emission for a car with a volume of 2000cm3 and a weight of 1500kg
print("Predicted CO2:", predicted_CO2)