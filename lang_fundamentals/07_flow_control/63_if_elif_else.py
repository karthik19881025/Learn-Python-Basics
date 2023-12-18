# if

name = input('enter your name: ')
if name == 'karthik':
	print('Hello', name, 'Good Evening.')
print('How are you?')

# if-else
name = input('enter your name: ')
if name == 'karthik':
	print(f'Hello {name}, Good Evening.')
else:
	print(f'Hello Guest, Good Evening.')
print('How are you?')

# if-elif-else
brand = input('enter you favourite brand: ')
if brand == 'KF':
	print('It is children\'s brand')
elif brand == 'KO':
	print('It is too light')
elif brand == 'RC':
	print('It is not that much kick')
elif brand == 'FO':
	print('Buy one GET one FREE')
else:
	print('Other brands are not recommended')
