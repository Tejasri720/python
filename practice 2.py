#Create a Dictionary from User Input
a=int(input())
d={}
for i in range(a):
    key,value=input().split()
    d[key]=value
print(d)
#Search for a Key
'''a=int(input())
d={}
for i in range(a):
    key,value=input().split()
    d[key]=value
print(d)
b=input()
if b in d:
    print("key exists")
else:
    print("key does not exist")'''
#Find the Value of a Key.
'''a=int(input())
d={}
for i in range(a):
    key,value=input().split()
    d[key]=value
print(d)
b=input()
print(d[b])'''
#Add a New Key-Value Pair.
'''a=int(input())
d={}
for i in range(a):
     key,value=input().split()
     d[key]=value
print(d)
b,c=input().split()
d[b]=c
print(d)'''

#Update a Dictionary Value.
'''a=int(input())
d={}
for i in range(a):
     key,value=input().split()
     d[key]=value
print(d)
b,c=input().split()
d[b]=c
print(d)'''

#Count Frequency of Characters

'''a=input()
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)'''

#Number Frequency

'''a=list(map(int,input().split()))
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)'''
        
#Find the Maximum Value in a Dictionary.
'''a=int(input())
d={}
for i in range(a):
    key,value=input().split()
    d[key]=value
print(max(d.values()))'''

#Find the Minimum Value.
'''a=int(input())
d={}
for i in range(a):
    key,value=input().split()
    d[key]=value
print(d)
print(min(d.values()))'''

#Sum of Dictionary Values.
'''
a=int(input())
d={}
for i in range(a):
    key,value=input().split()
    d[key]=int(value)
print(sum(d.values()))'''

#Remove a Key from a Dictionary.
'''a=int(input())
d={}
for i in range(a):
    key,value=input().split()
    d[key]=value
b=input()
if key in d:
    del d[key]
print(d)'''
        
#file hanling
'''
t=input()
with open("sample.txt","w") as f:
    f.write(t)
print("data written successfully")

'''
'''with open("sample.txt", "r") as f:
    data = f.read()

print(data)'''

#append data to file
'''with open("sample.txt","a") as f:
    f.write("\n"+input())
with open("sample.txt","r") as f:
    print(f.read())'''

#Count Characters in a File.
'''with open("sample.txt","r") as f:
    d=f.read()
print(len(d))'''

#Count Lines in a File.
'''
with open("sample.txt","r") as f:
    lines=f.readlines()
print(len(lines))'''

#Count Words
'''
with open("sample.txt","r") as f:
    d=f.read()
w=d.split()
print(len(w))'''

#Count Vowels in a File
'''
c=0
with open("sample.txt","r")  as f:
    d=f.read()
for i in d:
    if i in "aeiouAEIOU":
        c+=1
print(c)'''

#Copy File Contents
'''with open("sample.txt","r") as f:
    d=f.read()
with open("dog.txt","w") as f:
    f.write(d)
print(d)'''

#letter frequency
'''a = input()
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)'''
#find gratest and second gratest
'''a=set(list(map(int,input().split(','))))
b=sorted(a)
print(max(b))
print(b[-2])'''

#greeting function
'''def greet(name):
    print(("hello {}, welcome to python!").format(name))
greet("tejasri")'''
# Even or Odd
'''def num(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
n=int(input())
num(n)'''
        
#Find Maximum
'''a=int(input())
b=int(input())
c=int(input())
g=a
if b>g:
    g=b
if c>g:
    g=c
print(g)'''

#Count Vowels
'''def count(a):
    c=0
    for i in a:
        if i in "aeiouAEIOU":
            c=c+1
    print(c)
a=input()

count(a)'''

#Factorial
'''import math
def fact(a):
    print(math.factorial(a))
a=int(input())
fact(a)'''
#Prime Number Function
'''def prime(n):
    a=0
    for i in range(2,n):
        if n%i==0:
            a=1
    if a==0:
        print("prime")
    else:
        print("not prime")
n=int(input())
prime(n)'''
    
#Calculator Function
'''while True:
    def cal(a,b,c):
        if c=="+":
            print(a+b)
        elif c=="-":
            print(a-b)
        elif c=="*":
            print(a*b)
        elif:
            print(a/b)
        else:
            print('invalid operator')
    a=int(input())
    b=int(input())
    c=input("choose +,-,*,/")
    cal(a,b,c)'''
#Division with Exception Handling
'''try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except ZeroDivisionError:
    print('cannot divide by zero')
except ValueError:
    print('invalid input')
else:
    print('completed')
finally:
    print("operation ended")'''
    
#Integer Conversion
''''try:
    a=int(input())
    print(a)
except ValueError:
    print("Invalid output")
finally:
    print("over")'''

