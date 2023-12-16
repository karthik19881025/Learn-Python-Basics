"""

Dict:

1. insertion order is preserved
2. call allow to hold key value pair info only.  Duplicate Keys are allowed.  But we
can always access the last vale that we added for that key can be retrieved.
3. represented within {} and key:value should be separated by ,
4. heterogeneous objects (key and value) are allowed
5. mutable
6. can not be accessed via indexing and slicing concept
7. growable in nature (we can add or remove any elements)

"""

d = {100: "Karthik", 200: 'durga', 200: 'ravi'}
print(d, id(d), type(d))

d[1] = 'ravi'
d[100] = 'karthik'
d[200] = 'divya'


print(d, id(d), type(d))
