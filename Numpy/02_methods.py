import numpy as np

# arr=np.array([1,2,3,4,5])


#copy vs view

# #copy
# x=arr.copy()  #create a copy of arr
# arr[0]=99
# print(arr)  #modified arr
# print(x)    #x remains unchanged

#view
# y=arr.view()  #create a view of arr
# arr[1]=88
# print(arr)  #modified arr
# print(y)    #y is also modified since it's a view of arr


#concatenate

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# # concateArr=np.concatenate((arr1,arr2))
# concateArr=np.concatenate((arr1,arr2),axis=1)
# print(concateArr)

# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[5,6],[7,8]])
# # concateArr=np.concatenate((arr1,arr2))  #default axis=0
# concateArr=np.concatenate((arr1,arr2),axis=1)  #concatenate along columns
# print(concateArr)



#stack
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# # concatArr=np.stack((arr1,arr2)) 
# # concatArr=np.vstack((arr1,arr2)) #vertical stack
# # concatArr=np.hstack((arr1,arr2)) #horizontal stack
# concatArr=np.dstack((arr1,arr2)) #depth stack

# print(concatArr)

#spliting
# newArr=np.array_split(concatArr,3)  #split arr into 3 parts

#hsplit, vsplit, dsplit
# newArr=np.hsplit(concatArr,2)  #horizontal split into 2
arr4=np.array([[1,2,3,4],[5,6,7,8]])
# newArr=np.vsplit(arr4,2)  #vertical split into 2
# newArr=np.dsplit(concatArr,2)  #depth split into 2
# print(newArr)  #list of arrays


#search
# arr=np.array([1,2,3,4,5,6,7,8])
# x=np.where(arr%2==0)  #return indices where condition is true
# print(x)    #output (indices of even numbers)

# arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
# y=np.where(arr2%2==0)  #return indices where condition is true
# print(y)    #output (row indices, column indices of even numbers)

#searchsorted
arr3=np.array([1,3,5,6,7])
print(np.searchsorted(arr3,5))  #output 2
print(np.searchsorted(arr3,7,side='left')) 
print(np.searchsorted(arr3,7,side='right')) #output 5 because 7 is at index 4, so right side is index 5
index=np.searchsorted(arr3,2)  #find index where 6 should be inserted to maintain order
print(index)  #output 1