from types import FunctionType

s = 'ABCDEFGFHBA'

print(s.find('B'))  # 1 -> index of the first occurrence for the given string (left to right)
print(s.find('z'))  # -1

print(s.find('B', 3, 8))  # -1
print(s.find('G', 3, 8))  # 6

print(s.rfind('B'))  # 9 index of the first occurrence for the given string (right to left)
print(s.rfind('z'))  # -1

print(s.rfind('B', 3, 8))  # -1
print(s.rfind('F', 3, 8))  # 7

print(s.index('E'))  # 4
print(s.index('G', 3, 8))  # 6

print(s.rindex('E'))  # 4
print(s.rindex('G', 3, 8))  # 6

mail = 'karthik.mksamy@gmail.com'
try:
	i = mail.index('@')
	print(f"mail id contains @ symbol which is mandatory at index {i}")
except ValueError:
	print("mail id doesn't contains @ symbol")