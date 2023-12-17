from sys import argv


print(type(argv))
print('Total no. of cmd line arguments      : ', len(argv) - 1)
print('List of cmd line arguments           : ', argv)
print('The cmd line arguments one by one    : ')

# print('name of the file : ', argv[0]) # python file's absolute path
# print('first parameter   : ', argv[1]) # first parameter
# print('second parameter : ', argv[2]) # second parameter
# print('third parameter  : ', argv[3])  # third parameter


for p in argv:
	print(p)

result = 0
for v in argv[1:]:
	result += int(v)
	
print("The sum is: ", result)
