"""

bytearray:

1. it can hold only between 0 and 255
2. mutable
3. value can be accessed & modified through indexing and slicing concept

"""

l1 = [10, 20, 30, 40, 50]

b = bytearray(l1)

print(b, id(b), type(b))

print(b[0])
print(b[-1])

b[3] = 255

for i in b:
    print(i)