"""

reserved words or keywords

1. it contains only alphabetic characters
2. except the following three, all contain only lower case characters
	True, False & None
3. do-while & switch is not there in python
4. int, float, etc. - data types are not part of keywords.

"""
import keyword
print("Total Number of Keyword: ", len(keyword.kwlist))
count = 0
for keyword in keyword.kwlist:
	count += 1
	print(keyword, end=', ')
	if count % 15 == 0:
		print()
	