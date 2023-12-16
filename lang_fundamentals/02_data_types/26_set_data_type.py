"""

Set:

1. insertion order is not preserved
2. call allow to hold duplicate objects (elements) but we can use only the distinct values while we process it
3. represented within { } and values should be separated by ,
4. heterogeneous objects are allowed
5. mutable
6. can not be accessed via indexing and slicing concept
7. growable in nature (we can add or remove any elements)

"""

s = {10, 20, 30, 'durga', True, 10, 20}
print(s, id(s), type(s))

s.add(100)
print(s, id(s), type(s))

s.remove(10)
print(s, id(s), type(s))

##  important point  ##
s = {}
print(s, id(s), type(s))

s = set()
print(s, id(s), type(s))
