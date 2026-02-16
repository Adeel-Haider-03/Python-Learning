#ufuncs is a function that operates on the ndarray elementwise. It is a fast and efficient way to perform operations on arrays.
import numpy as np

a=[1,2,3,4]
b=[5,6,7,8]
#add
x=np.add(a,b)
print(x)

#subtract
# y=np.subtract(a,b)
# print(y)

#without ufuncs, we can use zip to perform elementwise operations 
#zip is a built-in function that takes two or more iterables and returns an iterator that produces tuples of the elements in the iterables.

c=[]
for i,j in zip(a,b):
    c.append(i+j)
print(c)
