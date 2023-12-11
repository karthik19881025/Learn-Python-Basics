"""

strings support both positive and negative indexing

positive indexing: 0 to n-1
negative indexing: -1 to -n

when we try to access the index which is not available, then
PVM throws 'string index out of range' error

"""
s = 'karthik'
print(s[0], s[1], s[2], s[3], s[4], s[5], s[6])
print(s[-8], s[-7], s[-6], s[-5], s[-4], s[-3], s[-2], s[-1])