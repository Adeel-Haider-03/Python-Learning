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

#--------------------------------------------------------------------------------------------------------------------#

#normal Distribution
# x=np.random.normal(loc=1, scale=1, size=100) #loc is mean (all values will be centered arounf mean)
# , scale is standard deviation(mean how far points will be generated from mean, lesser the value closer the points),
# size is number of elements in array
# print(x)
# sns.displot(x, kind="kde")
# plt.show()

# y=np.random.normal(loc=1, scale=1, size=(3,4)) #2D array of 3 rows and 4 columns
# print(y)
# # sns.displot(y)
# # sns.displot(y, kind="kde")
# plt.show()

#--------------------------------------------------------------------------------------------------------------------#

#Bionomial Distribution  (it is descrete while normal distribution is continous), describe outcome of binary scenario
#n=number of trials, p=probability of success, size=number of elements in array

# toss=np.random.binomial(n=1,p=0.5,size=10) #n=1 means we are tossing a coin once
# print(toss)
# sns.displot(toss,kind='kde')
# plt.show()

#if we increase size it will almost become normal distribution
data={
    'normal':np.random.normal(loc=1,scale=1,size=1000),
    'binomial':np.random.binomial(n=1,p=0.5,size=1000)
}

# sns.displot(data,kind='kde')
# plt.show() 


#----------------------------------------------------------------------------------------------------#

#Poisson Distribution ,It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

# x=random.poisson(lam=2, size=1000) #lam is the expected number of events that occur in a fixed interval of time or space
# # print(x)
# sns.displot(x)
# plt.show()

#-------------------------------------------------------------------------------------#
#uniform distribution, it is continous distribution where all values are equally likely to occur
# y=random.uniform(low=0, high=1, size=10) 
# sns.displot(y)
# plt.show()

# #-------------------------------------------------------------------------------------#

# #logistic distribution, it is continous distribution used to model growth of population, it is similar to normal distribution but has heavier tails
# z=random.logistic(loc=0, scale=1, size=1000) #loc is mean, scale is standard deviation
# sns.displot(z, kind='kde')
# plt.show()

#-------------------------------------------------------------------------------------#
#multinomial distribution, it is descrete distribution used to model the probability of outcomes of a multi-class experiment, e.g. rolling a die
outcomes=random.multinomial(n=1,pvals=[1/6,1/6,1/6,1/6,1/6,1/6],size=10) #n is number of trials, pvals is the probability of each outcome
print(outcomes)
sns.displot(outcomes)
plt.show()