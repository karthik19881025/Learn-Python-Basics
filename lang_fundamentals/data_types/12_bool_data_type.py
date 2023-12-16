"""

bool data type is used to represent either true or false

"""

a = True
b = False

print(a, type(a), id(a))
print(b, type(b), id(b))

print(int(a), id(int(a)))
print(int(b), id(int(b)))

a = 10
b = 20
c = 10 > 20
print(c)

print(True + True)
print(True - False)
print(True + False)
print(False + False)
print(False - True)
print(False + True)