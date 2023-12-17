f1 = open('file1.txt')
f2 = open('file2.txt')

f3 = open('output.txt', 'w')

for x in f1:
	f3.write(x)
	
f3.write('\n')

for y in f2:
	f3.write(y)
