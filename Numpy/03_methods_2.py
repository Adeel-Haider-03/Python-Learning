import numpy as np

#3D array iterating
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)


#using nditer()
# for x in np.nditer(arr):
#     print(x)

#iterating with different step size
arr2=np.array([1,2,3,4,5,6,7,8])
# for x in np.nditer(arr2[::2]):     #step size 2
#     print(x)

# #iterating with different data types
# for x in np.nditer(arr2.astype('f')): #float data type
#     print(x)


# using indexes for iterating using ndenumerate()
# for x,idx in np.ndenumerate(arr): #3d array
#     print(idx,x)

# for x,idx in np.ndenumerate(arr2): #1d array
#     print(idx,x)


#sorting arrays
arr3=np.array([[3,2,4],[5,0,1]])
print(np.sort(arr3))  #sorts each row

#sort along the first axis (columns)
print(np.sort(arr3,axis=0))

#sort along the last axis (rows)
print(np.sort(arr3,axis=1))

#sorting alphabetical order
arr4=np.array(['banana','cherry','apple'])
print(np.sort(arr4))