n = 10
for i in range(n):
	print('* ' * (i + 1) + '  ' * (n + 1))
print('-' * 80)

n = 10
for i in range(n):
	print('* ' * (n - i))
print('-' * 80)

n = 10
for i in range(n):
	print('  ' * (n - i - 1) + '* ' * (i + 1))
print('-' * 80)

n = 10
for i in range(n):
	print('  ' * i + '* ' * (n - i))
print('-' * 80)

n = 10
for i in range(n):
	print(' ' * (n - i - 1) + '* ' * (i + 1))
print('-' * 80)

n = 10
for i in range(n):
	print(' ' * i + '* ' * (n - i))
print('-' * 80)

n = 10
for i in range(n):
	print(' ' * (n - i - 1) + '* ' * (i + 1))
for i in range(n):
	print(' ' * i + '* ' * (n - i))
print('-' * 80)


n = 10
for i in range(n):
	print(' ' * (n - i - 1) + '* ' * (i + 1))
for i in range(1, n):
	print(' ' * i + '* ' * (n - i))
print('-' * 80)


n = 10
for i in range(n):
	print(' ' * (n - i - 1) + '* ' * (i + 1))
for i in range(n-1):
	print(' ' * (i + 1) + '* ' * (n - i - 1))
print('-' * 80)
