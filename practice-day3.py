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
#WAP to store the following word meanings in a python dictionary
python_dictionary = {
        "cat" : "a small animal",
        "table" : ("a piece of furniture","list of facts and figures")
}
print(python_dictionary)
subjects = {"Pyhton","Java","C++","Javascript","C"}
print(len(subjects))
#WAP tp enter marks of 3 subjects from the user and store them in a dictionary Start with an empty dictionary and add one by one use subject name as key and marks as value
dict = {}
marks1 = int(input("Enter your phy marks : "))
dict.update({"Phy" : marks1})
marks2 = int(input("Enter your chem marks : "))
dict.update({"chem" : marks2})
marks3 = int(input("Enter your math marks : "))
dict.update({"math" : marks3})
print(dict)
#WAP to figure out a way to store 9 and 9.0 as separate values in the set
values = {9,"9.0"}
print(values)
#WAP t find the sum of all elements in a list
list = [1,2,3,4,5]
print(list[0]+list[1]+list[2]+list[3]+list[4])
