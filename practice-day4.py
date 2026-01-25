#WHILE LOOP PRACTICE QUESTION
#WAP to print number 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1
#WAP to print number 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1
#WAP to print the multiplication table of a number n
n = int(input("Enter your number : "))
i = n
while i <= n*10:
    print(i)
    i += n
#Another Method
n = int(input("Enter the Number : "))
i = 1
while i <= 10:
    print(f"Table is {n*i}")
    i += 1
#WAP to print the element of the following list using a loop
nums = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
#WAP to search for a number x in this tuple using loop
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx",i)
        break
    else:
        print("Finding...")
    i += 1
print("End of loop")
#WAP to print odd number from 1 to 20
i = 1
while i <= 20:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1
#WAP to print even number from 1 to 20
i = 1
while i <= 20:
    if(i%2 != 0):
        i += 1
        continue
    print(f"Even Number is : {i}")
    i += 1
#WAP to print the multiplication Table of 5
Table = 5
print("Table of 5")
i = 1
while i <= 10:
    print(Table*i)
    i += 1
#WAP to find the sum of numbers 1 to 100
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print("Sum of 1 to 100 : ",total)
#WAP to print each character of a string "Python" using a loop
a = "Python"
i = 0
while i < len(a):
    print(a[i])
    i += 1
#WAP to count how many numbers from 1-50 are divisible by 3
count = 0
i = 1
while i <= 50:
    if(i%3 == 0):
        count += 1
    i += 1
print("Number which are divisible by 3: ",count)
#WAP to print all number from 1 to 50 that are divisible by 5 and 7
i = 1
while i <= 50:
    if((i%5 == 0) and (i%7 == 0)):
        print(i)
    i += 1
#WAP to print the sum of even numbers between 1 and 100
sum = 0
i = 1
while i <= 100:
    if(i%2 == 0):
        sum += i
    i += 1
print("Sum is : ",sum)
#WAP to find the sum of all elements in a list
list = [1,2,3,4,5]
sum = 0
i = 0
while i < len(list):
    sum += list[i]
    i += 1
print("Sum of list is : ",sum)
#WAP to count how many even number are in the list
num = [1,2,3,4,5,6,7,8,9,10]
count = 0
i = 0
while i < len(num):
    if(num[i]%2 == 0):
        count += 1
    i += 1
print("Total even Number in a list is ",count)
#WAP to remove all negative number in a list
num = [1,2,3,4,-1,-2,-3,-4]
new_num = []
i = 0
while i < len(num):
    if(num[i] >= 0):
        new_num.append(num[i])
        print(num[i])
    i += 1
print(new_num)

#Question practice using For loop

#WAP to print the elements of the following list using a loop
number = [1,4,9,16,25,36,49,64,81,100]
for val in number:
    print(val)
#WAP to search for a number x in this tuple using loop
number = (1,4,9,16,25,36,49,64,81,100,49)
x = 49
idx = 0
for el in number:
    if(el == x):
        print("Number found",idx)
        # break
    idx += 1

#RANGE practice question
#print number from 1 to 100 
for i in range(1,101,1):
    print(i)
#print number from 100 to 1
for i in range(100,0,-1):
    print(i)
#print the multiplication table of a number n
n = int(input("Enter the Number: "))
# for i in range(n,n*11,n):
#     print(i)
for i in range(1,11):
    print(i*n)
#WAP to find the sum of first n natural number(using while)
n = int(input("Enter the Number: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum of N number is : ",total)
#ANOTHER METHOD
n =int(input("Enter the Number : "))
total = 0
for i in range(1,n+1):
    total += i
print("Sum of N natural number is : ",total)
#WAP to find the factorial of first n natural numbers(using for)
n =int(input("Enter the Number : "))
fact = 1
for i in range(1,n+1,):
    fact *= i
print(fact)
#while loop 
n =int(input("Enter the Number : "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial of N number is: ",fact)
#Print numbers from 1 to 10 using a loop
for i in range(1,11):
    print(i)
#Print numbers from 10 to 1 (reverse order)
for i in range(10,0,-1):
    print(i)
#Print even numbers from 1 to 20
for i in range(1,21):
    if(i%2 == 0):
        print(i)
for i in range(2,21,2):
    print(i)
# Print odd numbers from 1 to 20
for i in range(1,20,2):
    print(i)
#Print the multiplication table of 5
num = 5
for i in range(1,11):
    print(num*i)
#Find the sum of numbers from 1 to 100
total = 0
for i in range(1,101):
    total += i
print("Sum of number from 1 to 100 : ",total)
#Print each character of a string "Python" using a loop
name = "Python"
for i in name:
    print(i)
#Count how many numbers from 1–50 are divisible by 3
count = 0
for i in range(1,51):
    if(i%3 == 0):
        count += 1
print("Total number is : ",count)
#Print all numbers from 1 to 50 that are divisible by 5 and 7
count = 0
for i in range(1,51):
    if((i%5 == 0)and(i%7 == 0)):
        print(i)
#Count the number of digits in a given number
a = int(input("Enter the number : "))
count = 0
while a > 0:
    a = a // 10
    count += 1
print("Total digits:",count)
#Reverse a number using a loop (e.g., 123 → 321)
