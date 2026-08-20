Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes------
int5
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int5
NameError: name 'int5' is not defined. Did you mean: 'int'?
int(5)
5
a=5
type(a)
<class 'int'>
a=3.4
type(a)
<class 'float'>
a="teja"
type(a)
<class 'str'>
a=4j
type(a)
<class 'complex'>
a=True
type(a)
<class 'bool'>
#datatype conversions-------
int(3)
3
int(3.7)
3
int("apple")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int("apple")
ValueError: invalid literal for int() with base 10: 'apple'

int(6j)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
float(5)
5.0
float(4.9)
4.9
float("dad")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float("dad")
ValueError: could not convert string to float: 'dad'
float(7j)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(False)
0.0
str(5)
'5'
str(9.7)
'9.7'
str("cute")
'cute'
str(6j)
'6j'
>>> str(True)
'True'
>>> complex(5)
(5+0j)
>>> complex(4.3)
(4.3+0j)
>>> complex("string")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex("string")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> bool(3)
True
>>> bol(9.7)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    bol(9.7)
NameError: name 'bol' is not defined. Did you mean: 'bool'?
>>> bool(9.8)
True
>>> bool("rat")
True
>>> bool(5j)
True
>>> bool(False)
False
