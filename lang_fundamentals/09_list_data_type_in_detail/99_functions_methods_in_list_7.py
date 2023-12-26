l1 = [10, 20, 30, 40]
l2 = l1[::]
print(l1, id(l1))
print(l2, id(l2))
l1.append(50)
print(l1, id(l1))
print(l2, id(l2))
print('#' * 80)

l1 = [10, 20, 30, 40]
l2 = l1.copy()
print(l1, id(l1))
print(l2, id(l2))
l1.append(50)
print(l1, id(l1))
print(l2, id(l2))

print('#' * 80)

l1 = [10, 20, 30, 40]
l2 = l1
print(l1, id(l1))
print(l2, id(l2))
l1.append(50)
print(l1, id(l1))
print(l2, id(l2))

