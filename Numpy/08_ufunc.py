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


#let's create a custom ufunc to perform elementwise addition
def myAdd(x,y):
    return x+y

#we can use np.frompyfunc to create a ufunc from a python function
customAdd=np.frompyfunc(myAdd,2,1)  #(func name, no of arguments, no of returns)

y=customAdd(a,b)
print(y)

#we can also use the built-in ufuncs to perform elementwise operations on arrays

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])

plus= np.add(arr1,arr2)
print(plus)

minus=np.subtract(arr1,arr2)
print(minus)

div=np.divide(arr1,arr2)
print(div)

mod=np.mod(arr1,arr2)
print(mod)

#The divmod() function return both the quotient and the mod. The return value is two arrays,
#  the first array contains the quotient and second array contains the mod.
divandmod=np.divmod(arr1,arr2)
print(divandmod)

arr3=np.array([-1,-4,-5])
absol=np.absolute(arr3)
print(absol)


# it has many more ufunc
#  for sum, commulative sum,
#  product,
#  log,
#  LCM, GCD,
#  sin cos,
#  hyperbolic,
#  set operations
#  and many others