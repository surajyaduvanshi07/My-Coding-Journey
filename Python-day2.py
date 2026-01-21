#STRING 
str1 = "This is a String."
str2 = 'Suraj yadav'
str3 = """Hello World"""
print(str1,str2,str3)

#ESCAPE SEQUENCE CHARACTER(\n)
str = "This is a String.\nwe are creating it in python"
print(str)

#OPERATIONS PERFORM ON STRING
#1 Concatenation (+) add two or more thentwo string
str1 = "Suraj"
str2 = "Yadav"
print(str1 + str2)

#2 Length of String
str = "Hello everyone. My name is Suraj Yadav"
len1 = len(str)
# print(str,len(str))
print("Length of a String : ",len1)

#INDEXING(access character) -> Position started with 0
str = "Surajyadav"
ch = str[0]
print(ch,str[5])

#SLICING (accessing parts of a string)
str = "Suraj yadav" #ending idx is not included
print(str[1:6]) #uraj 
print(str[:4]) #start with 0 and ouput is sura
print(str[1:len(str)]) #is same as str[1: ]




 

