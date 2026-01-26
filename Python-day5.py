#FUNCTION IN PYTHON
"""
Block of statements that perform a specific task
def func_name(param1,param2..): (function definition)
    #some work
    return val
    func_name(arg1,arg2..) (function call) arg-> arguments
    """
# def calc_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum
# calc_sum(5,6)
# calc_sum(4,9)
# calc_sum(5,8)
#Function definition
# def calc_sum(a,b): #parameter
#     return a + b
# #Function call
# sum = calc_sum(1,2) #arguments
# print(sum)
# def print_hello():
#     print("Hello")

# print_hello()
# print_hello()
# print_hello()
# print_hello()
#average of 3 numbers
# def average(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)
#     return avg

# average(2,4,6)
#TYPES OF FUNCTIONS
"""Two types of function
1. Built-in Function (print(), le(), type(), range())
2. User defined Functions"""
#Default Parameters
#Assigning a default value to parameter, which is used when no argument is passed
# def cal_prod(a = 1,b = 1):
#     print(a * b)
#     return a * b
# cal_prod()

"""RECURSION
when a function calls itself repeatedly
#print n to 1 backwards
"""
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    

show(5)
