# a="Adeel is a good boy"

# print("Adeel" in a)  #check substring
# print(len(a))       #length of string, print number of characters (included spaces also)

# print(a[0:5])  #slicing
# print(a[-8:-4])  #negative indexing, counts from end of string, -1 is last character
# if we write like [:5] it means from start to index 5
# if we write like [2:] it means from index 2 to end of string



# # a=a.lower()  #convert to lowercase
# a=a.replace("Adeel", "Ahmed")  #replace substring
# #print(a)

# a.strip()  #removes extra spaces from start and end of string

# print(a.split(" ")) #splits string into list of substrings based on given separator,mtlb jaha space deke separate krdo
# print(a.find("good"))  #find substring, returns starting index of substring, if not found returns -1
# print(a.capitalize())  #capitalizes first character of string
# print(a.upper())  #convert to uppercase
# print(a.count("o"))  #counts occurrences of substring in string
# print(a.startswith("Adeel"))  #checks if string starts with given substring, returns True



age=25
txt=f"my name is Adeel and i am {age} years old" #f-string for string formatting
math=f"sum of 2x2= {2*2}"
jacket=50
price=f"the price of jacket is {jacket:.2f} dollars"  #formatted string with 2 decimal places
print(txt)
print(math)
print(price)

