for i in range(10):
	if i % 2 == 0:
		continue
	print(i)

print('Process started')
cart = [10, 1000, 20, 30, 600, 70, 80]
for item in cart:
	if item > 500:
		print(
			f"To place this order {item}, insurance must be required, we can't proceed further on processing this item")
		continue
	print(f'processing item: {item}')
print('Process ended')
print('#' * 80)

t = (10, 20, 0, 5, 0, 30)
for x in t:
	if x == 0:
		print(f'Hello Stupid, how can we divide 100 with {x}')
		continue
	else:
		print(f'100/{x} = {100 / x}')
print('#' * 80)

for i in range(3):
	for j in range(3):
		if i == j:
			continue
		print(i, j)
print('#' * 80)
