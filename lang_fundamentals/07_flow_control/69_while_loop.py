i = 1
while i <= 10:
	print("Hello, Welcome to while loop")
	i += 1
	
print('#' * 80)

i = 1
while i <= 10:
	print(i)
	i += 1

print('#' * 80)


i = 1
while i <= 20:
	if i % 3 == 0:
		print(i)
	i += 1

print('#' * 80)

n = int(input('Enter a number: '))
total = 0
i = 1
while i <= n:
	total += i;
	i += 1
print(f'Total: {total}')

print('#' * 80)

name = ''
while name != 'sunny':
	name = input("Enter your fav actress: ")
print('Thanks for confirmation!')

print('#' * 80)


i = 1
while True:
	if i == 1000:
		break;
	print(i)
	i += 1
print('#' * 80)
