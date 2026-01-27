"""Create a new file "practice.txt" using python. Add the following data in it
Hi everyone
we are learning File I/O
using Java
i like programming in Java
"""
# with open("My-Coding-Journey/practice.txt","w") as f:
#     f.write("Hey everyone\nwe are learning File I/O\nusing Java\ni like programming in Java")

# with open("My-Coding-Journey/practice.txt","r") as f:
#     data = f.read()
#     print(data)
"""
Write a function that replace all occurrences of "Java" with "python" in above file
"""
# with open("My-Coding-Journey/practice.txt","r") as f:
#     data  = f.read()
# new_data = data.replace("Java","Python")
# print(new_data)
# with open("My-Coding-Journey/practice.txt","w") as f:
#     f.write(new_data)
"""
search if word learning exists in the file or not
"""
word = "learning"
with open("My-Coding-Journey/practice.txt","r") as f:
     data  = f.read()

     if(data.find(word) != -1):
        print("Found")
     else:
         print("NOt found")
