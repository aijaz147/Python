# python data structures and boolean
    #  boolean, Boolean & logical operators, Comparasion Operators, Dictionaries, Tuples, Sets 

# boolean variables

myStr = "Hello World"
print(myStr.isalnum())

print(myStr.endswith("r"))

# boolean and logical operators

# True and False - true
# True and False - false
# True or False - true
# True or Ture - true


str1 = "Hello"
str2 = "World"

print(str1.isalnum() and str2.isalnum())

# lists - list is collection of items and mutable

n = ["John", "Tonny", "Kevin", "Martin", "Josh"]

print(type(n))
print(len(n))
n.append("Hey")
print(n)
print(n[1:4])
n.append(["Johnny", "Chester"])
print(n)
n.insert(3, "Mount")

print(n)

print(len(n))

n.extend([7,8])
print(n)

print(n.index("Hey"))
n.pop(6)
print(n)
