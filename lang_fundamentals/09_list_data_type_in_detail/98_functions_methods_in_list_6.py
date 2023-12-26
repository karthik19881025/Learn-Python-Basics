l1 = [10, 20, 30, 40, 50]
print(l1)
l1.reverse()
print(l1)

print('#' * 80)

l2 = [10, 20, 30, 40, 50]
r = reversed(l2)
print(l2)
print(list(r))
print('#' * 80)
s = 'durga'
print(s)
r = reversed(s)
for x in r:
	print(x, end='')
print()
print(s)
print('#' * 80)
l1 = [34, 23, 12, 32, 100]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l1.sort()
l1= [23, 44, 10, 234, 0]
l2 = sorted(l1)
print(l2)