"""
and
or
not

0 - False
Non-0 - True
empty string, empty list, empty tuple, empty set, empty dict - False

1. x and y
if x is evaluated as false, then return x
if x is evaluated as true, then return y

2. x or y
if x is evaluated as true, then return x
if x is evaluated as false, then return y

3. x not y
result is always return as boolean

"""

print(0 and 20)
print(10 and 20)
print('' and 'soft')
print('durga' and 'soft')


print('#' * 80)

print(10 or 20)
print(0 or 20)
print('durga' or 'soft')
print('' or 'soft')

print('#' * 80)

print(not 20)
print(not 0)
print(not 1)
print(not 'soft')
print(not '')