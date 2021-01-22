Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={}
>>> s1={1,2,3,4}
>>> s1
{1, 2, 3, 4}
>>> len(s1)
4
>>> s1.add(value)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s1.add(value)
NameError: name 'value' is not defined
>>> s1.add(10)
>>> s1
{1, 2, 3, 4, 10}
>>> s2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s2
NameError: name 's2' is not defined
>>> s1.union(s2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s1.union(s2)
NameError: name 's2' is not defined
>>> s2=()
>>> s1.union(s2)
{1, 2, 3, 4, 10}
>>> s2
()
>>> s1.intersection(s2)
set()
>>> s1
{1, 2, 3, 4, 10}
>>> s.discard(1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.discard(1)
AttributeError: 'dict' object has no attribute 'discard'
>>> s1.discard(1)
>>> s1
{2, 3, 4, 10}
>>> s1.update({10,23,45})
>>> s1
{2, 3, 4, 10, 45, 23}
>>> s
{}
>>> s1.pop
<built-in method pop of set object at 0x000002746C54B9E0>
>>> s1.pop()
2
>>> s1
{3, 4, 10, 45, 23}
>>> 