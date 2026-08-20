#print(),input(),max(),min(),sum(),len(),type(),range(),pow()
#print(dir())
#print(dir("__builtins__"))
#fromkeys()
'''
a="codegnan"
print(a)
print(list(a))
print(set(a))
print(tuple(a))
#print(dict(a))
b=dict.fromkeys(a)
print(b)
c=dict.fromkeys(a,"pooja")
print(c)
c["o"]="python"
print(c)'''

#eval(): it accept  all datatypes
'''
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''
'''
while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''
'''
while True:
    a=str(input("a value"))
    b=str(input("b value"))
    print(a+b)'''
'''
while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multiple collection into one collection.
'''
a=[10,20,30,40,50,60]
names=["teja","kavya","mani","bhavi","baa"]
print(a+names)
b=zip(a,names)
print(b)
b=list(zip(a,names))
print(b)
b=tuple(zip(a,names))
print(b)
b=set(zip(a,names))
print(b)
b=dict(zip(a,names))
print(b)
b=(zip(a,names))
print(*b)
b=list(zip(a,names))
print(*b)
'''
#enumerate()-> we can give counter to the collection
'''
names=["teja","pooja","pushpa","devi","bharani"]
for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names,1))
print(b)
b=list(enumerate(names))
print(b)
b=set(enumerate(names))
print(b)
b=tuple(enumerate(names))
print(b)'''

#railway ticket
'''
while True:
    a=1000
    c=input("choose the male or female")
    age=int(input("enter the age"))
    def male():
        if age>=60:
            print("ticket cost",a-(a*(30/100)))
        elif age<60:
            print("ticket cost ",a)
        
    def female():
        if age>=60:
            print("ticket cost",a-(a*(50/100)))
        elif age<60:
            print("ticket cost ",a-(a*(30/100)))
    if c=="male":
        male()
    else:
        female()'''

#using single loop
'''
def rail():
    t=1000
    gender=input("enter your genter")
    age=int(input("enter the age"))
    if gender=="m":
        if age>=60:
            print("senior citizen")
            t=t-30/100*t
            print(t)
        elif age<60:
            print("normal citizen")
            print(t)
        if gender=="f":
            if age>=60:
                print("senior citizen")
                t=t-500/100*t
                print(t)
            elif age<60:
                print("normal citizen")
                t=t-30/100*t
                print(t)
rail()
'''

#anonymous functions
#write a function to calculate 2*x+5 where x=5
'''def add(x):
    print(2*x+5)
add(5)'''
'''
def fun():
    x=int(input())
    print(2*x+5)
fun()'''
'''
#syntax
#a=lambda arg:expr
a=lambda x:2*x+5
print(a(5))'''
'''
a=int(input())
cb=lambda x:2*x+5
print(cb)'''
'''
a="codegnan"
b=lambda a:a.upper()
print(b(a))'''
'''
b=lambda a:a.upper()
print(b("codegnan"))'''
'''
a="python course"
b=lambda a:a.title()
print(b(a))'''
#multiplay
'''
a=int(input())
b=int(input())
c=lambda a,b:a*b
print(c(a,b))
'''
'''
a=2
b=5
c=lambda a,b:a*b
print(c(a,b))'''
'''
b=lambda a,b:a*b
print(b(2,4))'''


'''
f=input()
l=input()
c=lambda f,l:f+l
print(c(f,l))'''
'''
c=lambda f,l:f+l
print(c("teja","sri"))'''
'''
a,b=[x for x in input("enter the name").split(" ")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter
'''a=[10,20,30,40,50,60,70,80,90]
if a%2==0:
    print(a)'''
'''
a=[10,20,30,40,50,60,70,80,90]
for i in a:
    if i%2==0:
       print(i)'''
'''
a=[10,20,30,40,50,60,70,80,90]
b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[] () {}
'''
a=[]
print(type(a))
b=()
print(type(b))
c={}
print(type(c))
d=set()
print(type(d))'''
'''
a=[[],{},(),None,"",3,4.5,"python",6+9j,True,False]
b=list(filter(None,a))
print(b)'''

#map(())-.> each object from a collection and forms a collection and forms a new collection
'''
a=[2,5,7,9,10,20,30,80]
b=[1,9,20,50,60,4,25,80]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)'''

#using string
'''
a=input("data 1")
b=input("data 2")
print(a+b)'''
'''
a,b=input("enter the data").split(",")
print(a+b)'''
'''
a,b=map(str,input("enter the names").split(","))
print(a+b)'''
#using int
'''
a=int(input())
b=int(input())
print(a+b)'''
'''
a,b=[int(x) for x in input("enter the values").split(",")]
print(a+b)'''
'''
a,b=int(input("enter the values").split(","))
print(a+b)#error'''
'''
a,b=map(int,input("enter the values").split(","))
print(a+b)'''
'''
a=list(map(int,input("values").split(",")))
print(a)
print(type(a))'''
'''
a=tuple(map(int,input("values").split(",")))
print(a)
print(type(a))'''
'''
a=set(map(int,input("values").split(",")))
print(a)
print(type(a))'''

#dict
'''
a=int(input())
d={}
for i in range(a):
    key=input()
    values=input()
    d[key]=values
print(d)'''
'''
a=input()
b=dict(i.split(":") for i in a.split(","))
print(b)'''
'''
a=list(map(eval,input("values").split(",")))
print(a)
print(type(a))'''

a= input()
b=dict(i.split(":") for i in a.split(","))
print(b)














































