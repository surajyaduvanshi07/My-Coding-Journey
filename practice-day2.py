#WAP to input user's first name and print its length
name = input("Enter your name :")
print(len(name))
#WAP to find the occurrence of "$" in a string
a = "I am $$$ and my value is 1$"
print(a.count("$"))
##WAP that converts a string to uppercase and lower case
a = "i am suraj"
print(a.upper())
b = "MY NAME IS SURAJ"
print(b.lower())
#WAP that return the first character of a string
a = "suraj yadav"
print(a[0])
#WAP that checks if a substring exists inside a string
a = "my name is suraj"
print(a.endswith("aj"))
print(a.replace(" ","_"))
#WAP that join two string with a hyphen(-)
str1 = "suraj"
str2 = "yadav"
print(str1+"-"+str2)
#WAP to check if a number entered by the user is odd or even
num = int(input("Enter your number : "))
if(num%2 == 0):
    print("Number is even")
else:
    print("Number is odd")
#WAP to find the greatest of 3 numbers entered by the user
a = int(input("Enter the value : "))
b = int(input("Enter the value : "))
c = int(input("Enter the value : "))
if(a > b and a > c):
    print("A is greatest number")
elif(b > c and b > a):
    print("B is greatest number")
else:
    print("C is greatest number")
#WAP to check if a number is a mulltiple of 7 or not
num = int(input("Enter your number: "))
if(num%7 == 0):
    print("It is a multiple of 7")
else:
    print("Not a multiple of 7")
#WAP to check if a character is a vowel or consonant
ch = input("Enter your character: ")
if(ch in 'aeiou'):
    print("your character is vowel: ",ch)
else:
    print("Your character is consonent: ")
#WAP to check if a number is divisible by 5 and 11
num = int(input("enter your number: "))
if(num%5 == 0 and num%11 == 0):
    print("yes")
else:
    print("no")
#WAP to create a calculator using conditional statements
a = int(input("Enter your Number: "))
b = int(input("Enter your Number: "))
op = input("Enter your Symbol: ")
if(op == '+'):
    print("Addition of a and b is: ",a + b)
elif(op == '-'):
    print("Subtraction of a and b is: ",a - b)
elif(op == '*'):
    print("Multiplication of a and b is: ",a * b)
elif(op == '/'):
    print("Division of a and b is: ",a / b)
else:
    print("As always your choice is wrong")
#WAP to check leap year 
year = int(input("enter your year: "))
if(year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("leap year")
else:
    print("not leap year")