import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from sklearn.metrics import r2_score


x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
# plt.scatter(x, y)

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print ('r2-value:', r_value**2)

# def myfun(x):
#     return slope * x + intercept

# mymodel = list(map(myfun, x))

# plt.plot(x, mymodel)
# plt.show()

#we applied a linear regression model to the data, but the line doesn't fit well.

#so let's try a polynomial regression model instead, which can capture more complex relationships between the variables.

poly_model=np.poly1d(np.polyfit(x, y, 3)) #fit a 3rd degree polynomial to the data

myline = np.linspace(1, 22, 100) #generate 100 evenly spaced values between 1 and 22

# plt.scatter(x, y)
# plt.plot(myline, poly_model(myline)) #plot the polynomial model
# plt.show()

r2=r2_score(y, poly_model(x)) #calculate the r-squared value for the polynomial model

print('r-squared:',r2 ) 

#r2-value: 0.18231625879420685  -> the linear model doesn't fit well, as the r-squared value is low (0.18).
#r-squared: 0.9432150416451026  -> the polynomial model fits much better, as the r-squared value is much higher (0.94).


#predicting new values
new_x = 17
predicted_y = poly_model(new_x)
print("Predicted value for x =", new_x, "is y =", predicted_y)