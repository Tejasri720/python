Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=[9,1,5,2,8,4,6,3,7,0]
#[7,6,4,3,0,9,8,5,2,1]
a.sort()
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.reverse()
a
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a=[9,1,5,2,8,4,6,3,7,0]
a
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
a.extend([7,6,4,3,0,9,8,5,2,1])
a
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0, 7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
a.clear()
a
[]
a.extend([7,8,4,3,0,9,8,5,2,1])
a
[7, 8, 4, 3, 0, 9, 8, 5, 2, 1]
a.extend([7,6,4,3,0,9,8,5,2,1])
a
[7, 8, 4, 3, 0, 9, 8, 5, 2, 1, 7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
a.extend([7,6,4,3,0,9,8,5,2,1]).update()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.extend([7,6,4,3,0,9,8,5,2,1]).update()
AttributeError: 'NoneType' object has no attribute 'update'
a.extend([7,6,4,3,0,9,8,5,2,1])
a.update()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.update()
AttributeError: 'list' object has no attribute 'update'
>>> a.clear()
>>> a
[]
>>> a.extend([7,6,4,3,0,9,8,5,2,1])
>>> a
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> b=a2+a1
>>> b
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
