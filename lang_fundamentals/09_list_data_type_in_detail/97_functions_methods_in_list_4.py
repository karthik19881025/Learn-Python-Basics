l1 = [10, 20, 30, 40, 50]
l1 = l1 * 2
print(l1)
l1.remove(10)
print(l1)
print('#' * 80)

l2 = [1, 2, 3, 4, 5, 6, 7, 8]
print('Before removal: ', l2)
x = int(input('Enter an element to be removed: '))
if x in l2:
	l2.remove(x)
	print('After removal: ', l2)
else:
	print(f'{x} not present in the list')
print('#' * 80)


l3 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8]
print('Before removal: ', l3)
x = int(input('Enter an element to be removed: '))
while True:
	if x in l3:
		l3.remove(x)
	else:
		break
print('After removal: ', l3)