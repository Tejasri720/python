'''def greetings(name):
    print("welcome",name)'''
'''
a=int(input("a value"))
b=int(input("b value"))
print("the  sum is",a+b)
'''

'''
details={"idno":[10,20,30],
         "names":["teja","pushpa","devi"],
         "marks":[50,40,30]}'''

'''
if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)'''
'''
def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program run as module")
dummy()'''

#math module
'''
import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,4))
print(math.log(2))
print(math.tan(45))
print(math.sin(60))
print(math.cos(30))
print(math.ceil(2.9))
print(math.ceil(3))
print(math.floor(2.7))
print(math.cbrt(2))'''
'''
from math import pi,log,sqrt
print(pi)
print(log(10))
print(sqrt(2))'''

#sys module
'''
import sys
print(sys.path)
print(sys.version)'''

#os module
import os
'''
print(os.path)
print(os.getcwd())
print(os.listdir())'''
'''
print(os.mkdir("oct16"))
print(os.listdir())'''
'''
print(os.chdir("C:\\Users\\lenovo\\Downloads"))
print(os.listdir())'''

#Ascii
'''
print(chr(67))
print(chr(65))
print(chr(90))
print(chr(93))
print(ord("a"))
print(ord("z"))
#print(ord(97))#error
print(chr(97))'''
'''
for i in range(97,123):
    print(chr(i),end=" ")'''
'''
for j in range(65,91):

    print(chr(j),end=" ")'''
#print our name
'''

a=input()'''
'''
b=[]
for i in a:
    b.append(ord(i))
print(a,b)'''
'''
for i in a:
    print(i,"-",ord(i))'''

#random module
#random module is used to generate random numbers in python ,randinit fun() is used
#and this function is defined in random module
#simple
'''
import random
a=random.sample(range(10,50),10)
print(a)'''
#randint()
'''
import random
a=random.randint(40,50)
print(a)'''
#choice
'''
import random
b=[10,20,30,40,50]
a=random.choice(b)
print(a)'''


#task
'''
import random
a=random.randint(1,6)
print(a)
o=input("choose 1.yes or 2.no")
if o=="1":
    continue
else:
    break'''
'''
import random
while True:
    input("enter the roll of dice")
    a=random.randint(1,6)
    print(a)
    option=input("roll again? (y/n)")
    if option=="y":
        continue
    elif option=="n":
        break
    else:
        print("invalid")'''

import calendar
'''
year=2026
month=8
print(calendar.month(year,month))'''
'''
year=2026
print(calendar.calendar(year))'''
'''   
a=int(input("enter year"))
b=int(input("enter month"))
print(calendar.month(a,b))'''

 #date and time
'''
from datetime import date
a=date.today()
print(a)'''
'''
import datetime
a=datetime.datetime.now()
print(a)'''
'''
#epoch time
import time
a=time.time()
print(a)#epoch time
b=time.localtime(a)
print(b)
print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"time{b.tm_hour}:{b.tm_min} :{b.tm_sec} ")
print(f"day is {b.tm_wday} -{b.tm_yday} -{b.tm_isdst}")'''


import random
import time
'''
a=random.sample(range(1,11),10)
for i in a:
    c=time.sleep(2)
    print(i)'''
'''
for i in range(10):
    a=random.randint(20,40)
    print(a)
    time.sleep(2)'''



#regex(regular expressions)
'''
a="codegnan is in vij"
print(a)'''
'''
a="codegnan\nis\tin\nvija"
print(a)'''

#rstring
'''a=r"codegnan\nis\tin\nvija"
print(a)'''

#compile(),search(),findall(),split(),sub
#sequence characters
'''
\w->it matches alpha numeric
\W->it matches non-alpha numeric
\d-> it matches any digit
\D-> it matches non digit
\s->it represents white spaces
\S->iter represents non-white spaces  '''

#compile()
import re
#a="map maths cat code cash money mat cup cap monkey"
'''b=re.compile(r"m\w\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)'''
'''
b=re.search(r"m\w+",a)
print(b)


#findall
c=re.findall(r"m\w+",a)
print(*c)

c=re.findall(r"c\w+",a)
print(*c)

c=re.findall(r"\w+",a)
print(*c)

#split()
d=re.split(r"m",a)
print(d)

e=re.split(r"\s",a)
print(e)

e=re.split(r"\s",a)
print(e)
#sub()
f=re.sub(r"m","a",a)           
print(f)'''
'''          
a="1 3 c 5 4 s r t"
b=re.search(r"\d+",a)
print(b)

c=re.findall(r"\d+",a)
print(*c)

c=re.findall(r"\D+",a)
print(*c)

c=re.findall(r"\W+",a)
print(*c)'''














