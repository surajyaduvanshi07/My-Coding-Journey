#LOOP IN PYTHON (IT IS USES TO REPEAT INSTRUCTION)
# WHILE LOOP (SYNTAX)
#while (condition):
       #statement
# while True :
#     print("hello")
# count = 1 #iterator
# while count <= 5:
#     print("Hello")
#     count += 1
# print(count)
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# print("Loop Ended")
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print("Loop Ended")

#BREAK AND CONTINUE STATEMENTS
#BREAK : used to terminate the loop when encountered
# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# print("end of loop")

#CONTINUE : terminates execution in the current iteration and continues execution of the loop with the next iteration
# i = 0
# while i <=5:
#     if(i == 3):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1
# i = 1
# while i <= 10:
#     if (i%2 == 0):
#         i += 1
#         continue
#     print("odd number",i)
#     i += 1
#FOR LOOP IN PYTHON
#For loop are used for sequential traversal. for traversing list, string, tuples etc
nums = [1,2,3,5,6,7]
for val in nums:
    print(val)
else:
    print("end")