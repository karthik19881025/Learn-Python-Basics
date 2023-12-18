"""

%i - singed decimal value
%d - singed decimal value
%f - float value
%s - string other objects

"""

a = 10
print('a value: %i' % a)
print('a value: %d' % a)
print('a value: %f' % a)
name = 'durga'
marks = [10, 20, 30, 40]
print('Hello %s, your marks list: %s' % (name.upper(), marks))

price = 70.56789
print('price value = {}'.format(price))
print('price value = %.2f' % price)
