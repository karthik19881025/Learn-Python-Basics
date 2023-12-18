
def func1():
	num1 = eval(input('Enter the first number   : '))
	num2 = eval(input('Enter the second number  : '))
	num3 = eval(input('Enter the third number  : '))
	
	if num1 > num2 and num1 > num3:
		print(f'Biggest Number is {num1}')
	elif num2 > num3:
		print(f'Biggest Number is {num2}')
	else:
		print(f'Biggest Number is {num3}')


n = eval(input('Enter any number: '))
if 1 <= n <= 100:
	print(f'The number {n} is in-between 1 and 100')
else:
	print(f'The number {n} is not in-between 1 and 100')
	