Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={'name','teja','year':20276,'month':7}
SyntaxError: invalid syntax
a={'name','teja','year':2026,'month':7}
SyntaxError: invalid syntax
a={"name","teja","year":2026,"month":7}
SyntaxError: invalid syntax
a={"name":"teja","year":2026,"month":7}
a
{'name': 'teja', 'year': 2026, 'month': 7}
print(type(a))
<class 'dict'>
a.update({"time":2})
a
{'name': 'teja', 'year': 2026, 'month': 7, 'time': 2}
a.update({"time":2},{"day":'true"})
                     
SyntaxError: unterminated string literal (detected at line 1)
a.update({"time":2,"day":"true"})
                     
a
                     
{'name': 'teja', 'year': 2026, 'month': 7, 'time': 2, 'day': 'true'}
{'name': 'teja', 'year': 2026, 'month': 7, 'time': 2, 'day': 'true'}
                     
{'name': 'teja', 'year': 2026, 'month': 7, 'time': 2, 'day': 'true'}

a={"name":"teja","city":"vij"}
                     
a.setdefault("mail":"tejasrikadavakollu16@gmail.com")
                     
SyntaxError: invalid syntax
a.setdefault("mail","tejasrikadavakollu16@gmail.com")
                     
'tejasrikadavakollu16@gmail.com'
a
                     
{'name': 'teja', 'city': 'vij', 'mail': 'tejasrikadavakollu16@gmail.com'}
#pop------
                     
a={"state":"ap","country":"india"}
                     
a.pop("country")
                     
'india'
a
                     
{'state': 'ap'}
a.popitem()
                     
('state', 'ap')
a
                     
{}
a={"color":"purple","food":"rasam rice"}
                     
a.copy()
                     
{'color': 'purple', 'food': 'rasam rice'}
len(a)
                     
2
b=a.copy()
                     
b
                     
{'color': 'purple', 'food': 'rasam rice'}
a={"name":"teja","city":"vij","name":"teja"}
                     
a
                     
{'name': 'teja', 'city': 'vij'}
a={"name":"teja","city":"vij","name":"sri"}
                     
a
                     
{'name': 'sri', 'city': 'vij'}
a={"name":"teja","city":"vij","name1":"teja"}
                     
a
                     
{'name': 'teja', 'city': 'vij', 'name1': 'teja'}
a.count("name")
                     
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
a.index('city')
                     
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.index('city')
AttributeError: 'dict' object has no attribute 'index'
a.clear()
                     
a
                     
{}
b={}
                     
b.update({"name":"pooja"})
                     
b
...                      
{'name': 'pooja'}
>>> b.update({"name":"teja","city":"vij"})
...                      
>>> b
...                      
{'name': 'teja', 'city': 'vij'}
>>> a={"idno":[10,20,30],"names":['sai','teja],'aadhya'],"marks":[60,70,80]}
...                               
SyntaxError: unterminated string literal (detected at line 1)
>>> a={"idno":[10,20,30],"names":['sai','teja,'aadhya'],"marks":[60,70,80]}
...                               
SyntaxError: unterminated string literal (detected at line 1)
>>> a={"idno":[10,20,30],"names":['sai','teja','aadhya'],"marks":[60,70,80]}
...                               
>>> a
...                               
{'idno': [10, 20, 30], 'names': ['sai', 'teja', 'aadhya'], 'marks': [60, 70, 80]}
>>> type(a)
...                               
<class 'dict'>
>>> a.keys()
...                               
dict_keys(['idno', 'names', 'marks'])
>>> a.values()
...                               
dict_values([[10, 20, 30], ['sai', 'teja', 'aadhya'], [60, 70, 80]])
>>> 
>>> a.items()
...                               
dict_items([('idno', [10, 20, 30]), ('names', ['sai', 'teja', 'aadhya']), ('marks', [60, 70, 80])])
