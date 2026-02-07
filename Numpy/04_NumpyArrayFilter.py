import numpy as np

#filtering arrays
arr=np.array([1,2,3,4,5,6,7,8,9])

#WE HAVE TO CREATE A BOOLEAN ARRAY THAT WILL BE USED AS A MASK TO FILTER THE ELEMENTS, only 
#only the elements corresponding to True in the boolean array will be included in the new array

x=[True,False,True,False,True,False,True,False,True]

newArr=arr[x]
print(newArr)  #prints [1 3 5 7 9]


#filtering using conditions
filterArr=arr>5
print(filterArr)  #prints [False False False False False  True  True  True  True]
newArr2=arr[filterArr]
print(newArr2)  #prints [6 7 8 9]


a=arr[arr%2==0] # filter even numbers, we can pass condition directly inside the square brackets
print(a)  #prints [2 4 6 8]

