'''a = input("Enter ")
b = ""
for i in range(len(a) - 1, -1, -1):
    rev = b + a[i]
print(b)'''

'''a=input()
for i in a:
    print(i,end="|")'''

'''
a = input("Enter")
c = ""
for i in a:
    if i not in c:
        print(i, a.count(i), end="")
        c = c + i'''

'''a = input("Enter ")
d=int(input())
b = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
}
c= (b[a]+d)%7
print(list(b.keys())[c])'''
'''
a=list(map(int,input().split()))
b=int(input())
c = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == b:
            c.append([a[i], a[j]])
print(c)
'''
#even or odd
'''a=int(input())
if a%2==0 :
    print("even")
else:
    print("odd")'''

#Largest of Three Numbers
'''a=int(input())
b=int(input())
c=int(input())
g=a
if b>g:
    g=b
if c>g:
    g=c
print(g)'''

#The Second Largest
'''a=int(input()) 
b=list(map(int,input().split()))
c=set(b)
d=sorted(c)
print(d[-2])'''

'''n = int(input())
a = list(map(int, input().split()))
largest = None
second = None
for i in a:
    if largest is None or i > largest:
        second = largest
        largest = i
    elif i != largest and (second is None or i > second):
        second = i
#print(largest)
if second is None:
    print(-1)
else:
    print(second)'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

#First Non-Repeating Character
'''a=input()
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key, value in d.items():
    if value==1:
        print(key)
        break
        
else:
    print("-1")'''
#method used
'''a = input()

for i in a:
    if a.count(i) == 1:
        print(i)
        break
else:
    print(-1)'''


#Longest Consecutive Increasing Sequence
'''n = int(input())
a = list(map(int, input().split()))
c = 1
m = 1
for i in range(n - 1):
    if a[i] + 1 == a[i + 1]:
        c += 1
    else:
        c = 1

    if c > m:
        m = c
print(m)'''

#Missing Number
'''n=int(input())
a=list(map(int,input().split()))
b=n*(n+1)//2
c=sum(a)
print(b-c)'''

#Anagram Check
'''a=input()
b=input()
d={}
e={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for j in b:
    if j in e:
        e[j]+=1
    else:
        e[j]=1
if d==e:
    print(True)
else:
    print(False)'''

#Second Largest Distinct Number
'''n=int(input())
a=list(map(int,input().split()))
largest=None
second=None
for i in a:
    if largest is None or i>largest:
        second=largest
        largest=i
    elif i !=largest and (second is None or i<second):
        second=i
if second is None:
    print(-1)
else:
    print(second)'''

#Majority Element
'''n=int(input())
a=list(map(int,input().split()))
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key,value in d.items():
    if value>(n/2):
        print(key)
        break
else:
    print(-1)'''

#Method Overriding
'''class animal():
    def sound(self):
        print("animals makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
a=animal()
b=dog()
a.sound()
b.sound

'''
#Method Overriding + super()
'''class person():
    def display(self):
        print("i am person")
class student(person):
    def display(self):
        super().display()
        print("i am a student")
a=person()
b=student()
a.display()
b.display()'''

#Multiple Child Classes
'''class animal():
    def sound(self):
        print('animals make sound')
class dog(animal):
    def sound(self):
        print('dog barks')
class cat(animal):
    def sound(self):
        print("cat meows")
class cow(animal):
    def sound(self):
        print("cow ambaa")
a=animal()
b=dog()
c=cat()
e=cow()
d=int(input())
if d==1:
    a.sound()
elif d==2:
    b.sound()
elif d==3:
    c.sound()
elif d==4:
    e.sound()
else:
    print('none')'''

#Duck Typing
class animal():
    def sound(self):
        print('animals make sound')
class dog(animal):
    def sound(self):
        print('dog barks')
class cat(animal):
    def sound(self):
        print("cat meows")
class cow(animal):
    def sound(self):
        print("cow ambaa")
a=animal()
b=dog()
c=cat()
e=cow()