#List Index + Exception Handling
'''try:
    a=list(map(int,input().split()))
    b=int(input())
    print(a[b])
except IndexError:
    print("Index out of range")
finally:
    print("over")'''
#Multiple Exceptions
'''
try:
    a=int(input())
    b=int(input())
    print(a/b)

except ValueError:
    print("invalid input")

except ZeroDivisionError:
    print('division by zero')'''
#File Exception Handling
'''try:
    a=input()
    with open(a,"r")as f:
        print(f.read())
        
except FileNotFoundError:
    print('file not found')'''

#Math Module
'''import math
a=int(input())
print(math.sqrt(a))
print(math.factorial(a))
print(math.ceil(a))
print(math.floor(a))'''

#GCD and LCM
'''import math
a=int(input())
b=int(input())
print(math.gcd(a,b))
print(math.lcm(a,b))'''
#Random Number
'''import random
print(random.randint(1,100))'''
#Generate a 6-Digit OTP
'''import random
otp=random.randint(100000,999999)
print(otp)'''
#Calendar Module
'''import calendar
a=int(input())
b=int(input())
print(calendar.month(b,a))'''
#OS Module
'''import os
print(os.getcwd())
print(os.listdir())'''

#Regex: Find Digits
'''import re
a=input()
d=re.findall(r"\d+",a)
print(d)'''
#Regex: Find Vowels
'''
import re
a=input()
d=re.findall(r"[aeiouAEIOU]",a)
print(len(d))'''

#Regex: Validate Mobile Number
'''import re
a=input()
p="[0-9]{10}"
if re.fullmatch(p,a):
    print("valid")
else:
    print("Invalid")'''

#Validate Email
'''import re
a=input()
p="^[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
if re.fullmatch(p,a):
    print("valid")
else:
    print("invalid")'''

#Regex: Extract URLs
'''import re
a=input()
b=re.findall("https:\S+",a)
print(b)'''

#Regex: Capitalized Words
'''import re
a=input()
p=r"\b[A-Z][a-z]*\b"
b=re.findall(p,a)
print(b)'''
#File Handling: Write to a File
"""with open("sample.txt","w") as f:
    f.write(input())
    f.close"""
#Read a File
'''with open("sample.txt","r") as f:
    print(f.read())'''
#Count Characters in a File
'''with open("sample.txt","r") as f:
    d=f.read()
    print(len(d))'''
#Count Words in a File
'''with open("sample.txt") as f:
    d=f.read()
    c=d.split()
    print(len(c))'''
#Count Vowels in a File
'''
with open("sample.txt") as f:
    d=f.read()
c=0
for i in d:
    if i in "aeiouAEIOU":
        c+=1
print(c)'''

#Count Lines in a File
'''with open("sample.txt","r")as f:
          line=f.readlines()
          print(len(line))'''

#Copy File Contents

'''with open("sample.txt","r") as f:
    d=f.read()
    
with open("copy.txt","w") as f:
    f.write(d)'''

#Append Data to a File
'''with open("sample.txt","a") as f:
    f.write("\n"+"welcome to file handling")'''
#File Handling + Exception Handling
'''try:
    a=input()
    with open(a,"r") as f:
        print(f.read())
        
except:
    print("file not found")'''

#File Handling + Regex
'''import re
with open("sample.txt","w") as f:
    f.write("i have 20 mangoes and 20 apples")
with open("sample.txt","r") as f:
    d=f.read()
    c=re.findall("\d+",d)
    print(c)'''
#File + Regex: Find and Count Emails
'''import re
with open("sample.txt","w") as f:
    f.write("my email is teja@gmai.com and one more is dsri@gmail.com")
with open("sample.txt","r") as f:
    d=f.read()
    p=r"[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    c=re.findall(p,d)
    print(c)
    print(len(c))'''

#File + Regex: Find Phone Numbers
'''import re
with open("sample.txt","w") as f:
    f.write("Contact 9876543210 or 9123456789")
with open("sample.txt","r") as f:
    d=f.read()
    p=r"\d{10}"
    c=re.findall(p,d)
    print(c)'''

#File + Regex: Count Vowels
'''
import re
with open("sample.txt","w") as f:
    f.write("Python is amazing")
with open("sample.txt","r") as f:
    d=f.read()
    c=re.findall(r"[AEIOUaeiou]",d)
    print(c)
    print(len(c))'''

#Mini Project: Student File Analyzer
'''import re
a=input()
with open("student.txt","w") as f:
    f.write(a)
with open("student.txt","r") as f:
    d=f.read()
    p="[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    c=re.findall("\d+",d)
    e=re.findall(p,d)
    print(c)
    print(len(c))
    print(e)
    print(len(e))'''



























