"""
1. By using index
2. By using slice operator

for k in list.__dict__:
	print(k)
"""

l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
print(l1[0])
print(l1[-1])
# print(l1[100])
print('#' * 80)
print(l1[0:11:2])
print(l1[2:7])
print(l1[2:7:2])
print(l1[4::2])
print(l1[8:2:-2])
print(l1[4:100])
print(l1[4:0:2])
print(l1[::1])
print(l1[::-1])
print('#' * 80)

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(l1):
	print(l1[i])
	i += 1
print('#' * 80)

for x in l1:
	print(x)
print('#' * 80)

for x in l1:
	if x % 2 == 0:
		print(x)
print('#' * 80)

l1 = [10, 20, 30, 40, 50, 60]
i = 0
while i < len(l1):
	print(f'The element present at +ve index {i} and at -ve index {i-len(l1)} is: {l1[i]}')
	i += 1