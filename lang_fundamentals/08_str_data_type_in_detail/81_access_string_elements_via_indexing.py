s = 'durga'

print(s[0], s[1], s[2], s[3], s[4])
print(s[-1], s[-2], s[-3], s[-4], s[-5])

print('#' * 80)

s = input('Enter some string: ')

print(f'size of the entered string is: {len(s)}')

for i in range(len(s)):
	print(f'the character present at index {i}  & {i-len(s)} is {s[i]}')

