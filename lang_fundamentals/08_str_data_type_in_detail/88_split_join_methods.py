s = 'Durga Software Solutions'
print(s)
l1 = s.split()  # always returns a list
print(l1)
for x in l1:
	print(x)
	
print('#' * 80)

d = '05-04-2019'
print(d)
l1 = d.split('-')
print(l1)
for x in l1:
	print(x)
	
print('#' * 80)

l1 = ['durga', 'software', 'solutions']
print(l1)
s = ' '.join(l1)
print(s)