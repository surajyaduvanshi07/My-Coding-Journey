#DICTIONARY IN PYTHON (are used to store data value in key:value pairs)
#they are unordered, mutable and don't allow duplicate keys
dict = {
        "name": "Suraj",
        "Age": 19,
        "learning": "coding",
        "subject": ["python","java","c++"],
        "topics": ("dictionary","set"),
}
dict["surname"] = "yadav"
print(dict,type(dict))
dict["name"] = "SURAJ"
print(dict["name"])
null_dict = {}
null_dict["name"] = "Surajyadav"
print(null_dict)
#NESTED DICTIONARY
student = {
        "name" : "Suraj",
        "subjects": {
            "phy" : 97,
            "chem" : 98,
            "math" : 95,
        }
}
print(student)
print(student["subjects"]["chem"])
#DICTIONARY METHODS
print(student.keys()) #return all keys (not inlcude nested keys)
print(list(student.keys()))
print(len(list(student.keys())))
print(len(student)) #Total number of keys
print(student.values()) #return all values
print(student.items()) #return all (key,val) pairs as tuples
print(student.get("name")) #returns the key according to value
student.update({"city" : "Rohtak"}) #inserts the specified items to the dictionary
print(student.update({"city" : "Rohtak"})) #return none value
print(student)
#SET IN PYTHON (immutable)
nums = {1,2,3,3,3,3,3,3,3,3,4,5}
print(nums,type(nums),len(nums))
nums = {}#empty dictionary
collections = set() # used empty set; syntax
print(type(nums),type(collections))
#SET METHODS
set = {1,2,3,4,5,6,7} #set -> mutable, elements -> immutable
set.add(8)#adds an elements
print(set) 
set.remove(2) #removes an elements
print(set)
# set.clear() #empties the set
# print(set)
set.pop() #remove randomly
print(set)
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
