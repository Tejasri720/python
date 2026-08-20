'''a=2
b=3
print(a+b)'''

#run-input input
'''a=int(input("enter a value"))
b=int(input("enter a value"))
print(a+b)'''

'''
a=float(input("enter a value"))
b=float(input("enter a value"))
print(a+b)
            '''
'''
a=str(input("enter a value"))
b=str(input("enter a value"))
print(a+b)
'''

'''a=complex(input("enter a value"))
b=complex(input("enter a value"))
print(a+b)
'''
'''
a=bool(input("enter a value"))
b=bool(input("enter a value"))
print(a+b)
'''
'''
a=input("enter  data:")
b=input("enter data1:")
print(a+b)
'''
'''
a=str(input("enter a value"))
b=str(input("enter a value"))
print((a+" "+b).title())'''
'''
a=bool(input("enter a value"))
b=bool(input("enter a value"))
c=bool(input("enter a value"))

print(a+b+c)'''

'''a=int(input("value a:"))
b=int(input("value b:"))
option=int(input("choose the option 1.add 2.sub 3.mul"))
print(a+b)
print(a-b)
print(a*b)'''

'''
a=int(input("value a:"))
b=int(input("value b:"))
option=int(input(choose the option
                 1.add
                 2.sub
                 3.mul))
print(a+b)
print(a-b)
print(a*b)'''

a=int(input("value a:"))
b=int(input("value b:"))
option=input("choose the option add sub mul")
print(a+b)
print(a-b)
print(a*b)
#task 2
#swapping of variables
#1st method(using operators)
'''
a=int(input("value a:"))
b=int(input("value b:"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)'''

#second method(without temp)
'''
a=int(input("value a:"))
b=int(input("value b:"))
a,b=b,a
print(a,b)'''
#third method(temp method)
'''
a=int(input("value a:"))
b=int(input("value b:"))
temp=a
a=b
b=temp
print(a,b)'''

#fourth method(number formating)
'''
a=int(input("value a:"))
b=int(input("value b:"))
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d"%(a,b))'''
#task 3
#["CODEGNAN","PYTHON","COURSE"]
'''
a=["codegnan","python","course"]
b=str(a)
print(b.upper())'''
#0r
'''
a="codegnan"
b="python"
c="course"
print([a.upper(),b.upper(),c.upper()])'''
#task4
#[10,20,30,40,50,"code"]
'''
a=[10,20,30,40,50,"code"]
a.extend("code")
print(a)'''

#task5
'''
a=[5,7,9,10,11,13]
a.insert(5,12)
print(a)'''
#task 6
'''
a=[9,7,4,0,1,5,10,8,6,3]
a.sort()
print(a)'''
#task7
'''
a=("apple","banana","mango")
b=list(a)
b.append("grapes")
c=tuple(b)
print(c)
print(type(c))'''

#student profile
a=int(input("Id NO:"))
b=str(input("Name:"))
c=int(input("mobile no:"))
d=str(input("mail-id:"))
e=str(input("college name:"))
f=str(input("branch:"))
print(a,"\n", b,"\n",c,"\n",d,"\n",e,"\n",f,"\n")
'''print(a)
print(b)
print(c)
print(d)
print(e)
print(f)'''














