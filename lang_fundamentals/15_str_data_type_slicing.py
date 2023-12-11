"""

slicing syntax

s[begin:end]

1. returns the substring from begin index to end-1 index.
2. if the 'begin' value is not specified,
   then the 'begin' index is 0
3. if the 'end' value is not specified,
   then the 'end' index is considered as the last index of that string.
4. if the 'being' and 'end' value are not specified,
   then the 'begin' index is 0 and the 'end' index is considered
   as the last index of that string.


"""
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[3:9])
print(s[:9])
print(s[3:])
print(s[:])
print(s[3:1000])

s = 'durga'
output = s[0].upper() + s[1:]
print(output)

s = 'durga'
output = s[:len(s)-1] + s[-1].upper()
print(output)

s = 'durga'
output = s[0].upper() + s[1:len(s)-1] + s[-1].upper()
print(output)