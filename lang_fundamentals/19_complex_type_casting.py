"""

complex() - to covert from other types to int

1. float to complex - possible
2. bool to complex - possible
3. str to complex - possible only if the str contains only float or
                    integral value with base 10 representation.
                    second parameter (imag part) can't be string
4. int to complex - possible (all base representations possible)

"""

print(complex(10))
print(complex(10, 20))
print(complex(0, 20))
print(complex(10.34))
print(complex(10, 20.34))
print(complex(0, 20.23))
print(complex(10.23, 20.34))

print(complex(True))
print(complex(False))
print(complex(True, False))
print(complex(False, True))

print(complex("10.234"))
# print(complex("10", "45.345"))
# print(complex("10", 45.345))
# print(complex(10, "10.234"))