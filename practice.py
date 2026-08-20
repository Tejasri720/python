'''a="Tejasri"
b=21
print("My name is {} and I am {} years old".format(a,b))
'''
"""
a=input()
print("My favourite programming is {}".format(a))
"""
'''
a=input()
b=input()
print("[Brand: {} Model:{}]".format(a,b))'''
'''
a=10
b=5
c=a*b
print("area of rectangle with length {} and width {} is {}.".format(a,b,c))
'''
'''
temp = 35
print(f"Today's temperature is {temp}\u00B0C.")'''
'''
a=input()
b=int(input())
c=int(input())
d=int(input())
print("Name: {}\nmath: {}\nscience: {}\nEnglish: {}".format(a,b,c,d))
'''
'''
a="Ravi"
b=450.756
print("customer {} has to pay Rs.{:.2f}".format(a,b))

'''
'''
a=7
print("{:03}".format(a))'''
'''
a="python"
b=a.upper()
print(b)'''
'''
a="pyTHOn"
b=a.lower()
print(b)
'''
'''
a="python programming"
b=a.capitalize()
print(b)'''

'''
a="python is easy"
b=a.title()
print(b)'''
'''
a="pYThOn"
b=a.swapcase()
print(b)
'''
'''
a=input()
print(a.count('a'))
'''
'''
a="programming"
b=a.find("g")
print(b)'''
'''
a="banana"
print(a.rfind("a"))'''
'''
a="python programming"
d=a.startswith("python")
print(d)'''
'''
a="hello.py"
d=a.endswith("py")
print(d)'''
'''
a="i like java"
d=a.replace("java" ,"python")
print(d)'''
'''
a="python"
c=a.strip().upper()
print(c)'''
'''
a="HELLO WORLD"
c=a.strip().lower()
print(c)'''

'''
a="i love java"
c=a.replace("java","python").upper()
print(c)'''

'''
a="ApPle And BAnAnA"
c=a.lower().count("a")
print(c)'''
'''
a="  python programming"
c=a.strip().startswith("python")
print(c)'''
'''
a="python full stack"
c=a.replace(" ","_").upper()
print(c)'''
'''
a="  welcome to python programming"
c=a.strip().title()
print(c)'''
'''
a="I LOVE CODE"
C=a.lower().find("code")
print(C)'''
'''
a="Batch 2025"
c=a.replace("2025","2026").endswith("2026")
print(c)'''
'''
a="  Hello World  "
c=a.strip().count("o")
print(c)'''
'''
text = "  PyThOn  "
print(text.strip().lower().replace("python", "java").upper())

'''
'''
#list practice
a=list(map(str,input().split()))
print(a)'''
'''
a=list(map(int,(input().split())))
print(a)'''
'''
a=list(map(int,input().split()))
print(a[0],a[-1])'''
'''
a=list(map(int,input().split()))
b=len(a)
print(b)'''
'''
a=list(map(str,input().split()))
a.append("python")
print(a)'''
'''
a=list(map(int,input().split()))
a.insert(2,100)
print(a)'''

'''a=list(map(str,input().split()))
a.pop(-1)
print(a)'''
'''
a=list(map(str,input().split()))
a.remove("apple")
print(a)'''
'''
a=list(map(str,input().split()))
a.clear()
print(a)'''
'''
a=list(map(str,input().split()))
if "25" in a:
    print(True)
else:
    print(False)'''
'''
a=list(map(str,input().split()))
b=a.count("5")
print(b)'''
'''
a=list(map(str,input().split()))
b=a.index("banana")
print(b)'''
'''
a=list(map(str,input().split()))
a.reverse()
print(a)'''

'''a=list(map(str,input().split()))
a.sort()
print(a)'''
'''
a=list(map(str,input().split()))
a.sort(reverse=True)
print(a)'''
'''
a=list(map(str,input().split()))
b=a.copy()
print(b)'''
'''
a=list(map(str,input().split()))
b=list(map(str,input().split()))
a.extend(b)
print(a)
'''
'''
a=list(map(int,input().split()))
for i in a:
    if  i%2==0:
        print(i, end=" ")'''
