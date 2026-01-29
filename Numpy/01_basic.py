import numpy as np

# arr=np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# multi-dimensial array

# arr2=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(arr2)
# print(type(arr2))
# print((arr2.ndim))    
# print((arr2.shape))  

# print(arr2[0,1,1])
# # print(arr2[0,2,3])

arr3=np.array([1,2,3,4],dtype='f') #create array with specific data type
print(arr3)
print(arr3.dtype)

#convert data type
arr3Convert=arr3.astype('i')
print(arr3Convert)
print(arr3Convert.dtype)