# sets
    # a set is unordered collection data type that is iterable, mutable and has no duplicate elements.

mySet = {"John", "Tom", "Kevin"}
mySet1 = {"Kevin", "Yen", "Martin"}

print(type(mySet))
# print(mySet)

mySet.add("100")
# print(mySet)

# there is no indexing in sets

mySet.add("Tom")

print(mySet)

mySet1.difference(mySet)
print(mySet)


# dictionary

myDic = {
    "name": "Tommy",
    "age": 24,
    "city": "Tokyo"
}

print(myDic["city"])

myDic["email"] = "xyz@gmail.com"
print(myDic)

# tuples

myTup = ("Hey", "Hello")
print(myTup)

# we can not change the element but we can change the tuple
