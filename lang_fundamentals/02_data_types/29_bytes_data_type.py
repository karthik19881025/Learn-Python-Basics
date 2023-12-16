"""

bytes:

1. it can hold only between 0 and 255
2. immutable
3. value can be only accessed through indexing and slicing concept

"""

l1 = [10, 20, 30, 40, 50]

b = bytes(l1)
print(b, id(b), type(b))
for x in b:
    print(x)

print(b[1])