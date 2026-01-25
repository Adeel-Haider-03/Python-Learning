import os


#file=open('text.txt', 'x')  #creates a new file

# file=open('text.txt', 'w')  #opens the file in write mode
#file=open('text.txt', 'a')  #opens the file in append mode

# file.write("Hello World!\nWelcome to File Handling in Python.")
# file.close()



with open("text.txt", 'r') as file:  # we do not need to close the file manually with 'with' statement
    print(file.read())  #reads the entire file
    #print(file.readlines())  #reads all lines and returns a list of lines

os.remove('text.txt')  #deletes the file