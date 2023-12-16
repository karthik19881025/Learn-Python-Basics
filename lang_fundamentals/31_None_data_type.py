a = 10
a = None
b = None
c = None
print(a, id(a), type(a))
print(b, id(b), type(b))
print(c, id(c), type(c))


def f1():
    print("Hi")


print(f1(), 'How are you?')