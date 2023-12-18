l1 = [10, 20, 30, 40, 50]
print(l1)

t1 = (10, 20, 30, 40, 50)
print(t1)

name = 'durga'
salary = 10000
gf = 'sunny'

print(f'Hello {name.upper()}, Your salary is {salary} and your friend {gf} is waiting')

print('Hello {}, Your salary is {} and your friend {} is waiting'.format(name, salary, gf))

print('Hello {0}, Your salary is {1} and your friend {2} is waiting'.format(name, salary, gf))

print('Hello {n}, Your salary is {s} and your friend {f} is waiting'.format(n=name, s=salary, f=gf))

print('Hello {n}, Your salary is {s} and your friend {f} is waiting'.format(f=gf, n=name, s=salary))

a, b, c, d = 10, 20, 30, 40
print('a={}, b={}, c={}, d={}'.format(a, b, c, d))
print('a={0}, b={1}, c={2}, d={3}'.format(a, b, c, d))
print(f'a={a}, b={b}, c={c}, d={d}')
