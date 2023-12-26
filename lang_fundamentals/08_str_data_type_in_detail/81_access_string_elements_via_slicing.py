s = 'abcdefghijk'

"""
s[begin(optional):end(optional):step(optional)]
1. get the substring from 'begin' index to the 'end-1' index
2. begin is optional and its default value is 0
3. end is optional and its default value is lens(s)
4. step is optional and its default value is 1
5. step value can be either positive and right.  It cannot have 0.
6. if step value is positive, slicing will be done from left to right (forward direction) with begin to end-1
7. if step value is negative, slicing will be done from right to left (backward direction) with begin to end+1
8. if end value is 0 in forward direction, the result will be always empty.
9. if end value is -1 in backward direction, the result will be always empty.
10. default values for forward direction: begin is 0 and end is len(s)
11. default values for backward direction: begin is -(len(s)+1) and end is -1

variations:
1. s[begin:end]
2. s[begin:]
3. s[:end]
4. s[begin:end:step]
5. s[begin::step]
6. s[:end:step]
7. s[::step]
8. s[::]

"""

for i in range(len(s)):
	print(f'the character present at index {i}  & {i - len(s)} is {s[i]}')
print('#' * 80)
print(f's[:]                    -> {s[:]}')
print(f's[2:7]                  -> {s[2:7]}')
print(f's[:7]                   -> {s[:7]}')
print(f's[2:]                   -> {s[2:]}')
print(f's[::]                   -> {s[::]}')
print(f's[2:7:1]                -> {s[2:7:1]}')
print(f's[2:7:2]                -> {s[2:7:2]}')
print(f's[2:7:3]                -> {s[2:7:3]}')
print(f's[::1]                  -> {s[::1]}')
print(f's[::2]                  -> {s[::2]}')
print(f's[::3]                  -> {s[::3]}')
print('#' * 80)
print(f's[:0]                  -> {s[:0]}')
print(f's[:-(len(s)+1]         -> {s[:-(len(s) + 1)]}')
print('#' * 80)

s = 'abcdefghij'
print(s[1:6:2])  # bdf
print(s[::1])  # abcdefghij
print(s[::-1])  # jihgfedcba   (reverse manner)
print(s[3:7:-1])  # empty string
print(s[7:4:-1])  # hgf (reverse manner)
print(s[0:10000:1])  # abcdefghij
print(s[-4:1:-1])  # gfedc
print(s[-4:1:-2])  # gec
print(s[5:0:1])  # empty string
print(s[0:-10:-1])  # empty string
print(s[0:-11:-1])  # a
print(s[0:0:1])  # empty string
print(s[0:-9:-2])  # empty string
print(s[-5:-9:-2])  # fd
print(s[10:-1:-1])  # empty string
print(s[1000:2:-1])  # jihgfed