num1 = eval(input('Enter the first number   : '))
num2 = eval(input('Enter the second number  : '))

if num1 > num2:
	print(f'Biggest Number is {num1}')
elif num1 == num2:
	print(f'Both are equal')
else:
	print(f'Biggest Number is {num2}')

if num1 < num2:
	print(f'Smallest Number is {num1}')
elif num1 == num2:
	print(f'Both are equal')
else:
	print(f'Smallest Number is {num2}')
	