# equality operators == and !=

l1 = ['Dog', 'Cat', 'Rat']
l2 = ['Dog', 'Cat', 'Rat']
l3 = ['DOG', 'CAT', 'RAT']
l4 = ['Cat', 'Rat', 'Dog']
print(l1 == l2)
print(l1 == l3)
print(l1 == l4)
print(l1 != l2)
print(l1 != l3)
print(l1 != l4)

print('#' * 80)

# relational operators < <= > >=
l1 = [10, 20, 30, 40]
l2 = [5, 50, 60]
print(l1 < l2)
print(l1 <= l2)
print(l1 > l2)
print(l1 >= l2)

l1 = ['Remo']
l2 = ['Ramba', 'Durga']
print(l1 < l2)
print(l1 <= l2)
print(l1 > l2)
print(l1 >= l2)

print('#' * 80)
# membership operator in and not in
l1 = [10, 20, 30, 40]
print(100 in l1)
print(20 in l1)
print(100 not in l1)
print(20 not in l1)