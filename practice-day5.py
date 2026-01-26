#WAF to print the length of a list(list os the parameter)
cities = ["Delhi","Gurgaon","Rohtak","Uttar pardesh","Punjab"]
anime = ["onepiece","Demonslayer","Baki","Aot","Dundadun"]
def print_len(list):
    print(len(list))
    # return len(list)
print_len(cities)
print_len(anime)
#WAF to print the elements of a list in a single
cities = ["Delhi","Gurgaon","Rohtak","Uttar pardesh","Punjab"]
anime = ["onepiece","Demonslayer","Baki","Aot","Dundadun"]
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)
print_list(anime)
#WAF to find the factorial of n(n is the parameter)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)
#WAF to convert USD to INR
USD = int(input("Enter the Numbers of $ : "))
def cal_convert(USD):
    INR = USD * 100
    print(f"{USD} USD = {INR} Rupees")
cal_convert(USD)

n = int(input("Enter the Number"))
def cal(n):
    if(n%2 == 0):
        print(n,"is Even")
    else:
        print(n,"is odd")
cal(n)
#Simple Greeting Function
"""
Write a function greet() that prints:
"Hello, welcome to Python!"
"""
def greet():
    print("Hello, Welcome to Python!")
greet()
"""
Function with One Parameter
Write a function square(num) that returns the square of a number."""
def square(num):
    sq = num *num
    print(sq)
square(2)
def square(num):
    return num*num
print(square(4))
"""
Even or Odd
Create a function is_even(n) that returns True if the
 number is even, otherwise False.
"""
n = int(input("Enter the Number : "))
def is_even(n):
    if(n%2 == 0):
        return True
    else:
        return False
print(is_even(n))
"""
Find Larger Number
Write a function max_of_two(a, b) that returns the greater number.
"""
def max_of_two(a,b):
    if(a>b):
        print(a," is greatest")
    else:
        print(b," is greatest")
max_of_two(3,2)
max_of_two(73737,46363)
max_of_two(10,9)
max_of_two(6,9)
"""
Simple Calculator – Addition
Write a function add(a, b) that returns the sum of two numbers.
"""
def add(a,b):
    return a + b
print(add(4,5))
print(add(6,8))
vowels = "aaaiiiooouuunnneeeii"
text = input("Enter you letter: ")
def count_vowels(text):
    if text in vowels:
        return True
    else:
        return False
print(count_vowels(text))
vowels = "aaaiiiooouuunnneeeii"
def count_vowels():
    count = 0
    for i in vowels:
        if i in "aeiou":
            count += 1
    
    print(count)
print(count_vowels())
def count_vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1
    return count

print(count_vowels("aaaiiiooouuunnneeeii"))
"""
Reverse a String
Write a function reverse_string(s) that returns the
 reversed version of the string.
"""
str1 = input("Enter the String: ")
def reverse_string(str1):
    reversed_str1 = str1[::-1]
    return reversed_str1
print(reverse_string(str1))
"""
Sum of List Elements
Write a function sum_list(numbers) that returns the sum of
 all elements in a list
"""
numbers = [1,2,3,4,5,6,7,8,9]
def sum_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(sum_list(numbers))

