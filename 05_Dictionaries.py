#Dictionaries are used to store data values in key:value pairs.
# dict={
#     "name":"Adeel",
#     "age":22,
#     "above_18":True
# }

# print(dict)
# print(dict["name"])
# print(dict.get("age"))
# x=dict.keys()
# print(x)

# dict["color"]="blue" #Adding new key:value pair
# print(dict)
# print(dict.values())


# dict.update({"age":23}) #Updating existing key:value pair
# print(dict)

# dict.pop("above_18") #Removing key:value pair
# print(dict)

# for x in dict:
#     print(x)    #prints keys
#     print(dict[x])  #prints values

# for x, y in dict.items():
#     print(x, y)

# copyDict=dict.copy() #Copying dictionary
# anotherDict={"country":"Pakistan"}
# copyDict=dict(anotherDict)
# print(copyDict)


#--------------------------------------------Nested Dictionaries-------------------------------------------------
myFamily={
    "child1":{
        "name":"Adeel",
        "age":22
    },
    "child2":{
        "name":"Ahmed",
        "age":20
    }
}
# print(myFamily)

# for x, y in myFamily.items():
#     print(x, y)
#     for values in y.items():
#         print(values)

# The fromkeys() method returns a dictionary with the specified keys and the specified value.
x=(0,1,2)
y=("adeel"," ahmed", "ali")

mydict=dict.fromkeys(x,y)  #for all x acting as key y will be the value
print(mydict)