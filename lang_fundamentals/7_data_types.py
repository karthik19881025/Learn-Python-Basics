"""

1. In python, we don't need to specify the data type of the variables.
2. PVM will automatically consider its data type during run time.
3. Python is a dynamically typed language.

1. int
2. float
3. bool
4. complex
5. str
6. list
7. tuple
8. set
9. frozenset
10. dict
11. bytes
12. bytearray
13. range
14. None

"""

a = 10
b = 10.5
c = True
d = 1 + 2j
e = 'a'
d = 'Karthik'
f = [1, 2, 3, 4, 5, 6, 7, 8]
g = (1, 2, 3, 4, 5, 6, 7, 9)
h = {1, 2, 3, 4, 5}
i = frozenset({1, 2, 3, 4, 5})
j = {'a': 1, 'b': 2, 'c': 3}

print(f"{'variable name': <30}{'id': <30}{'type': <30}{'value': <30}")
print(f"{a:<30}{id(a):<30}{str(type(a)):<30}{a:<30}")
print(f"{b:<30}{id(b):<30}{str(type(b)):<30}{b:<30}")
print(f"{c:<30}{id(c):<30}{str(type(c)):<30}{c:<30}")
print(f"{d:<30}{id(d):<30}{str(type(d)):<30}{d:<30}")
print(f"{e:<30}{id(e):<30}{str(type(e)):<30}{e:<30}")
print(f"{str(f):<30}{id(f):<30}{str(type(f)):<30}{str(f):<30}")
print(f"{str(g):<30}{id(g):<30}{str(type(g)):<30}{str(g):<30}")
print(f"{str(h):<30}{id(h):<30}{str(type(h)):<30}{str(h):<30}")
print(f"{str(i):<30}{id(i):<30}{str(type(i)):<30}{str(i):<30}")
print(f"{str(j):<30}{id(j):<30}{str(type(j)):<30}{str(j):<30}")
