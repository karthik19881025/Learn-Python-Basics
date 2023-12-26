l1 = list(range(1, 11))
print(l1)
print('#' * 80)

l2 = []
for i in range(1, 11):
	l2.append(i)
print(l2)
print('#' * 80)

l3 = [x for x in range(1, 11)]
print(l3)
l3 = [x ** 2 for x in range(1, 11)]
print(l3)
print('#' * 80)

l4 = [x for x in range(1, 101) if x % 10 == 0]
print(l4)
print('#' * 80)

l5 = [10, 20, 30, 40]
l6 = [30, 40, 50, 60]
l7 = [x for x in l5 if x not in l6]
print(l7)
l8 = [x for x in l5 if x in l6]
print(l8)
print('#' * 80)

l9 = ['Balaiah', 'Nag', 'Venky', 'Chiru']
l10 = [x[0] for x in l9]
print(l10)
print('#' * 80)

s = 'the quick brown fox jumps over the lazy dog'
words = s.split()
print(words)
l11 = [[word.upper(), len(word)] for word in words]
print(l11)
print('#' * 80)

vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter any string to search for vowels: ')
result = []
for ch in word:
	if ch in vowels and ch not in result:
		result.append(ch)
print(result)
print('The number of unique vowels: ', len(result))
result = []
for ch in vowels:
	if ch in word and ch not in result:
		result.append(ch)
print(result)
print('The number of unique vowels: ', len(result))
print('#' * 80)

l12 = [ch for ch in vowels if ch in word]
print(l12)
print('The number of unique vowels: ', len(l12))