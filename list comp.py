'''a=["python","java","dsa"]
for in a:
    print(i.upper(),end=' ')
b=[]
for i in a:
    b.append(i.upper())
print(b)
'''

#while loop
'''
a=10
while a>1:
    print(a)'''
'''
a=10
while a>1:
    print(a)
    a=a-1'''
'''
a=10
while a>1:
    print(a)
    a=a+1'''
'''
a=10
while a>=1:
    print(a)
    a=a-1'''
'''
a=20
while a>2:
    a=a-1
    print(a)'''
'''
a=20
while a>2:
    a=a-1
print(a)'''
'''
a=30
while a>2:
    print(a)
    a+=1'''
'''
a=30
while a>2:
    print(a)
    a-=1'''
'''
a=1
while a<30:
    print(a)
    a+=1'''
'''
while True:
    a=str(input("username"))
    c=int(input("password"))
    if a=="Teja" :
        if c==1234 :
            print("login successful")
    else :
            print("invalid credentials")'''

#range()
#the range function returns a sequence of numbers,
#starting from zero by default and increments by 1 by 1 and stops before a  specified number
#start-stop-step
'''
for i in range(10):
    print(i)'''
'''
for i in range(5,20):
    print(i)'''
'''
for i in range(5,50,5):
    print(i)'''
'''
for i in range(0,20,2):
    print(i)'''
'''
for i in range(3,30,3):
    print(i)'''
'''
#it wont work because in for loop it gives continuous iteation
a=int(input())
for i in range(91,101):
    print("grade A")
    break
    for j in range(81,91):
        print("grade B")
        for k in range(71,81):
            print("grade C")
            for l in range(50,71):
                print("grade D")
                for m in range(0,49):
                    print("fail")'''
'''
while True:
    m=int(input("enter:"))
    if m in range(91,101):
        print("grade A")
    elif m in range(81,91):
        print("grade B")
    elif m in range(71,81):
        print("grade c")
    elif m in range(50,71):
        print("grade D")
    else:
        print("fail")'''



#Break
'''
a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''
'''
a=20
while a>3:
    a=a-1
    if a==6:
        break
    print(a)'''
'''
for i in range(25):
    if i==19:
        break
    print(i)'''
'''
a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue---
'''
a=30
while a>5:
    print(a)
    a=a-1
    if a==15:
        continue
    '''
'''
a=30
while a>5:
    a=a-1
    if a==15:
        continue
    print(a)'''
'''
for i in range(15):
    if i==11:
        continue
    print(i)'''
'''
a="python"
for i in a:
    if i=="h":
        continue
    print(i)'''

#pass-----
'''
a=9
while a>2:
    print(a)
    a=a-1
    if a==7:
        pass'''
'''

for i in range(25):
    if i==20:
        pass
    print(i)'''


#atm application

while True:
    account = 100000
    pwd = 1234
    card = 'c'

    a = str(input("insert the card: "))

    if a == card:
        print("welcome teja")
        b = int(input("enter the password: "))

        if b == pwd:
            option = int(input("enter the option 1: balance enquiry 2: withdraw: "))

            if option == 1:
                print("account balance is", account)

            elif option == 2:
                money = int(input("enter the amount: "))
                print(money)
                balance = account - money
                print("remaining account balance is", balance)

            else:
                print("invalid option")

        else:
            print("incorrect password")

    else:
        print("invalid card")
'''
for y in range(3):
    for x in range(1,10):
        print(x,end="")
 
    print()'''

'''
a=5
for i in range(1,a+1):
    print("*"*i)'''
'''
a=5
for i in range (1,a+1):
    print("*"*a)'''
'''
a=5
for i in range(5,0,-1):
    print("*"*i)'''
'''
a=5
for i in range(n):
    print("*"*(n-i))'''

    
'''
a=5
for i in range(1,a+1):
    print(" "*(a-i)+"* "*i)'''



































#list comprehension
a=["python","java","dsa"]
#["PYTHON","JAVA","DSA"]
#PRINT(a.upper()) error
'''
b=str(a)
print(b.upper())'''
'''
for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[expression for var in collection/range]
'''
a=[i.upper() for i in a]
print(a)'''
'''
a=["codegnan","course","python"]
b=[i.title() for i in a]# here capitalize can be used
print(b)'''
'''
a=[1,3,4,5,6,8,12,13]
b=[i**2 for i in a]
b=[i*i for i in a]
b=[pow(i,2) for i in a]
print(b)'''

# if useage in list  compresion
'''
a=21
b=[i for i in range(a) if i%2==0]
print(b)'''
'''
a=21
b=[i for i in range(a) if i%2!=0]
print(b)'''
'''
a=21
b=[i*i for i in range(a) if i%2==0]
print(b)'''
'''
a=["apple","banana","mango","dragon","kiwi","berry"]
b=[i for i in a if "a" in i]
print(b)
a=["apple","banana","mango","dragon","kiwi","berry"]
b=[i for i in a if "a" not in i]
print(b)'''

#no elif  useage in list compresion
'''
#if-else useage in list compresion
a=16
b=[i*i if i%2==0 else i*5  for i in range(a)]
print(b)'''
'''
a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(5)]
c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

'''
#students report
a=int(input("no.of students:"))
p=0
aa=0
for i in range(1,a+1):
    c=input(f"student{i}(p/a)")
    if c=="p":
        p=p+1
    elif c=="a":
        aa=aa+1
print("..........attendence report...............")
print("total students",a)
print("total presenties",p)
print("total absenties",aa)'''
'''
#BMI calculator
while True:
    a=float(input("enter the weight:"))
    b=float(input("enter the height:"))
    bmi=a/(b)**2
    print(bmi)
    if bmi<18.5:
        print("under weight")
    elif bmi>=18.5 and bmi<24.5:
        print("healthy weight")
    elif bmi>=24.5 and bmi<=29.5:
        print("over weight")
    elif bmi>30:
        print("obesity")'''






































                    
        
        

































