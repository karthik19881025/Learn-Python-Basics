"""

Identity Operator:
1. is
2. is not

Membership Operator:
1. in
2. not in

"""

a = 10
b = 20
print(a is b)

l1 = [10, 20, 30]
l2 = [10, 20, 30]
print(l1 is l2)

a = 10
b = a
print(a is b)

l1 = [10, 20, 30]
l2 = l1
print(l1 is l2)

print(10 in l1)
print(100 in l2)

s = "hello learning python is very easy"
print('h' in s)
print('d' in s)
print('d' not in s)
print('python' in s)
