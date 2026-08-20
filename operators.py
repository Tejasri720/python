Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithmatic
a=2
b=2
print(a+b)
4
print(a-b)
0
print(a*b)
4
print(a/b)
1.0
print(a**b)
4
print(a%b)
0
print(a//b)
1
#assinmenta=3
a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
8
a-=b
a
3
a*=b
a
15
a/=b
a
3.0
a//=b
a
0.0
a**=2
a
0.0
a=4
b=3
b+=a
b
7
b-=a
b
3
b*=a
b
12
b**=a
b
20736
b/=a
b
5184.0
b//=a
b
1296.0
#comparision
a=3
b9
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    b9
NameError: name 'b9' is not defined. Did you mean: 'b'?
a=4
b=6
a>b
False
a<b
True
a==b
False
a!b
SyntaxError: invalid syntax
a!=b
True
a<=b
True
a>=b
False
b<=a
False
b>=a
True
b<a
False
b>a
True
b!=a
True
b==a
False
#logical
a=3
b=4
a>b and b>a
False
a<=b and b>=a
True
a!=b  and a==b
False
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not Flase
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    not Flase
NameError: name 'Flase' is not defined. Did you mean: 'False'?
not False
True
#identify
a=6
type is int
False
type is not int
True
type(a) is int
True
type (a) is not int
False
type(b) is float
False
b="python"
type (b) is not float
True
type (b) is not string
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    type (b) is not string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(b) is not String
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    type(b) is not String
NameError: name 'String' is not defined
b=4j
type(b) is complex
True
 type(b) is not complex
 
SyntaxError: unexpected indent
type (b) is not complex
False
#membership
a=4,5,6,7,8
5 in a
True
10 in a
False
10 not in a
True
 1 in a
 
SyntaxError: unexpected indent
1 in a
False
#bitwise
#bitwise
#bitwise-------------





















#bitwise-------------
#bitwise-------------
a=2
b=3
a&b
2
b&a
2
bin(2)
'0b10'
bin (11)
'0b1011'
bin(12)
'0b1100'
bin(13)
'0b1101'
BIN(14)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    BIN(14)
NameError: name 'BIN' is not defined. Did you mean: 'bin'?
bin(14)
'0b1110'
'0b1110'
'0b1110'

a=2
b=6
a|b
6
b|a
6
a=9
b=8
a|b
9
a=2
b=6
a|b
6
bin(32)
'0b100000'
a=67
b=90
a|b
91
a=6
-9a+1)
SyntaxError: invalid decimal literal
a=6
-(a+1)
-7
~a
-7
a=4
~a
-5
b=-3
~b
2
d=2
a=3
>>> d~a
SyntaxError: invalid syntax
>>> a=3
>>> b=6
>>> a^b
5
>>> a=8
>>> b=9
>>> a^b
1
>>> a=67
>>> a'=4
SyntaxError: unterminated string literal (detected at line 1)
>>> a^a'
SyntaxError: unterminated string literal (detected at line 1)
>>> a=5
>>> a>>
SyntaxError: invalid syntax
>>> a>>2
1
>>> a=5
>>> a>>2
1
>>> a=5
>>> a<<2
20
>>> a=4
>>> a>>2
1
>>> a<<2
16
