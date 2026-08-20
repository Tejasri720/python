Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4.5,"python",6+3j,True,False]
print(a)
[2, 4.5, 'python', (6+3j), True, False]
type(a)
<class 'list'>
b=2.3
type(b)
<class 'float'>
b=[2.3]
type(b)
<class 'list'>
#append
a=["python","c++","java"]
a.append("C")
a
['python', 'c++', 'java', 'C']
a.append("c","html")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("c","html")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["html","css"])
a
['python', 'c++', 'java', 'C', ['html', 'css']]
#extend
a=["python","c","java"]
a.extend(["html","css","c++"])
a
['python', 'c', 'java', 'html', 'css', 'c++']
#insert
b=["vja","vzg","hyd"]
b.insert(1,"chennai")
b
['vja', 'chennai', 'vzg', 'hyd']
#index
a=["apple","banana","grapes"]
a.index("grapes")
2
#copy
a.copy()
['apple', 'banana', 'grapes']
b=a.copy()
b
['apple', 'banana', 'grapes']
a.count("apples")
0
a.count("apple")
1
len(a)
3
len(b)
3
d="apples"
len(d)
6
e=["apple"]
len(e)
1
#sort
a=["mango","kiwi","dragon","berry","apple"]
a.sort()
b=[5,2,8,12,9,19,2,0,1]
b.sort()
b
[0, 1, 2, 2, 5, 8, 9, 12, 19]
#reverse()
a=["ai","ml","ds"]
a.reverse()
b=[3,27,18,18,29,4,5,6,8]
v.reverse()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    v.reverse()
NameError: name 'v' is not defined
b.reverse()
b
[8, 6, 5, 4, 29, 18, 18, 27, 3]
#pop
a=["black","blue","white"]
a.pop()
'white'
a
['black', 'blue']
a.pop(1)
'blue'
a
['black']
#remove
a=["black","blue","white"]
a.remove("black")
a
['blue', 'white']
#clear
a=["black","blue","white"]
a.clear()
a
[]
#tuple
a=(4,4.5,"python",8+3j,True,False)
print(a)
(4, 4.5, 'python', (8+3j), True, False)
type(a)
<class 'tuple'>
#index
a.index(8+3j)
3
len(a)
6
#count()
a.count(a)
0
a.count(True)
1
#set{}
a={4,7.8,"pooja",5+9j,True,False}
print(a)
{False, True, (5+9j), 4, 7.8, 'pooja'}
type(a)
<class 'set'>
a={4,7.8,"pooja",5+9j,True,False}
print(b)
[8, 6, 5, 4, 29, 18, 18, 27, 3]
#add()
a={4,5,1,7,8}
a.add(15)
a
{1, 4, 5, 7, 8, 15}
a={1,2,3,4,5,6,7}
b={1,2,3}
a.issubset(b)
False
b.issubset(a)
True
a={1,2,3,4}
b={2,3}
b.issubset(a)
True
a.issubset(b)
False
#issuperset
a={1,2,3,4,5,6}
b={1,2,3}
a.issuperset(b)
True
b.issuperset(a)
False
a={3,4,5,6,7}
b={1,2,3,4,5,6,7}
a.union(b)
{1, 2, 3, 4, 5, 6, 7}
a={3,4,5,6,7}
b={1,2,3,7,8,9}
a.intersection(b)
{3, 7}
b.intersection(a)
{3, 7}
a={1,2,3,4,5,6,7,8}
b={5,6,7,8,9}
#difference
a.difference(b)
{1, 2, 3, 4}
b.difference(a)
{9}
a={1,2,3,4,5,6}
b={6,7,8,9}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a,b
({1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 2, 3, 4, 5, 6, 7, 8, 9})
a={2,3,4,5,6,7,8}
b={1,4,6,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 3, 5, 7, 9, 10, 11}
b.symmetric_difference(a)
{1, 2, 3, 5, 7, 9, 10, 11}
a={4,5,6,7,8,9}
b={1,2,3,4,5,6,10}
a.difference_update(b)
a
{7, 8, 9}
b.difference_update(a)
b
{1, 2, 3, 4, 5, 6, 10}
a={3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.intersection_update(b)


a
{8, 5, 6, 7}
b.intersection_update(a)
>>> b
{8, 5, 6, 7}
>>> a={11,12,13,14,15,16}
>>> b={13,14,15,16,17,18}
>>> a.symmetric_difference_update(b)
>>> a
{17, 18, 11, 12}
>>> b.symmetric_difference_update(a)
>>> b
{16, 11, 12, 13, 14, 15}
>>> a={1,2,3,4,5,6,7}
>>> a.pop()
1
>>> a.po(2)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    a.po(2)
AttributeError: 'set' object has no attribute 'po'. Did you mean: 'pop'?
>>> a.remove(3)
>>> a
{2, 4, 5, 6, 7}
>>> a={10,20,30,40}
>>> a.copy()
{40, 10, 20, 30}
>>> b=a.copy()
>>> b
{40, 10, 20, 30}
>>> a.discard(50)
>>> a
{40, 10, 20, 30}
>>> a.discard(30)
>>> a
{40, 10, 20}
>>> a.clear()
>>> a
set()
>>> a=set()
>>> a.add(100)
>>> a={2,3,4,5,6}
>>> b={6,7,8,910}
>>> a.isdisjoint(b)
False
>>> c={10,20,30,40}
>>> d={50,60,70,80}
>>> c.isdisjoint(d)
True
