#WAP to input 2 numbers and print their sum 
num1 = int(input("Enter your value : "))
num2 = int(input("Enter your value : "))
sum = num1 + num2
print("Sum of two number is : ",sum)
#WAP to input side of a square and print its area
side = int(input("Enter the value : "))
area = side * side
print("Area of a square is : ",area)
#WAP to input 2 flaoting point number and print its average
a = float(input("Enter your value : "))
b = float(input("Enter your value : "))
avg = (a + b)/2
print("Average of 2 flaoting number is : ",avg)
#WAP to input 2 int numbers, a and b.print true if a is greater then or equal to b. if not print false
a = int(input("Enter the value : "))
b = int(input("Enter the value : "))
print(a >= b)
#WAP to take user name as input and print a greeting
name = input("Enter your name : ")
print("Welcome", name)
#WAP to find the area of circle
r = int(input("Enter your value : "))
pi = 3.14
area = pi*r*r
print("Area of a circle is: ",area)
#WAP which convert celsius to fahrenheit
cel = int(input("Enter your number : "))
fah = (cel)*9/5 + 32
print("Converstion : ",fah)
#WAP to swap two number without using third variable
a = int(input("Enter your value : "))
b = int(input("Enter your value : "))
a,b = b,a
print("After Swaping")
print("a = ",a)
print("b = ",b)