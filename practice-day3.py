#WAP to ask the user to enter names of their 3 favorite movies and store them in a list
list = []
mov1 = input("Enter your movie name : ") 
list.append(mov1)
mov2 = input("Enter your movie name : ") 
list.append(mov2)
mov3 = input("Enter your movie name : ") 
list.append(mov3)
#Another method 
mov1 = input("Enter your movie name : ") 
mov2 = input("Enter your movie name : ") 
mov3 = input("Enter your movie name : ") 
list = [mov1,mov2,mov3]
print(list)
#WAP to check if a list contains a palindrome of element 
list = [1,2,3,2,1]
copy_list = list.copy()
copy_list.reverse()
if(list == copy_list):
    print("It is a Palindrome")
else:
    print("Not a Palindrome")
#WAP to count the number of students with the "A" grade in the following tuples
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))
list1 = list(grade)
list1.sort()
print(list1)