'''
a=list(map(str,input().split()))
b=max(a)
print(b)
'''
'''
a=list(map(str,input().split()))
b=min(a)
print(b)'''
'''
a=list(map(int,input().split()))
b=sum(a)
print(b)'''
'''
a=list(map(str,input().split()))
b=0
for i in a:
    if i.lower() in "'a','e','i','o','u'":
        b=b+1
print(b)'''
'''
a=list(map(str,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)'''
'''
a=list(map(str,input().split()))
b=list(map(str,input().split()))
a.extend(b)
a.sort()
print(a)'''
'''
a=list(map(str,input().split()))
a.sort()
print(a[-2])'''
'''
a=list(map(int,input().split()))
k=int(input())
a=a[k:]+a[:k]
print(a)'''
'''
a=list(map(int,input().split()))
k=int(input())
a=a[-k:]+a[:-k]
print(a)'''
'''
a = list(map(int, input().split()))
k = int(input())

#k = k % len(a)

for i in range(k):
    l = a.pop()
    a.insert(0, l)

print(a )'''

'''
a = list(map(str, input().split()))
b=[]
for i in range(len(a)-1,-1,-1):
    b.append (a[i])
print(b)'''
'''
a = list(map(str, input().split()))
b= list(map(str, input().split()))
if  a==b:
    print(True)
else:
    print(False)'''

'''   
a = list(map(str, input().split()))
b = list(map(str, input().split()))
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)'''
'''
a=input().split()
print(a[0])
print(a[-1])
print(len(a))'''

'''
b=list(map(int,input().split()))
c=sum(b)
print(max(b))
print(min(b))
print(c)'''
'''
for i in range(1,20):
    if i%2==0:
        print(i,end=" ")'''

    
'''  
a=tuple(map(int,input().split()))
print(a[1])
print(a.count(10))
print(a.index(20))'''
'''
#a=int(input())
c=[i*i for i in range(1,11)]
print(c)'''
'''
name, age, course = input().split()
print(name, age, course)'''
#mul
'''
a,b=(map(int,input().split(" ")))
print(a*b)'''
#max
'''
a=list(map(int,input().split()))
print(max(a))'''
#odd r even
'''
a=int(input())
if a%2==0:
    print("even")
else:
    print("odd")'''

#vowel count
'''a=input()
c=0
for i in a:
    if i in "aeiou":
        c=c+1

print(c)'''

#reverse a string
'''
a=input()
print(a[::-1])'''
'''
a=input()
if a==a[::-1]:
    print("palindrome")
else:
    print("not palindrome")'''

#print even numbers
'''
for i in range(2,11,2):
    print(i,end=" ")'''
'''
n=int(input())
for i in range(5,51,5):
    print(i)'''
'''
import math'''
'''
print(math.factorial(5))'''
'''
a=6
b=list(map(int,input().split()))
print(max(b))'''
'''
a=list(map(int,input().split()))
b=set(a)
for i in b:
    print(i,end=" ")'''
'''
def fun(name="welcome to python"):
    print(Hello,name)
fun()'''


'''  
def display(name):
    print("hello",name)
name=input()
display(name)'''
'''
def fun(a,b):
    print(a+b)
a=int(input())
b=int(input())
fun(a,b)'''
'''
def fun(a):
    print(a*a)
a=int(input())
fun(a)'''
'''
def fun():
    if a%2==0:
        print("even")
    else:
        print("odd")
a=int(input())
fun()'''
'''
def fun():
    if a>b:
        print("a is  greater")
    else:
        print("b is greater")
a=int(input())
b=int(input())
fun()'''

'''
def fun():
    if a<b and a<c:
        print(a)
    elif b<a and b<c:
        print(b)
    else:
        print(c)
a=int(input())
b=int(input())
c=int(input())
fun()
'''
'''
import  math
def fun():
    print(math.factorial(a))
a=int(input())
fun()'''

'''

def fun():
    print(a[::-1])
a=input()
fun()'''
'''
def fun():
    c=0
    for i in a:
        if i in "aeiou":
            c=c+1
    print(c)
a=input()

fun()'''





import re
'''
a=input()
p="[A-Za-z]+"
if re.fullmatch(p,a):
    print("valid")
else:
    print("Invalid")'''

'''
a=input()
if re.fullmatch("\d+",a):
    print("valid")
else:
    print("invalid")'''

