"""

List:

1. insertion order is preserved
2. can allow to hold duplicate objects (elements)
3. represented within [ ] and values should be separated by ,
4. heterogeneous objects are allowed
5. mutable
6. can be accessed or modified via indexing and slicing concept
7. growable in nature (we can add or remove any elements)

append - to add a new element in a list
remove - to remove an element from a list

"""

a = [10, 'durga', 30, True, 50.45, 50, 40, 30, 10+123j, 10]

print(a, id(a), type(a))

a = []
a.append(10)
a.append('durga')
a.append(30)
a.append(True)
a.append(50.345)
print(a)
a.remove(30)
print(a)

a = [10, 20, 30, 40, 50]
a[0] = 7777
print(a)

print(a[2:6])