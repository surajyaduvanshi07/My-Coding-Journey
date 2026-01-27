"""FILE I/O(INPUT OR OUTPUT) IN PYTHON
python can be used to perform operation on a file(read and write data)
types of all files
1. Text Files : .txt, .docx, .log etc
2. Binary Files : .mp4, .mov, .png, .jpeg etc
"""
"""
OPEN, READ & CLOSE FILE
we have to open a file before reading or writing
file-name(sample.txt,demo.docx)
mode((r: read mode),(w: write mode))
f = open("file_name", "mode")
data = f.read()
f.close()
"""
# f = open("My-Coding-Journey/demo.txt","r")
# # data = f.read()#read complete file
# # data = f.read(5)#read charcter by indexing which you give
# line1 = f.readline() #read line one by one
# print(line1)
# line2 = f.readline()
# print(line2)
# # print(data)
# # print(type(data))
# f.close()
"""
WRITING TO A FILE
"""
# f = open("My-Coding-Journey/demo.txt","w")
# f.write("I want to learn javascript tomorrow. 1234")
# f = open("My-Coding-Journey/demo.txt","a")
# f.write("\nMy name is suraj yadav")
# f.close()
# f = open("My-Coding-Journey/demo.txt","r+") #overwrite 
# f.write("KBC")
# print(f.read())
# f.close()
#with syntax
# with open("My-Coding-Journey/demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("My-Coding-Journey/demo.txt","w") as f:
#     f.write("My new day start")
"""
DELETING A FILE
using the os module
Module(like a code library) is a file written by another programmer that generally has a function we can use
import os
os.remove(filename)
"""
import os
os.remove("My-Coding-Journey/demo.txt")
