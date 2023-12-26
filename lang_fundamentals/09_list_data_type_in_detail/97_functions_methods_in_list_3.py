l1 = [10, 20, 30, 40, 50]
l2 = [60, 70, 80, 90, 100]
l1.extend(l2)
print(l1)
l2.append(l1)
print(l2)
l1.extend('ABC')
print(l1)