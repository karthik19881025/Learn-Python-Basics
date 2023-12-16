"""

= Is used to assign a value to a variable
+= is used to assing a value to itself after its original value got manipulated. (Compound Assignment Operator)
-= is used to assing a value to itself after its original value got manipulated. (Compound Assignment Operator)
*=
%=
**=
/=
//=

^=
&=
|=
^=
>>=
<<=


"""

x = 10
a, b = 20, 30
y = z = 100
print(x, a, b, y, z)

x = 10
x &= 5
print(x)

x = 10
print(-x)
