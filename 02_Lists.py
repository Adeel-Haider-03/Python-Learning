#List is a collection which is ordered (anything added will go to last) and changeable(meaning that we can change, add, and remove items in a list after it has been created). Allows duplicate members.It is mutable.


list=[2,3,4,5,6,7,8,9,10]
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