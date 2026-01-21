#STRING 
str1 = "This is a String."
str2 = 'Suraj yadav'
str3 = """Hello World"""
print(str1,str2,str3)

# #ESCAPE SEQUENCE CHARACTER(\n)
str = "This is a String.\nwe are creating it in python"
print(str)

# #OPERATIONS PERFORM ON STRING
#1 Concatenation (+) add two or more thentwo string
str1 = "Suraj"
str2 = "Yadav"
print(str1 + str2)

# #2 Length of String
str = "Hello everyone. My name is Suraj Yadav"
len1 = len(str)
# print(str,len(str))
print("Length of a String : ",len1)

# #INDEXING(access character) -> Position started with 0
str = "Surajyadav"
ch = str[0]
print(ch,str[5])

# #SLICING (accessing parts of a string)
str = "Suraj yadav" #ending idx is not included
print(str[1:6]) #uraj 
print(str[:4]) #start with 0 and ouput is sura
print(str[1:len(str)]) #is same as str[1: ]

# #FUNCTION PERFROM ON STRING
str = "i am studying python."
print(str.endswith("on.")) #return true if string ends with substr
# str = str.capitalize()
print(str.capitalize()) #capitalize 1st char
print(str)
print(str.replace("python","java")) #replace all occurrences of old str.replace("u","o")
print(str.find("u")) #return 1st index of 1st occurrer or if not exist then output is -1
print(str.count("t"))

#CONDITIONAL STATEMENTS(IF-ELIF-ELSE)
age = 21
if(age >= 18):
    print("Can vote and apply for license") #indentation(proper spacing to separate a block of code)
ligth = "green"
if(ligth == "red"):
    print("Stop")
elif(ligth == "green"):
    print("Go")
elif(ligth == "yellow"):
    print("Wait")

num = 5
if(num > 2):
    print("greater than 2")
if(num > 3):
    print("greater than 3")
elif(num > 3):
    print("greater than 3")
#GRADE STUDENT BASED MARKS PROGRAM
marks = int(input("Enter your grade : "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90): grade = "B"
elif(marks >= 70 and marks < 80): grade = "C"
elif(marks < 70): grade = "D"
print(grade)

#NESTING (IF-ELSE)
age = 95
if(age >= 18):
        if(age >=80):
              print("cannot vote")
        else:
              print("can drive")
else:
      print("cannot drive")
