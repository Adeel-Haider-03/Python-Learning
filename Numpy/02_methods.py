import numpy as np

arr=np.array([1,2,3,4,5])


#copy vs view

# #copy
# x=arr.copy()  #create a copy of arr
# arr[0]=99
# print(arr)  #modified arr
# print(x)    #x remains unchanged

#view
y=arr.view()  #create a view of arr
arr[1]=88
print(arr)  #modified arr
print(y)    #y is also modified since it's a view of arr