l1 = [10, 20, [30, 40]]
print(l1, type(l1), id(l1))
print(l1[0], type(l1[0]))
print(l1[1], type(l1[1]))
print(l1[2], type(l1[2]))
print(l1[2][0], type(l1[2][0]))
print(l1[2][1], type(l1[2][1]))
print('#' * 80)

l2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
for x in l2:
	print(x)
print('#' * 80)
for x in l2:
	for y in x:
		print(y, end=' ')
	print()