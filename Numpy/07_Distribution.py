import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

#seaborn is used to viusalize random distribution

# x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# x=np.random.randint(1,20,100) #array of 100 random integers between 1 and 20
# plt.hist(x)
# sns.displot(x)
# sns.displot(x, kind="kde") #shows continous distribution of data, it is a smoothed version of histogram
# plt.show()



#normal Distribution
x=np.random.normal(loc=1, scale=1, size=100) #loc is mean (all values will be centered arounf mean)
# , scale is standard deviation(mean how far points will be generated from mean, lesser the value closer the points),
# size is number of elements in array
# print(x)
# sns.displot(x, kind="kde")
# plt.show()

y=np.random.normal(loc=1, scale=1, size=(3,4)) #2D array of 3 rows and 4 columns
print(y)
# sns.displot(y)
# sns.displot(y, kind="kde")
plt.show()