Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#len()-------
a="codegnan"
len(a)
8
a="kadavakolluTejasri"
len(a)
18
b="i am happy"
len(b)
10
a=""
len(a)
0
a=" "
len(a)
1
#count--------
n="tik tik tap tap"
n.count("tik")
2
n.count("tap")
2
n.count("t")
4
a.count(" ")
1
n.count(" ")
3
n.count("")
16
#finding a string
a="python"
a[1]
'y'
a.find["h"]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.find["h"]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.find("h")
3
b="hello"
b.find("l")
2
b[2:4]
'll'
a.find("k")
-1
#escape sequence
#\n-.new line
#\t->tab space
a="name\nmailid\tmobileno\ncollege\tbranch"
print(a)
name
mailid	mobileno
college	branch
b="name:Teja\nmailid:kadavakollutejasri@gmail.com\tmobileno:7207421109\ncollege:RGUKT\tbranch:ECE
SyntaxError: unterminated string literal (detected at line 1)
b="name:Teja\nmailid:kadavakollutejasri@gmail.com\tmobileno:7207421109\ncollege:RGUKT\tbranch:ECE"
print(b)
name:Teja
mailid:kadavakollutejasri@gmail.com	mobileno:7207421109
college:RGUKT	branch:ECE
#replace-----
a="wait untill you succeed"
a.replace("wait","work")
'work untill you succeed'
b="python java"
b.replace("p","c")
'cython java'
c="wait wait until you succeed"
c.replace("wait","work")
'work work until you succeed'
c.replace("wait","work",10)
'work work until you succeed'
c.replace("wait","work",1)
'work wait until you succeed'
#upper()
a="code"
a.upper()
'CODE'
a.lower()
'code'
#lower()
a="SADF"
a.lower()
'sadf'
c="python"
c[0].upper()
'P'
c.capitalize()
'Python'
e="i am a good girl"
e.title()
'I Am A Good Girl'
'I Am A Good Girl'
'I Am A Good Girl'

a="code"
a.isupper()
False
a=islower()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a=islower()
NameError: name 'islower' is not defined
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="code course"
b.isalpha()
False
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="123"
d.isdigit()
True
d="1,2,4"
d.isdigit()
False
#alnum mean alphabates and numericals
a="teja123"
a,isalnum()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a,isalnum()
NameError: name 'isalnum' is not defined
a.isalnum()
True
b="teja@123"
b.isalnum()
False
c="teja.123"
c.isalnum()
False
a="data science"
a.startswith("d")
True
a.startswith("e")
False
a.endswith("e")
True
#srip()
#istrip(),rstrip()
a=' teju  '
a.strip()
'teju'
a.lstrip()
'teju  '
a.rstrip()
' teju'
b=" i am in class"
b.strip()
'i am in class'
#split-----------
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i love java"
b.split()
['i', 'love', 'java']
c='teja"
SyntaxError: unterminated string literal (detected at line 1)
c='teja'
c.split()
['teja']
#join
b="sql","java","dbms","js"
b.join()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    b.join()
AttributeError: 'tuple' object has no attribute 'join'
"".join(b)
'sqljavadbmsjs'
" ".join(b)
'sql java dbms js'
"k".join(b)
'sqlkjavakdbmskjs'
c="teja"
"c".join(c)
'tcecjca'
#concatination




























a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="teja"
lname="sri"
print(fname+lname)
tejasri
print(fname+" "+lname)
teja sri
print(fname.title()+" "+lname)
Teja sri
print(fname+" "+lname.title)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    print(fname+" "+lname.title)
TypeError: can only concatenate str (not "builtin_function_or_method") to str
print(fnmae+" "+lname.title())
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    print(fnmae+" "+lname.title())
NameError: name 'fnmae' is not defined. Did you mean: 'fname'?
print((fname+" "+lname).title())
Teja Sri
#formatting
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
city="vij"
print("city is",city)
city is vij
print9"the sum is,a+b")
SyntaxError: unmatched ')'
print("the sum is,a+b")
the sum is,a+b
#format----


























>>> #format----
>>> a="motu"
>>> b="pathlu"
>>> print("hello {}{}".format(a,b))
hello motupathlu
>>> print("hello{}  {}".format(a,b))
hellomotu  pathlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello pathlu
>>> print("hello {}\nhello{}".format(a,b))
hello motu
hellopathlu
>>> #fstring
>>> a="sitha"
>>> b="ram"
>>> print(f"hello{a}{b}")
hellositharam
>>> print(f"hello {a} {b}")
hello sitha ram
>>> print(f"hello {a}\nhello {ram}")
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    print(f"hello {a}\nhello {ram}")
NameError: name 'ram' is not defined
>>> print(f"hello {a}\nhello {b}")
hello sitha
hello ram
>>> print(f"hello {}\thello {b}")
SyntaxError: f-string: valid expression required before '}'
>>> print(f"hello {a}\thello {b}")
hello sitha	hello ram
