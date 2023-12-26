from string import *

s = 'ABABABABA'
print(s)
s1 = s.replace('A', 'C')
print(s1)

print('#' * 80)

s = 'Durga Software Solutions'
print(s, s.count(' '))
s1 = s.replace(' ', '')
print(s1)
print(len(s) - len(s1))

print('#' * 80)

s = 'Learning    Python is      Very Easy'
print(s, s.count(' '))
s1 = s.replace(' ', '')
print(s1)
print(len(s) - len(s1))
