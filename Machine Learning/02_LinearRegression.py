import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

x = [1500, 1600, 1700, 1800, 1900, 2000]  #square footage of houses
y = [300000, 320000, 340000, 360000, 380000, 400000] #price of houses

plt.scatter(x, y)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

def myfun(x):
    return slope * x + intercept

mymodel = list(map(myfun, x)) #apply the function to each element in x, returns a list of predicted y values based on the linear model
print("Slope:", slope)
print("Intercept:", intercept)
print('r-squared:', r_value**2) #coefficient of determination, indicates how well the data fit the linear model, closer to 1 means a better fit
print("p-value:", p_value) #statistical significance of the slope, a low p-value (typically < 0.05) indicates that the slope is significantly different from zero
print("Standard Error:", std_err) #standard error of the slope, measures the average distance that the observed values fall from the regression line, smaller values indicate a better fit

plt.plot(x, mymodel) 
plt.show()


#predicting new values
new_x = 2100
predicted_y = myfun(new_x)
print("Predicted price for a house with", new_x, "square footage:", predicted_y)