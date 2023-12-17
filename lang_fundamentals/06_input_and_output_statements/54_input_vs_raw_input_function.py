"""

Python 2.x:
raw_input - we have to do the type casting manually in the code.
input - we don't need to do the type casting and this function itself will take care of it.

Python 3.x:
input - only this function is available, and it will behave the same as raw_input function in python 2.x

"""

"""
while True:
	a = input("Enter an value (x to exit): ")
	print(a, type(a))
	if a == 'x':
		break

x = int(input("Enter the first number   : "))
y = int(input("Enter the second number  : "))
print("The sum is: ", x + y)


print("The sum is: ", int(input("Enter the first number   : ")) + int(input("Enter the second number  : ")))


eno = int(input("Enter the employee number: "))
ename = input("Enter the employee name: ")
esalary = float(input("Enter the employee salary: "))
eaddress = input("Enter employee address: ")
emarried = bool(
	input('Is employee married ? [True|False]: '))  # even if we enter as false, an end result will be like True

print("Please confirm your provided information")
print("Employee Number: ", eno)
print("Employee Name: ", ename)
print("Employee Salary: ", esalary)
print("Employee Address: ", eaddress)
print("Is Employee Married? :", emarried)
"""

a, b, c = [int(x) for x in input("Enter some 3 numbers: ").split()]
print("The sum is: ", a + b + c)

s = input("Enter some 3 numbers: ")
print(s)
l1 = s.split()
print(l1)
l2 = [int(x) for x in l1]
print(l2)
a, b, c = l2
print("The sum is: ", a + b + c)

a, b, c = [float(x) for x in input("Enter some 3 floating point numbers: ").split(',')]
print("The sum is: ", a + b + c)
