print('Process Started')
for i in range(10):
	if i == 7:
		print('Processing is enough, break statement executed')
		break
	print(i)
print('Process ended')
print('#' * 80)

print('Process started')
cart = [10, 20, 30, 600, 70, 80]
for item in cart:
	if item > 500:
		print(f"To place this order {item}, insurance must be required, we can't proceed further")
		break
	print(f'processing item: {item}')
print('Process ended')
print('#' * 80)

for i in range(3):
	for j in range(3):
		if i == j:
			break
		print(i,j)
print('#' * 80)