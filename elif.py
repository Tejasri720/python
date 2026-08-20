#if- else condition using comparision
#!=,==,<,>,<=,>=
'''
a=2
b=4
if a<b:
    print("less")
elif b<a:
    print("grater")'''
'''
a=2
b=4
if a==b:
    print("less")
elif b!=a:
    print("grater")'''
'''
a=2
b=4
if a==b:
    print("less")
elif b<a:
    print("grater")
elif b<=a:
    print("true")
elif a!=b:
    print("not true")'''

#if-elif-else
'''
a=5
b=10
if a>b:
    print("greater")
elif a>=b:
    print("not equel")
elif a==b:
    print("equal")
else:
    print("true")'''
'''
a=5
b=10
if a<b and b>a:
    print("greater")
elif a!=b or a==b:
    print("not equal")
else:
    print("true")'''
#identifier
#is is not
'''
a=int(input("value"))
if type(a) is int:
    print("it is int")
else:
    print("not int")'''

#multiple if
'''
a=9
b=11
if a>b:
    print("less")
if b>a:
    print("greater")
if a==b:
    print("equal")
if a!=b:
    print("not equal")'''
'''
a=9
b=11
if a>b:
    print("less")
if b>a:
    print("greater")
if a==b:
    print("equal")'''
'''
a=2
b=4
if a<b:
    print("less")
    if b>a:
        print("greater")'''
'''
a=2
b=4
if a==b:
    print("less")
    if b<a:
        print("greater")'''
'''
a=12
b=14
if a<b:
    print("less")
    if b<a:
        print('greater')'''
'''
a=2
b=4
if a==b:
    print("less")
    if b<a:
        print("greater")
    else:
            print("true")
'''
'''
a=15
b=20
if a==b:
    print("less")
if b>a:
    print("less")
if b>a:
    print("greater")
elif a!=b:
    print("not")'''

#task 1
#voteing
'''
a=int(input("enter number"))
if a>=18:
    print("eligible")
else:
    print("not eligible")

#even or odd
a=int(input("enter a number"))
if a%2==0:
    print("even number")
else:
    print("odd number")

#leap year
a=int(input("enter a number"))
if (a%4==0) and (a%400):
    print("leap year")
else:
    print("not leap year")'''

#task 2
'''
a=str(input("enter string"))
if (a=="teja"):
    print("welcome teja")
else:
    print("welcome guest")
#for multiple user
a=['teja','priya','divya','navya','ananya']
b=str(input())
if b in a:
    print("welcome",b)
else:
    print("welcome guest")'''
'''
#vowel and consonents
a=['a','e','i','o','u']
b=str(input("enter")).lower()
if b in a:
    print("it's a vowel")
else:
    print("it's a consonant")'''


    


            
        
        



    

