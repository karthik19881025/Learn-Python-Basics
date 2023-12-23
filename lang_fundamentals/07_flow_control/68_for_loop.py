s = 'Karthikeyan Muthukumarasamy'

i = 0

for x in s:
	print(f'The character present at {i} is: {x} ')
	i += 1
	
print('#' * 80)

for i in range(10):
	print('Hello, Welcome to Python For Loop')
	
print('#' * 80)

for i in range(1, 11):
	print('Hello, Welcome to Python For Loop')

print('#' * 80)

for i in range(21):
	if i % 2 != 0:
		print(i)

print('#' * 80)

for i in range(1, 21, 2):
	print(i)

print('#' * 80)

for i in range(10, 0, -1):
	print(i)

print('#' * 80)

l1 = eval(input('Enter the list of numbers separated by comma: '))
print(l1, type(l1))
total = 0
for i in l1:
	total += i
print(total)

print('#' * 80)

l1 = eval(input('Enter the list of numbers separated by comma: '))
print(l1, type(l1))
print(sum(l1))

l1 = list(input('Enter the list of numbers separated by comma: ').split(','))
print(l1, type(l1))
total = 0
for i in l1:
	total += int(i)
else:
	print('Hi')
print(total)

