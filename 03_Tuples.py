#Tuple items are ordered, unchangeable, and allow duplicate values.it is immuatable.

tuple1=(1,2,3,4,5,6,7,8,9,10)
#tuple1[3]=20   #will give error because tuple is immutable, while in list we can change values using assignment operator


#tuple2=('adeel')
#print(type(tuple2))   #will print string because single value tuple is not considered as tuple
# tuple2=('adeel',)   #correct way to define single value tuple
# print(type(tuple2))   #will print tuple


#to update Tuple, we have to convert it into list, update it and again convert it into tuple, same for removal of items from tuple
tuple3=(11,12,13)
list1=list(tuple3)   #convert tuple into list
list1[0]=22
tuple3=tuple(list1)   #convert list back into tuple
print(tuple3)  #will print (22,12,13)

#----------------------------------------#Tuple Unpacking---same as array destructing in Javascript----------------------------------#
#Tuple unpacking is used to assign values from a tuple to a tuple of variables.

fruits=("apple","banana","cherry")
# (green,yellow,red)=fruits
# print(green,yellow,red)   #will print apple banana cherry

# (green,_,red)=fruits   #if we want to ignore any value we can use underscore _ as variable
(green, *yellow)=fruits   #if we want to assign multiple values to a single variable we can use * before variable name,yellow will have banana and cherry both values in list form
#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
toys=("car","bike","cycle","plane","boat")
(boys,*girls,adult)=toys
print(girls)   #will print ['bike', 'cycle', 'plane']

print(yellow)

#multiply values in tuple
tuple4=('a','b','c')
print(tuple4*2)   #will print ('a', 'b', 'c', 'a', 'b', 'c')

#concatenate tuples
tuple5=tuple4+fruits
print(tuple5)   #will print ('a', 'b', 'c', 'apple', 'banana', 'cherry')

tuple6=(1,2,2,2,4,3,4,5)
print(tuple6.count(2))   #will print 3 because 2 is present 3 times in tuple6

print(tuple6.index(2))   #will print 1 because first occurrence of 2 is at index 1