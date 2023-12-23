"""

if a loop executes without a break, then else part will get execute in transfer statement
there is no link between continue and else

"""

cart = [10, 20, 30, 40, 50]
for item in cart:
	if item >= 500:
		break
	print(f'Processed Item: {item}')
else:
	print('All items have been processed successfully')
	
print('#' * 80)

cart = [10, 20, 600, 30, 40, 50]
for item in cart:
	if item >= 500:
		break
	print(f'Processed Item: {item}')
else:
	print('All items have been processed successfully')