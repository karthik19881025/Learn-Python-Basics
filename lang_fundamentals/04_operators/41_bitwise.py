"""

& - bitwise and; if both are bits are 1, then the result is 1 otherwise 0
| - bitwise or; if at-least 1 bit is 1, then the result is 1 otherwise 0
^ - bitwise x-or; if both the bits are different, then the result is 1 otherwise 0
~ - bitwise complement operator;
	a. the most significant bit acts as sign bit
	b. 0 means +ve number
	c. 1 means -ve number
	d. +ve numbers will be represented directly in the memory
	e. -ve numbers will be represented in 2's complement form
	f. 1's complement -> 0 will be replaced with 1 and 1 will be replaced with 0
	d. 2's complement -> 1's complement + 1
<< - bitwise left-shift operator; right side will be filled with 0s
>> - bitwise right-shift operator: left side will be filled with 0s

these operators can be applied only for int and bool

"""

print(4 & 5)  # 100 and 101 => 100
print(4 | 5)  # 100 or 101 => 101
print(4 ^ 5)  # 100 ^ 101 => 001

print('#' * 80)

print(~5)
print(~(-5))

print('#' * 80)

x = 10
print(x, bin(x))
x = x << 2
print(x, bin(x))
x = 10
x = x >> 2
print(x, bin(x))
x = -10
x = x >> 2
print(x, bin(x))

print('#' * 80)

print(True & False)
print(True | False)
print(True ^ False)
print(~True)
print(~False)
print(True >> 10)
print(False << 10)