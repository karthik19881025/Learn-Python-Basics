"""

Complex is a python-specific complex data type

a + bj

1. Real Part (a)
2. Imaginary Part (b)
3. j = sqrt(-1)

Real Part - can be represented using decimal / binary / octal / hexa form
Imaginary Part - can be represented decimal form

"""

x = 10 + 50j
print(x, id(x), type(x))
print(x.real, id(x.real), type(x.real))
print(x.imag, id(x.imag), type(x.imag))
y = 20 + 30j

print(x + y)
print(x - y)
print(x * y)
print(x / y)
