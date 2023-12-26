s = (5 * 'ABC') + 'A'
print(s)
print(len(s))
i = s.find('ABC')
print(i)
i = s.find('ABC', 3, 10)
print(i)
i = s.find('ABC', 6, 10)
print(i)
i = s.find('ABC', 9, 10)
print(i)

subs = input('Enter substring to search: ')
i = s.find(subs)
if i == -1:
	print('Substring not found')
counter = 0
while i != -1:
	print(f'{subs} present at index: {i}')
	i = s.find(subs, i + len(subs), len(s))
	counter += 1
print(f'total no. of occurrences : {counter}')
