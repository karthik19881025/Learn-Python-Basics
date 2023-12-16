"""

Tuple:

1. insertion order is preserved
2. call allow to hold duplicate objects (elements)
3. represented within ( ) and values should be separated by ,
4. heterogeneous objects are allowed
5. immutable
6. can be only accessed via indexing and slicing concept
7. Non-growable in nature (we cannot add or remove any elements)
8. read-only version of list

"""

t = (10, 20, 30, 'durga', True, 10, 20)
print(t, id(t), type(t))
print(t[-1])
print(t[2:6])

t = ()
print(type(t))
t = (10)
print(t, type(t))
t = (10, )
print(t, type(t))