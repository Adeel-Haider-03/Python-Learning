import numpy as np
from numpy import random

# x=random.rand()  #random float number between 0.0 to 1.0 if we don't pass any argument
# x=random.rand(5)    #array of 5 random float numbers between 0.0 to 1.0 if we pass an integer argument
# print(x)
# x=random.rand()*100  #random float number between 0.0 to 100.0
# print(f'{x:.2f}')  #prints the float number rounded to 2 decimal places

# y=random.randint(5,100) #random integer between 5 to 100
# print(y) 

# arr=random.rand(5)     #if we pass an integer argument, it will generate an array of that size with random float numbers between 0.0 to 1.0
# arr=random.rand(3,4)   #if we pass a tuple as an argument, it will generate a multi-dimensional array with the specified shape
# arr=random.rand(2,3,4) #we can also pass the size of the array as a tuple for multi-dimensional arrays      
# print(arr)

# #arr1=random.randint(5,100,10) #print random integers between 5 to 100, and the size of the array is 10
# arr1=random.randint(5,100,size=(10)) #we can also pass the size of the array as a tuple
# print(arr1)

# arr2=random.randint(5,100,size=(3,4)) #we can also pass the size of the array as a tuple for multi-dimensional arrays
# print(arr2)

# arr3=random.randint(5,100,size=(2,3,4)) #we can also pass the size of the array as a tuple for multi-dimensional arrays
# print(arr3)


#choice() method is used to generate a random sample from a given 1-D array

array=np.array([10,20,30,40,50])

x=random.choice(array)  #randomly selects one element from the array
print(x)
 
y=random.choice(array,size=(2,5)) # radnomly selects elements only from given array to create 2,5 array
print(y) #array of 2 rows and 5 columns with only elements from [10,20,30,40,50]

z=random.choice(array,size=(2,3,3)) #randomly selects elements only from given array to create 2,5 array without replacement
print(z) #array of 2 rows and 5 columns with only elements from [10,20,30,40,50] without replacement