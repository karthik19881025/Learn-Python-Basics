"""

Frozenset:

1. insertion order is not preserved
2. call allow to hold duplicate objects (elements) but we can use only the distinct values while we process it
3. represented within { } and values should be separated by ,
4. heterogeneous objects are allowed
5. immutable
6. can not be accessed via indexing and slicing concept
7. non-growable in nature (we cannot add or remove any elements)

"""

s = {10, 20, 30, 'durga', True, 10, 20}
print(s, id(s), type(s))

fs = frozenset(s)
print(fs, id(fs), type(fs))

fs = frozenset()
print(fs, id(fs), type(fs))