'''
a=input()
p="[AEIOU-aeiou]+"
c=0
for i in a:
    if re.fullmatch(p,i):
        c=c+1
print(c)

'''
'''
import re

text = input()

vowels = re.findall(r"[aeiouAEIOU]", text)

print(len(vowels))'''

'''
a=input()
b=re.findall("\d+",a)
print(b)'''
'''
a=input()
b=re.findall("\w+",a)
print(b)'''

'''
a=input()
b=re.findall("[a-z0-9_]+@[a-z]{2,}",a)
print(b)
'''
'''
a=input()

if re.fullmatch("\d{10}",a):
    print("Valid")
else:
    print("Invalid")'''
'''
a=input()
b=re.findall("#\w+",a)
print(*b)'''
#Extract Dates (dd-mm-yyyy)
'''a=input()
b=re.findall("\d{2}-\d{2}-\d{4}",a)
print(b)'''
#Find Words Ending with "ing"
'''a=input()
b=re.findall("\w+ing",a)
print(b)'''
#Remove All Special Characters
'''
a=input()
b=re.sub("[^A-Za-z0-9]","",a)
print(b)'''

#Find Repeated Words
'''
a=input()
b=re.findall(r"\b(\w+)\s+\1\b",a)#here using of r is complesary
print(b)'''

#Replace Multiple Spaces with a Single Space
'''a=input()
b=re.sub("\s+"," ",a)
print(b)'''

#Extract Currency Values
'''a=input()
b=re.findall("₹\d+",a)
print(b)'''

#Validate a Strong Password
'''
a = input()
p = r"[A-Za-z0-9@!#$%^&*]{8,}"
if re.fullmatch(p, a):
    print("Strong")
else:
    print("Weak")'''

#Extract All URLs
'''a = input()
b = re.findall(r"https\S+", a)
print(b)'''

#Math Module
'''
import math
a=int(input())
print(math.sqrt(a))
print(math.factorial(a))
print(math.ceil(a))
print(math.floor(a))'''
'''
import math
a=int(input())
b=int(input())
print(math.gcd(a,b))
print(math.lcm(a,b))'''
#Generate a Random Number
'''
import random
a=random.randint(1,1000)
print(a)'''

#Randomly Choose an Item from a List
'''
import random
a=input().split()
a=random.choice(a)
print(a)'''

#Shuffle a List
'''import random
n = list(map(int, input().split()))
random.shuffle(n)
print(n)'''

#Print the Calendar of a Given Year
'''
import calendar
a=int(input())
print(calendar.calendar(a))'''


#Print the Calendar of a Specific Month
'''import calendar
a=int(input())
b=int(input())
print(calendar.month(b,a))'''

#Check Whether a Year is a Leap Year
'''a=int(input())
if a%4==0 :
    print('leap year')
else:
    print('not leap year')'''
'''
import calendar
a=int(input())
if calendar.isleap(a):
    print('leap year')
else:
    print('not leap year')'''

#Print the Current Working Directory
'''import os
print(os.getcwd())'''

#List All Files and Folders in the Current Directory
'''
import os
print(os.listdir())'''

#Create a New Folder
'''import os
os.mkdir("p")
print("folder create successfully")'''
#Rename a File
'''import os
os.rename('demo.txt','python.txt')#given file name should be in your system
print("file rename successfully")'''

#Division by Zero — Easy
'''try:
    a=int(input())
    b=int(input())
    c=a/b
except:
    print("Cannot divie by zero")'''

#Integer Conversion
'''try:
    a=input()
    c=int(a)
except:
    print("Invalid input")'''

#Division with Multiple Exceptions
'''try:
    a=int(input())
    b=int(input())
    print(a/b)
except ValueError:
    print("please enter the number")
except ZeroDivisionError:
    print("cannot divide by zero")'''

#List Index Error
'''try:
    a=list(map(int,input().split()))
    b=int(input())
    print(a[b])
except:
    print('Index error')'''

#Dictionary Key Error
'''m={}
n=int(input("enter"))
for i in range(n):
    s=input("enter")
    mark=int(input("enter"))
    m[s]=mark
try:
    search=input("enter")
    print(m[search])
except:
    print("subject not found")'''

#Multiple Exceptions
try:
    a=int(input())
    b=int(input())
    c=int(input())
    


    
    

























