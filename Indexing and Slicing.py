Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
s="python"
s[0]
'p'
s[6]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s[6]
IndexError: string index out of range
s[4]
'o'
s[5]
'n'
s[0]+s[1]+s[2]+s[3]+s[4]+s[5]
'python'
s="12345"
s[0]+s[1]+s[2]+s[3]+s[4]
'12345'
s[0]
'1'
s[1]+[2]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s[1]+[2]
TypeError: can only concatenate str (not "list") to str
s[4]+s[5]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[4]+s[5]
IndexError: string index out of range
s="python"
s[4]+s[5]
'on'
a="i am in class"
a[8]+a[9]
'cl'
a[1]
' '
a="i am learning python"
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
KeyboardInterrupt
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
s= "i love codegnan"
a[3]+a[4]+a[5]+a[6]
'm le'
s[2]+s[3]+s[4]+s[5]
'love'
s[7]+s[8]+s[9]+s[10]
'code'
s[11]+s[12]+s[13]+s[14]
'gnan'
s="vijayawada is a royal city"
s[-10]+s[-9]+s[-8]+s[-7]+s[-6]
'royal'
s[-4]+s[-3]+s[-2]+s[-1]
'city'
s[-15]+s[-14]
'is'
b="vizag is a city od destiny"
b[-15]+b[-14]+b[-13]+b[-12]
'city'
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
#slicing
a="codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
a[4:]
'gnan'
a[:4]
'code'
a[:]
'codegnan'
a="work untile you suceed"
a[0:5]
'work '
a[5:10]
'until'
>>> s="simple is better than complex"
>>> s[-19:-14]
'bette'
>>> s[-7:]
'complex'
>>> s[-7:-1]
'comple'
>>> s[-29:-23]
'simple'
>>> s="codegnan it solutions"
>>> s[-8:]
'olutions'
>>> s[-9:]
'solutions'
>>> s[:-12]
'codegnan '
>>> #striding
>>> a="Machine learning"
>>> a[:4]
'Mach'
>>> a[::4]
'Miln'
>>> a[::7]
'M n'
>>> a[::2]
'Mcielann'
>>> a="cloud computing"
>>> a[1:12:3]
'ldou'
>>> a[4:14:4]
'dmi'
>>> a[6:10:1]
'comp'
>>> a[2:13:5]
'ooi'
>>> a[-1:-12:-3]
'gtm '
>>> a[-4:-14:-4]
'tou'
>>> a[-6:-10:-1]
'pmoc'
>>> a[-2:-13:5]
''
>>> a[-2:-13:-5]
'nmu'
