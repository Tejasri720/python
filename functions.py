'''a=10
b=20
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the difference is",a-b)
print("the product is",a*b)'''
'''
def fun(a,b):
    print("the sum is",a+b)
    print("the difference is",a-b)
    print("the product is",a*b)
fun(10,20)
fun(100,200)
fun(1000,2000)'''
'''
def fun(a,b):
    print("the power is",a**b)
    print("the modulus is",a%b)
    print("the division is",a//b)
fun(10,20)
fun(2,3)
fun(10,5)'''
'''
def add(a,b):
    print(a+b)
add(3,40)'''
'''
while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''
'''
def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add()'''
'''
def mul(a,b):
    print(a*b)
mul(2,4)'''
'''
def mul (a,b):
    return a*b
print(mul(2,4))'''
'''
def cal (a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,4)'''
'''
def cal (a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(2,4))'''
'''
while True:
    def funcal():
        a=int(input())
        b=int(input())
        c=int(input("choose the option 1.sum\n 2.sub\n 3.mul\n"))
        if c==1:
            print("the sum of a and b",a+b)
        elif c==2:
            print("the difference of a and b",a-b)
        elif c==3:
            print("the product of a and b",a*b)
    funcal()'''
'''
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
a=int(input())
b=int(input())
while True:
    c=int(input("choose the option 1.sum\n 2.sub\n 3.mul\n"))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        mul()'''
#split bill
'''
a=int(input("enter the number of people"))
b=int(input("enter the amount"))
c=b//a
print("amount that each person get",c)
'''
'''
def sub():
    a=int(input("enter the number of people"))
    b=int(input("enter the amount"))
    c=b//a
    return("amount that each person get",c)
print(sub())'''
'''
a=int(input("enter the number of people"))
b=int(input("enter the amount"))
c=b//a
c=("There are total {} people and the amount is{}.\n the amount each person get{}".format(a,b,c))
print(c)'''
'''
a=int(input("enter the number of people"))
b=int(input("enter the amount"))
c=b//a
c=(f"There are total {a} people and the amount is{b}.\n the amount each person get{c}")
print(c)'''

#keywords and positional arguments
'''
def Details(id,name,mailid):
    id=10
    name="teja"
    mailid="teja@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''
'''
def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id="20",name="malavika",mailid="m@gmail.com")
Details(id="30",name="lohitha",mailid="l@gmail.com")
Details(40,"geethika","g@gmail.com")
Details("teja","t@gmail.com",60)
Details(name="bharani",mailid="b@gmail.com",id=50)'''

#default arguments
'''
def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("rice",1500)'''
'''
def grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery()'''
'''
def grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("dal")'''
'''
def grocery(item="peanuts",price):
    #a nondefault argument follows default argument
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery(150)'''
'''
def bakery(cake,price,quantity):
    print("cake is %s"%cake)
    print("price is %d"%price)
    print("quantity is %s" ,quantity)
bakery("chocklete",600,"1kg")'''
'''
def bakery(cake="butterscotch",price=500,quantity="2kg"):
    print("cake is %s"%cake)
    print("price is %d"%price)
    print("quantity is %s",quantity)
bakery()'''
'''
def bakery(cake,price,quantity="1kg"):
    print("cake is %s"%cake)
    print("price is %d"%price)
    print("quantity is %s",quantity)
bakery("venilla")'''
'''
def bakery(cake="blackforest",price,quantity):
    print("cake is %s"%cake)
    print("price is %d"%price)
    print("quantity is %s",quantity)
bakery(600,"3kg")'''

 #* arguments
'''
a=[10,20,30,40]
print(a)
print(*a)'''
'''
a=(1,2,3,4,5,6)
print(a)
print(*a)'''
'''
a={1,2,3,4,5,6}
print(a)
print(*a)'''
'''
a={"year":2026,"month":"july"}
print(a)
print(*a)'''

'''
a,b,c=1,2,3,4,5,6,7,9
print(a)
print(b)
print(c)'''
'''
a,b,c=1,2,3
print(a)
print(b)
print(c)'''
'''
a,*b,c=1,2,3,4,5,6,7,9
print(a)
print(*b)
print(c)'''
'''
a="codegnan"
print(a)
print(*a)
'''
'''
a,b,c="codegnan"
print(a)
print(b)
print(c)'''
'''
a,b,c="cod"
print(a)
print(b)
print(c)'''
'''
a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''

#variable lengh arguments
'''
def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6)
b=[4,5,6,7,8]
check(*b)
c={9,7,6,5,7}
check(*c)
d={"name":"pooja","city":"vija"}
check(*d)'''
'''
def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(1,3,4,5.2,3.4)
check1(3,4,5,3.6,2.4,"pooja")'''

#kwargs(**)
'''
def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)'''
'''
def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)'''
'''
def final(*a,**b):
    d=3#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("keys is",i)
        print("value is",j)
final()
data=(2,3,4,3.5,6.2)
final(*data)
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
final(**details)
final(*data,**details)'''

#ma() min() sum()
'''
print(max(57,9,4,40,20))
print(min(1,2,3,56,7,8,90))
c=(1,2,3,4,5,6,7,8)
print(sum(c))'''
'''
#marks analysis report
a=int(input("enter no of students:"))
b=[]
for i in range(1,a+1):
    c=int(input("student {} marks".format(i)))
    b.append(c)
print("highest value is",max(b))
print("lowest value is",min(b))
c=sum(b)
print("total marks is",c)
d=c/a
print("average marks",(f"{d:.2f}"))'''


#global  and local variable
#first case of global variables
'''
a=2
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''

#second case of global variABLE
'''
a=4
def check1():
    a=5
    a=a**2
    print("inside value is",a)
check1()
print("outside value is",a)'''

#third case of both globa and local vaiables
'''
a=3
b=6
def check2():
    a=6
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variables
    b=b+a
    print("value of b is",b)
check2()
print("a value is",a)
print("b value is ",b)'''
#useage of global key word #scope of the variable
#when user wants to create a variable inside the function directly and
#carry forward and carry forward the updated value then we need to global key word.
'''
a=4
def final():
    global a,b
    print("inside value is",a)
    a=15
    print("updated value is",a)
    b=20
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

#generators
#a=[i for i in range(16)]# list comphresion
'''a=[i for i in range(16)]
print (a)
print(type(a))'''
'''
a=(i for i in range(16))
print(*a)
print(type(a))'''
'''
a=(i for  i in range(16))
#print(list(a))
#print(tuple(a))
print(set(a))'''
'''
a,b=(int(x) for x in input("value").split(","))
def check(a,b):
    while a<b:
        #yield a
        a=a+1
        yield a
print(*check(a,b))'''
'''
a,b=(int(x) for x in input("values").split(","))
def check (a,b):
    while a<b:
        a=a+1
        #return a
    return a
print(check(a,b))'''

#yield v/s return
'''def mygen():
    #return "vij"
    #return "hyd"
    #return "viz"
    return "vij","hyd","vzg"
print(*mygen())'''

'''
def mygen():
    yield"python"
    yield"java"
    yield"c"
print(*mygen())

#next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))#stop iteration'''
'''
a=10
print(a)
b=input()
print(b)'''

'''
c=[10,20,30,40]
d=sum(c)
print(d)
print(max(c))
print(min(c))
print(len(c))
print(type(c))'''


for i in range(1,11):
    print(i*i)







































        
          






























     
        
        




























