#List is a collection which is ordered (anything added will go to last) and changeable(meaning that we can change, add, and remove items in a list after it has been created). Allows duplicate members.It is mutable.


# list=[2,3,4,5,6,7,8,9,10]
# list[2:5]=[20,30,40]   #replace values from index 2 se 5
# print(list)
# print(list[2:5])    #print index 2 se 5 tak

list2=[12,"adeel",True,5.6]
# print(list2)
# print(type(list2))
# print(len(list2)) 

#list2.insert(2,"hello")   #insert at index 2

#list2.append("world")    #add at last
#print(list2)

#combineList=list.extend(list2)  #will print none because list.extend(list2) add items of list2 to list at last of list and return nothing

#correctway
#list.extend(list2)
#print(list)   #extend list1 by adding list2 items at last of list1


#list3=["apple","banana","cherry"]
# list3.remove("banana")   #remove banana from list3


#list3.pop(1)   #remove item at index 1
#del list3[0]   #remove item at index 0

# list3.clear()   #remove all items from list3
# print(list3)

# for x in list3:
#     print(x)

# for i in range(len(list3)):
#     print(list3[i])


#----------------------------------------#list comprehension----------------------------------#
# The Syntax
#  [expression for item in iterable if condition == True]


print([x for x in range(10)])   #list comprehension with range {0-10 value print karega}

list4=['adeel','awais','zeeshan','noor','ahmed']
print([name for name in list4])


# newlist=[x for x in list4 if 'r' in x]      #will only print noor

newlist=[x.upper() for x in list4 if 'r' in x]   #will print NOOR in uppercase

print(newlist)
print([x for x in list4 if x!="awais"])  #will print all names except awais

print([x if x == "adeel" else "Baba" for x in list4])  #if name is adeel print adeel otherwise print baba


#----------------------------------------#Sorting#----------------------------------#

list5=[100,20,300,40,500,60]

# list5.sort()  #sort in ascending order
# list5.sort(reverse=True) #sort in descending order
# print(list5)

# list6=["banana","apple","cherry","mango"]
# list6.sort()  #sort in alphabetical order
list6=["banana","apple","Cherry","mango"]
# list6.sort()                                     #will sort Cherry first due to capital alphabet
list6.sort(key=str.lower)                        #will sort in alphabetical order ignoring case sensitivity
print(list6)


#customize function---------You can also customize your own function by using the keyword argument key = function.

def myfunc(n):
    return n%3==0

list5.sort(key=myfunc,reverse=True)
print(list5)   #will sort even numbers first then odd numbers


#----------------------------------------#Copying a list#----------------------------------#
list7=[1,2,3,4,5]
#list8=list7            #this will not create a copy of list7 rather it will create a reference of list7
# list8=list7.copy()   #this will create a copy of list7
# list8=list(list7)        #this will also create a copy of list7
list8=list7[:]      #this will also create a copy of list7
print(list8)

#----------------------------------------#Joining two lists#----------------------------------#
list9=[10,20,30]
list10=[40,50,60]
# list11=list9+list10   #joining two lists
# for x in list10:
#     list9.append(x)     #joining two lists using loop
# print(list9)
list9.extend(list10)   #joining two lists using extend() method
print(list9)