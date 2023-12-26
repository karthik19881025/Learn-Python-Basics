l1 = [10, 20, 20, 30, 40, 50]
print(len(l1))  # size of a list

print(l1.count(20))
print(l1.count(100))

print(l1.index(20))
print(l1.index(20, 2))
# print(l1.index(100))  # we will get error

l1 = [1, 2, 2, 2, 3, 3]
x = eval(input('Enter element to find: '))
if x in l1:
	print(f'{x} present at index {l1.index(x)}')
else:
	print(f'{x} not present in the list')
	
	