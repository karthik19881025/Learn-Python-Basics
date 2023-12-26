l1 = []
for i in range(1,101):
	if i % 10 == 0:
		l1.append(i)
		
print(l1, id(l1))

l1.append(110)
l1.insert(5, 120)
print(l1, id(l1))
l1.insert(100, 140)
l1.insert(-100, -100)
print(l1)