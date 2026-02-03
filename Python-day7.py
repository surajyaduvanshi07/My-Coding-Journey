"""
OOP'S (Object Oriented pragramming System) in Python
To map with real world scenarios, we started using objects in code
This is called Object Oriented programming.
"""
"""
Class and Object in python
Class is a blueprint for creating objects.
#creating class
class Student:
    name = "Suraj yadav"
#creating object (instance)
s1 = Student()
print(s1.name)
"""
class Student:
    name = "Suraj"
s1 = Student()
print(s1.name)
class Car:
    color = "blue"
    brand = "BMW"
car1 = Car()
print(car1.color)
print(car1.brand)
"""
__init__ Function
Constructor 
All classes have a function called __init__(), which is always executed when the class is being initiated
#creating class
class Student:
    def __init__(self, fullname):
    self.name = fullname

#creating object
s1 = Student("Suraj")
print(s1.name)

*The self paratmeter is a reference to the current
instance of the class, and is used to access variables
that belongs to the class
"""
class Student:
    #Default constructors
    def __init__(self):
        print("enter anythings")

    #paramterize constructors
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("Creating new student in Database:")
    

s1 = Student("Suraj",98)
print(s1.name,s1.marks)
s2 = Student("Arjun",89)
print(s2.name,"marks = ",s2.marks)
"""
Methods
Methods are function that belong to objects
"""
class Student:
    def __init__(self,name):
        self.name = name

    def hello (self):
        print("Hello",self.name)

s1 = Student("Suraj")
s1.hello()
    