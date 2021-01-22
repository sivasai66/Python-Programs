Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t=(1,2,3)
>>> type(t)
<class 'tuple'>
>>> t.count(value)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.count(value)
NameError: name 'value' is not defined
>>> t.count()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> len(t)
3
>>> str(t)
'(1, 2, 3)'
>>> t.count(value)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t.count(value)
NameError: name 'value' is not defined
>>> t.index(value)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t.index(value)
NameError: name 'value' is not defined
>>> value=9
>>> t.count(value)
0
>>> t.index(value)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t.index(value)
ValueError: tuple.index(x): x not in tuple
>>> t*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> sum(t)
6
>>> min(t)
1
>>> 