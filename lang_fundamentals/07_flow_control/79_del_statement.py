"""

del is used to delete the variable name which frees the object for garbage collector to clean it up.

"""

x = 10
del x
# print(x)

s1 = 'durga'
s2 = s1
s3 = s2

del s1
print(s3)
print(s2)
# print(s1)
del s2, s3
# print(s3)
# print(s2)

s = 'durga'
# del s[0]
print(s)