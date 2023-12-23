"""

prime numbers - only two factors either 1 or that number itself

"""

# x = int(input('Enter any number: '))
x = 101
if x <= 1:
	print(f'{x} is not a prime number')
else:
	is_prime = True
	for i in range (2, x):
		if x % i == 0:
			is_prime = False
			break
	if is_prime:
		print(f'{x} is a prime number')
	else:
		print(f'{x} is not a prime number')
		
print('#' * 80)

y = 2
while y <= x:
	is_prime = True
	for i in range(2, (y // 2) + 1):
		if y % i == 0:
			is_prime = False
			break
	if is_prime:
		print(y)
	y += 1

print('#' * 80)

n = 10
y = 2
counter = 0
while True:
	is_prime = True
	for i in range(2, (y // 2) + 1):
		if y % i == 0:
			is_prime = False
			break
	if is_prime:
		counter += 1
		print(y)
	if counter == n:
		break
	y += 1

print('#' * 80)

