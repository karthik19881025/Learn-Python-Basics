"""

bool() - to covert from other types to int

1. float to bool - possible (0 - False, other than 0 - True)
2. int to bool - possible (0 - False, other than 0 - True)
3. str to bool - possible ('' - False, other than '' - True)
4. complex to bool - possible (0+0j or 0j - false, other than this - True)

"""

print(bool(10))
print(bool(0))

print(bool(10.123))
print(bool(0.0))

print(bool("10"))
print(bool("10.123"))
print(bool("0"))

print(bool(10+10j))
print(bool(0+0j))
print(bool(1+0j))
print(bool(0+1j))
print(bool(0j))

print(bool('True'))
print(bool('False'))
print(bool('yes'))
print(bool('no'))
print(bool(''))