#oops
#syntax
'''class classname():
    #attributes
    name="pooja"
    age=28
    place="vij"
    def fname(method_name):
        print("statements")
a=classname()
print(dir(a))
f.name()'''
#class declaration
'''class Details():
    name="teja"
    age=21
    place="vij"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#object instantiation
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("pushpa",22,"vij")
a.display()
b=Details()
b.data("barani",22,"vij")
b.display()
c=Details()
c.data("devi",22,"vij")
c.display()'''

#object initialization
'''class Data():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)

a=Data("devi",22,"vij")
print(dir(a))
a.display()'''
#user input
'''class Data():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Data(input("name"),int(input("age")),input("place"))
print(dir(a))
a.display()'''

'''class Data():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Data()
print(dir(a))
a.display()'''


#diff b/w _and__
'''class employee():
    def __init__(self):
        self.name="teja"
        self._mailid="teja@gmail.com"
        self.__salary=50000# privte variable
a=employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._employee__salary)'''

'''
class Employee():
    def __init__(self):
        self.name="teja"
        self._mailid="teja@gmail.com"
        self.__salary=50000# privte variable
class Employee1():
    def __init__(self):
        self.name="sai"
        self._mailid="sai@gmail.com"
        self.__salary=50000
        
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee__salary)
b=Employee1()
print(dir(b))
print(b.name)
print(b._mailid)
#print(a.__salary)
print(b._Employee1__salary)'''
#polymorphism
#operator overloading
'''a=4;b=8
print(a+b)
print(a.__add__(b))
print(a.__sub__(2))
print(a.__mul__(6))
print(a.__pow__(2))
#print(a.__div__(b))
print(a.__eq__(4))
print(a.__le__(8))
print(a.__ge__(10))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())'''
#operator overrideing
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class A():
    def __init__(self,a):
        self.a=a
x=A(6)
y=B(4)
#x=6
#y=4
print(x+y)'''

#Method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("product is",a*b)
        else:
            print("problem ends......")
a=new()
a.sum()
a.sum(3,6,8)
a.sum(4,5)'''
#method overriding
'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dogs can bark")
a=Animal()    
b=Dog()
a.speak()
b.speak()'''
    


'''class car():
    def vehicle(self):
        print("My fav one is Thar")
class bike():
    def vehicle(self):
        print("my fav one is black bullet")
a=car()
b=bike()
a.vehicle()
b.vehicle()'''

#inheritance
#single inheritance
'''class rbi():
    cash=100000
    def available_cash(cls):
        print('available cash is',cls.cash)
        print('available cash is',rbi.cash)
class sbi(rbi):
    pass
class hdfc(rbi):
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+rbi.cash)
a=hdfc()
a.available_cash()
a.new_cash()'''

#multiple inheritance
'''class father():
    a=5.9
    def height(self):
        print('father height is',father.a)
class mother():
    b=60
    def weight(self):
        print('mother weight is',mother.b)
class kid(father,mother):
    c=just born....
    def dob(self):
        print("date of bith of child is",kid.c)
d=kid()
d.height()
d.weight()
d.dob()'''

#multilevel inheritance
'''class grandparent():
    def land(self):
        print("1 acre land")
class parent(grandparent):
    def house(self):
        print("100sqft")
class child(parent):
    def bike(self):
        print("pulsar")
a=child()
a.land()
a.house()
a.bike()'''

#hierarchical inheritance
'''class employee():
    def company(self):
        print("codegnan")
class trainer(employee):
    def teching(self):
        print("python")
class developer(employee):
    def student(self):
        print("student")
    
a=trainer()
a.company()
a.teching()
b=developer()
b.company()
b.student()'''

#hybrid inheritance
'''class person():
    def details(self):
        print('i am a person')
class trainer(person):
    def teaching(self):
        print('i am teaching')
class student(person):
    def student(self):
        print('i am learning')
class programmanager(trainer,student):
    def manager(self):
        print('i am manager')
b=programmanager()
b.details()
b.teaching()
b.student()
b.manager()'''




#super function
'''class parent():#super class
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):#sub class
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("pooja",28)
print(a.age)
print(a.name)'''


#Encapsulation
#combing multiple units in to single unit
#public
'''class a():
    publicdata=1000
    def method1(self):
        print(self.publicdata)
class b(a):
    def method2(self):
        print(self.publicdata)
obj1=b()
obj1.method1()
obj1.method2()'''

#_protected data
'''class a():
    _protecteddata=10
    def method1 (self):
        print(self._protecteddata)
class b(a):
    def method2(self):
        print(self._protecteddata)
obj1=b()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#__privatedata
'''class a():
    __privatedata="Teja"
    def method1(self):
        print(self.__privatedata)
class b(a):
    def method2(self):
        print(self._a__privatedata)
obj1=b()
obj1.method1()
obj1.method2()'''

#abstraction
'''class a():
    def method1(self):
        pass
obj1=a()
obj1.method1()'''

'''class a():
    def method1(self):
        print("data")
obj1=a()
obj1.method1()'''
'''from abc import ABC,abstractmethod
class a():
    @abstractmethod
    def method1(self):
        print('python course')
obj1=a()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def method1(self):
        print("data science")
obj1=a()
obj1.method1()'''

from abc import ABC,abstractmethod
class a(ABC):
    def method1(self):
        pass
    def method2(self):
        print("python full stack")
    def method3(self):
        pass
class b(a):
    def method1(self):
        print("dat structures")
    def method3(self):
        print("java full stack")
obj1=b()
obj1.method1()
obj1.method2()
obj1.method3()
    











































