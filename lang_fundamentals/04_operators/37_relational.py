"""

>
<
>=
<=

"""

print(10 < 20)
print(10 > 20)
print(10 >= 20)
print(10 <= 20)

print('#' * 80)

print(10.10 < 20)
print(10 > 20.10)
print(10.20 >= 20)
print(10 <= 20.24)

print('#' * 80)

a = 'a'
b = 'b'

print(ord('a'))
print(chr(97))
print(ord('b'))
print(chr(98))

print(a > b)
print(a < b)


print('#' * 80)

a = 'window'
b = 'sunny'
print(a, b)
print('a < b', a < b)
print('a <= b', a <= b)
print('a > b', a > b)
print('a >= b', a >= b)

print('#' * 80)

a = 'sunny'
b = 'sunny'
print(a, b)
print('a < b', a < b)
print('a <= b', a <= b)
print('a > b', a > b)
print('a >= b', a >= b)


print('#' * 80)

a = 'sunny'
b = 'Sunny'
print(a, b)
print('a < b', a < b)
print('a <= b', a <= b)
print('a > b', a > b)
print('a >= b', a >= b)

print('#' * 80)

print(True > False)
print(True >= False)
print(True < False)
print(True <= False)

print('#' * 80)
print(str(10) < 'durga')
print('#' * 80)
a = 10
b = 20

if a > b:
	print('a is greater than b')
else:
	print('a is not greater than b')