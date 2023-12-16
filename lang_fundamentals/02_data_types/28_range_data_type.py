"""

range:

1. indexing & slicing can be applied
2. immutable
3. range(end_value), range(start_value, end_value), range(start_value, end_value, step_value)

"""
r = range(11)

for x in r:
    print(x, end=' ')

print()
r = range(50)

for x in r:
    print(x, end=' ')

print()
r = range(1, 11)

for x in r:
    print(x, end=' ')

print()
r = range(0, 100, 2)

for x in r:
    print(x, end=' ')

print()
r1 = range(10, 20, 2)
for x in r1:
    print(x, end=' ')


print()
r1 = range(20, 1, -2)
for x in r1:
    print(x, end=' ')

print()
print('#' * 100)

r = range(10, 21)
print(r[0])
print(r[-1])
print('#' * 100)
for i in r[4:8]:
    print(i)

for i in r:
    print(i)
