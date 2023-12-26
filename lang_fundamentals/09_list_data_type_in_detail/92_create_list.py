"""

1. insertion order is preserved
2. can allow to hold duplicate objects (elements)
3. represented within [ ] and values should be separated by ','
4. heterogeneous objects are allowed
5. mutable
6. can be accessed or modified via indexing and slicing concept
7. growable in nature (we can add or remove any elements)

"""

l1 = [10, 'durga', 10]
print(l1, type(l1), id(l1))

l1 = []
print(l1, type(l1), id(l1))

# l1 = eval(input('Enter a list: '))
# print(l1, type(l1), id(l1))

l1 = list('durga')
print(l1, type(l1), id(l1))

l1 = list(range(0,10, 2))
print(l1, type(l1), id(l1))

s = 'Learning Python is very easy'
l1 = s.split()
print(l1, type(l1), id(l1))

