Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #program to demonstrate the Directory operations
>>> #program 32
>>> d={}
>>> d
{}
>>> type (d)
<class 'dict'>
>>> d.keys()
dict_keys([])
>>> len(d)
0
>>> d.items()
dict_items([])
>>> d
{}
>>> d[key]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d[key]
NameError: name 'key' is not defined
>>> d1={}
>>> d1=d.copy()
>>> d1
{}
>>> d1={1,2,3,4,5}
>>> d1
{1, 2, 3, 4, 5}
>>> d1clear()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d1clear()
NameError: name 'd1clear' is not defined
>>> d1.clear()
>>> d.setdefault(key)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d.setdefault(key)
NameError: name 'key' is not defined
>>> d.update
<built-in method update of dict object at 0x0000019DA1D984C0>
>>> d.update()
>>> d.update(1,2,3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.update(1,2,3)
TypeError: update expected at most 1 argument, got 3
>>> d
{}
>>> d.update(x=100,y=2)
>>> d
{'x': 100, 'y': 2}
>>> d.update(4658,100)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d.update(4658,100)
TypeError: update expected at most 1 argument, got 2
>>> d.update([(10,20)])
>>> d
{'x': 100, 'y': 2, 10: 20}
>>> d1
set()
>>> d.clear
<built-in method clear of dict object at 0x0000019DA1D984C0>
>>> d1.clear()
>>> d1={"name":"Siva"}
>>> d.update(d1)
>>> d
{'x': 100, 'y': 2, 10: 20, 'name': 'Siva'}
>>> 