import numpy
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# x=numpy.array([True, True, True, False, False, True, True, False, False, False]) # actual values

# y=numpy.array([True, True, False, False, False, True, False, False, False, False]) # predicted values

# confusionMatrix=metrics.confusion_matrix(x, y)
# print(confusionMatrix)
# cm_display=metrics.ConfusionMatrixDisplay(confusion_matrix=confusionMatrix, display_labels=[False, True])
# cm_display.plot()
# plt.show()


#logistic regression

X=numpy.array([3.78, 2.45, 1.23, 4.56, 3.21, 2.34, 5.67, 4.32, 3.45, 2.56]) # actual values
Y=numpy.array([1 if val>4 else 0 for val in X]) # predicted values

# print(y)

regr=LogisticRegression()
# print(x)
# print(x.reshape(-1, 1)) # we are reshaping the x array to make it a 2D array with one column and as many rows as needed. This is because the logistic regression model expects the input to be a 2D array.
X=X.reshape(-1,1)
regr.fit(X,Y)

predict=regr.predict(X)

print(predict)

cm=metrics.confusion_matrix(Y,predict)
cm_display=metrics.ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=[True,False])
cm_display.plot()
plt.show()