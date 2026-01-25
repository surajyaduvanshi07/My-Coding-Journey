# LOOP IN PYTHON (IT IS USES TO REPEAT INSTRUCTION)
# WHILE LOOP (SYNTAX)
# while (condition):
#        statement
# while True :
#     print("hello")
count = 1 #iterator
while count <= 5: #iteration (how my time loop work)
    print("Hello")
    count += 1
print(count)
i = 1
while i <= 5:
    print(i)
    i += 1

print("Loop Ended")
i = 5
while i >= 1:
    print(i)
    i -= 1
print("Loop Ended")

# BREAK AND CONTINUE STATEMENTS
# BREAK : used to terminate the loop when encountered
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of loop")

# CONTINUE : terminates execution in the current iteration and continues execution of the loop with the next iteration
i = 0
while i <=5:
    if(i == 3):
        i += 1
        continue #skip
    print(i)
    i += 1
i = 1
while i <= 10:
    if (i%2 == 0):
        i += 1
        continue
    print("odd number",i)
    i += 1
#FOR LOOP IN PYTHON
#For loop are used for sequential traversal. for traversing list, string, tuples etc
#LIST
num = [1,2,3,4,5,6,7]
veggies = ["potato","tomato","ladyfinger","cucumber"]
# for el in num:
for val in veggies:
    print(val)
#TUPLE
tup = (1,2,3,4,5,6,7)
for val in tup:
    print(val)
#STRING
name = "Surajyadav"
for ch in name:
    print(ch)
else:
    print("End")
#RANGE FUNCTION (range())
#Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by default) and stop before a specified number
#Syntax-> range(start?,stop,step-size?) "?" means optional value
print(range(5))
seq = range(10)
for i in range(10): #seq: range(stop)
    print(i)
for i in range(2,10): #range(start, stop)
    print(i)
for i in range(2,10,2): #range(start,stop,step)
    print(i)
#if we want to print even number from 1 to 10
for i in range(1,11):
    if(i%2 == 0):
        print(i)
for i in range(2,101,2):
    print(i)
#PASS STATEMENT IN PYTHON
#pas is a null statement that does nothing. it is used as a placeholder for future code
for i in range(5):
    pass
print("some useful work")