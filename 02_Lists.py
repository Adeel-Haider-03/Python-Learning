#List is a collection which is ordered (anything added will go to last) and changeable(meaning that we can change, add, and remove items in a list after it has been created). Allows duplicate members.It is mutable.


list=[2,3,4,5,6,7,8,9,10]
list[2:5]=[20,30,40]   #ereplace values from index 2 se 5
print(list)
# print(list[2:5])    #print index 2 se 5 tak

list2=[12,"adeel",True,5.6]
# print(list2)
# print(type(list2))
# print(len(list2)) 

list2.insert(2,"hello")   #insert at index 2
print(list2)