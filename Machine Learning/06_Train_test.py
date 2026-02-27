import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2) # to make the random numbers predictable

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# plt.scatter(x, y)
# plt.show()


train_x=x[:80] # the first 80 values of x are used for training
train_y=y[:80]

test_x=x[80:] # the last 20 values of x are used for testing
test_y=y[80:]

# plt.scatter(train_x, train_y)
# plt.show()
# plt.scatter(test_x, test_y)
# plt.show()

myModel=numpy.poly1d(numpy.polyfit(train_x, train_y, 4)) # we are trying to fit a 4th degree polynomial to the data
myLine=numpy.linspace(0, 6, 100) # we are creating a line from 0 to 6 with 100 points
plt.scatter(train_x, train_y)
plt.plot(myLine, myModel(myLine)) # we are plotting the line and the model
plt.show()

r2score=r2_score(train_y, myModel(train_x)) # we are calculating the r2 score for the training data
print(r2score) #result=0.79 which shows that the model is a good fit for the training data

r2=r2_score(test_y, myModel(test_x)) # we are calculating the r2 score for the testing data
print(r2)  #result=0.8 which shows that the model is a good fit for the testing data as well, and it is not overfitting.

predicted=myModel(test_x)
plt.scatter(test_x, predicted)
plt.show()
 

print(myModel(2.525))

