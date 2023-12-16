"""

Mutable -> Changeable

Immutable -> Non-Changeable
1. All fundamental data types are immutable
2. Once we create an object under these fundamental data types,
   then we cannot make any changes in that object.
   If we are trying to perform any changes, a new object will be created.

"""

x = 2
print(x, hex(id(x)), end=' ')
x = x + 1
print(x, hex(id(x)))

x = 5
y = x
print(x, hex(id(x)), y, hex(id(y)))
y = y + 1
print(x, hex(id(x)), y, hex(id(y)))

print('#' * 80)

a = 10.234
b = 10.234
c = 10.234

print('a:', a, hex(id(a)))
print('b:', b, hex(id(b)))
print('c:', c, hex(id(c)))

print('#' * 80)

a = 'durgasoft'
b = 'durgasoft'
print(a is b)
print('a:', a, hex(id(a)))
print('b:', b, hex(id(b)))

print('#' * 80)

l1 = [10, 20, 30]
print(l1, id(l1))
l1[0] = 7777
print(l1, id(l1))

l1 = [10, 20, 30]
print(l1, id(l1))
l2 = [10, 20, 30]
print(l2, id(l2))
print(l1 is l2)

l2 = l1
print(l1 is l2)
print(l2, id(l2))

print('hi how are you')