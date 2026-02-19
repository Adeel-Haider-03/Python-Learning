import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('data.csv')

print(data.corr())  #to calculate the correlation between the columns in the dataframe, it will return a correlation matrix where the values range from -1 to 1,
#where -1 indicates a strong negative correlation, (one goes up other goes down)
#  0 indicates no correlation,
#  and 1 indicates a strong positive correlation. (one goes up other goes up)


# data.plot() 

data.plot(x='Duration', y='Calories', kind='scatter')  #to create a scatter plot to visualize the correlation between the 'Duration' and 'Calories' columns (it is strongly correlated because the points are close to a straight line)
plt.show()

data.plot(x='Duration', y='Maxpulse', kind='scatter')  #to create a scatter plot to visualize the correlation between the 'Duration' and 'Max Pulse' columns (it is weakly correlated because the points are scattered)
plt.show()