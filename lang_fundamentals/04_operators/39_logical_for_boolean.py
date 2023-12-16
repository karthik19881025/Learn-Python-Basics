"""

and - if both the expressions are true, then return true otherwise false
or - if one of the expressions is true, then return true otherwise false
not - if not false, then return true and if not true, then return false

"""
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('#' * 80)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('#' * 80)

username = input('Enter the user name   : ')
password = input('Enter the password    : ')

if username == 'durga' and password == 'sunny':
	print("Valid User")
else:
	print("Invalid User")

