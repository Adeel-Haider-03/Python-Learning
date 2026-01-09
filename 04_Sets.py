# set1={'adeel','ali','umer'}
# print(set1)                # in set it will not maintain the order, it can print in any order



# set2={'adeel','ali','umer','adeel'}  # set do not allow duplicate values
# print(set2)                # it will print only one 'adeel'

# #we cannot change items in set but we can add or remove items
# #set2[0]='hassan'          # this will give error because we cannot change items in set
# set2.add('hassan')         # adding an item to set
# print(set2)

# #we can add multiple items (set,list,dictionaries) to set using update() method
# set2.update({'ahmed','sami'})   # adding multiple items to set
# list=['zain','bilal']
# set2.update(list)               # adding items from list to set
# print(set2)

# #removing items from set
# set2.remove('ali')              # removing an item from set
# set2.discard('umer')            # removing an item from set
# set2.pop()                      # removing a random item from set
# print(set2)


#joining of sets
setA={'adeel','ali','umer'}
setB={'hassan','ahmed','sami'}
setC={1,2,3,4,5}
setD={2,4,6,8,10}

# setD=setA.union(setB)          # joining two sets using union() method
# print(setD)

# setD= setA | setC                # joining two sets using '|' operator
# print(setD)

# setE= setC.intersection(setD)    # getting common items from two sets using intersection() method
# print(setE)

# setE= setC & setD                  # getting common items from two sets using '&' operator
# print(setE)

# setE= setC.difference(setD)     # getting items that are in setC but not in setD using difference() method
# print(setE)

# setE=setC-setD               # getting items that are in setC but not in setD using '-' operator
# print(setE)

# setE= setC.symmetric_difference(setD)  # getting items that are in either setC or setD but not in both using symmetric_difference() method
# print(setE)

# setE= setC ^ setD                      # getting items that are in either setC or setD but not in both using '^' operator
# print(setE)

# setE=setD.isdisjoint(setC)    # checking if two sets have no items in common using isdisjoint() method
# print(setE)                    # it will return True if no common items, otherwise False

setF={1,2,3}
# setE=setF.issubset(setC)        # checking if setF is subset of setC using issubset() method
# print(setE)                     # it will return True if setF is subset of setC, otherwise False

setE=setC.issuperset(setF)      # checking if setC is superset of setF using issuperset() method
print(setE)                     # it will return True if setC is superset of setF, otherwise False