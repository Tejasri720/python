Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables--------
print(6+8)
14
a=4
b=9
print(a+b)
13
a="tej"
print(a)
tej
_a=4
print(_a)
4
@=7
SyntaxError: invalid syntax
first_one="tej"
print(first_one)
tej
a=(1,2,3,4,5,6,7,)
print(a)
(1, 2, 3, 4, 5, 6, 7)
 a,b,c=1,2,3
 
SyntaxError: unexpected indent
a,b,c=1,2,3
print(a,b,c)
1 2 3
a,b,c=1,2,4,5,6,
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a,b,c=1,2,4,5,6,
ValueError: too many values to unpack (expected 3, got 5)
a,b,c=(4,5,6,)
print(a,b,c)
4 5 6
a=6
print9a)
SyntaxError: unmatched ')'
print(a)
6
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: '_a'?
>>> fname="teja"
>>> lname="sri"
>>> print=(fname+lname)
>>> 
>>> printfname+lname)
SyntaxError: unmatched ')'
>>> print(lname+fname)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(lname+fname)
TypeError: 'str' object is not callable
>>> fname'teja'
SyntaxError: invalid syntax
>>> fname='teja'
>>> lname='sri'
>>> print(fname+lname)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(fname+lname)
TypeError: 'str' object is not callable
>>> fname="teja"
>>> lname="sri"
>>> print("fname+lname)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print(fname+lname)
...       
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(fname+lname)
TypeError: 'str' object is not callable
