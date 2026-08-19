Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> fname="teja"
>>> lname="sri"
>>> print(fname+lname)
tejasri
>>> print(fname= name)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(fname= name)
NameError: name 'name' is not defined. Did you mean: 'fname'?
>>> print(fname+ lname)
tejasri
>>> print(fname+" "+lname)
teja sri
>>> print(fname,lname)
teja sri
