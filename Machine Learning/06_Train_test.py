import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2) # to make the random numbers predictable

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()