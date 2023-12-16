"""

+ - Addition
- - Subtraction
* - Multiplication
/ - Division
% - Modulus
// - Floor (a result is in int or float based on the operand data type)
** - Exponentiation

"""

print(10+3)     # if one of them is a float type, then the result will be in float
print(10+3.3)         # if one of them is a float type, then the result will be in float
print(10-3)     # if one of them is a float type, then the result will be in float
print(10.0-3)     # if one of them is a float type, then the result will be in float
print(10*3)     # if one of them is a float type, then the result will be in float
print(10*3.0)       # if one of them is a float type, then the result will be in float
print(10%3)      # if one of them is a float type, then the result will be in float
print('result', 10%3.5)  # if one of them is a float type, then the result will be in float

print(10/2)     # it will always return a floating type value
print(10/3)     # it will always return a floating type value

print(10//3)    # if both are integer, then the result will be in int
print(10.0//3)  # if one of them is a float type, then the result will be in float

print(10**3)
print(10**3.4)
print(10.0**3)

print('durga' + 'soft')

print('durga' + str(10))

print('durga ' * 3)   # only int is allowed
print(3 * 'karthik ')  # only int is allowed
print(int(3) * 'hello ')
print(True * "asdf ")
print(False * 'Karthik ')  # empty string will be the result

print(10.0//0)