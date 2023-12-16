"""

It requires 3 operands to work with.

First_value if condition else second_value

Nesting of ternary operators is possible.

"""

a = 10
b = 20
c = 30 if a < b else 40
print(c)

# a = int(input("Enter the first Number   : "))
# b = int(input("Enter the second Number  : "))
# c = int(input("Enter the third Number   : "))
# print('min: ', a if (a < b and a < c) else (b if b < c else c))
# print('max: ', a if (a > b and a > c) else (b if b > c else c))

a = 100
b = 2000
print("Both Numbers are equal" if a == b else "First Number is smaller than second Number" if a < b else "First "
                                                                                                         "Number is "
                                                                                                         "greater "
                                                                                                         "than second "
                                                                                                         "number")