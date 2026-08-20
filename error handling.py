#error handling
#syntax error
'''for i in range(20)
print(i)'''

#runtime error
'''a=int(input())
b=int(input())
print(a//b)'''#10//0->zero division error

#logical error
'''a=10
b=20
print(a-b)'''

#exception handling
'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("expection raised")
    else:
        print("no else block")
    finally:
        print("program ends.............")'''

#file handling
#write()
'''
a=open("teja.txt","w")
b=a.write("python full stack")
a.close()'''

'''
a=open("teja.txt","w")
b=a.write("codegnan it solutions")
a.close()'''

#append
'''a=open("teja.txt","a")
b=a.write("\tteja")
a.close()'''
#user method
'''
a=open("teja.txt","w")
a.write(input("data"))
a.close()'''
'''
a=open("teja.txt","w")
b=input("data")
a.write(b)
a.close()'''
'''
a=open("teja.txt","w")
a.write(input("data"))
a.close()'''

#readlines()
'''
a=open("teja.txt")
#print(a.read())# it will display entire content
#print(a.readline())#it will display first line
#print(a.readlines())#it will display in list with\n
print(a.read(7))#it will display no .of characters'''
#writelines()->it mks every object side by side
'''a=open('sri.txt','w')
b=["pushpa","devi","bharani"]
a.writelines(b)
a.close()'''
'''
a=open('sri.txt','w')
b=["pushpa","devi","bharani"]
a.writelines("\n".join(b))
a.close()'''
'''
a=open("ifelse.py")
print(a.read())'''
'''
a=open("C:\\Users\\lenovo\Desktop\\pfs38\\functions.py")
print(a.read())'''


















