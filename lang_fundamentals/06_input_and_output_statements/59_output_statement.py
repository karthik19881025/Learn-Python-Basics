print()  # \n
print('hello world')
print('hello' + 'world')
print('hello' * 3)
print('hello', 'world', 'have', 'a', 'good', 'day')

print('hello', 'world', 'karthik', sep=":")
print('hello', 'world', 'karthik', sep=">")

l1 = ['hello', 'world', 'karthik!']

counter = 0
for i in l1:
	if counter == len(l1) - 1:
		print(i, end='')
	else:
		print(i, end=' ')
	counter += 1

print()
print(10, 20, 30, sep=':', end='***')
print(40, 50, 60, sep=':')
print(70, 80, sep='**', end='$$')
print(90, 100)


print('durga' + 'software')
print('durga', 'software')
