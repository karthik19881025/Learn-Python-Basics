s = 'durga '
s = 'durga' + 'soft '
print(s * 10)

s = 'durga software solutions'
print('durga' in s)
print('tech' in s)
print('durga' not in s)
print('tech' not in s)

print('ramba' < 'ramya')
for i in 'ramba':
	print(f'{i} unicode value is: {ord(i)}')
	
for i in 'ramya':
	print(f'{i} unicode value is: {ord(i)}')
	
s1 = 'remya'
s2 = 'Remya'
if s1 == s2:
	print(f'both the string are equal')
elif s1 < s2:
	print(f'string 1 is less than s2')
else:
	print(f'string 1 is greater than s2')
	
	