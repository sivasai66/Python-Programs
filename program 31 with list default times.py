Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[10,20,30]
>>> insert (2,1)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    insert (2,1)
NameError: name 'insert' is not defined
>>> append()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    append()
NameError: name 'append' is not defined
>>> append(10)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    append(10)
NameError: name 'append' is not defined
>>> append(10) in l
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    append(10) in l
NameError: name 'append' is not defined
>>> l.append(10)
>>> print l
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(l)?
>>> l
[10, 20, 30, 10]
>>> del l[0]
>>> l
[20, 30, 10]
>>> l.pop()
10
>>> l.push()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l.push()
AttributeError: 'list' object has no attribute 'push'
>>> l
[20, 30]
>>> l.push(10)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l.push(10)
AttributeError: 'list' object has no attribute 'push'
>>> l.clear
<built-in method clear of list object at 0x000001D8F94D5180>
>>> l
[20, 30]
>>> l.insert(2.100)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l.insert(2.100)
TypeError: insert expected 2 arguments, got 1
>>> l.insert(2,100)
>>> l
[20, 30, 100]
>>> l.clear()
>>> l
[]
>>> l=[10,22,1,2,34,4,5]
>>> l.sort()
>>> ls
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> l
[1, 2, 4, 5, 10, 22, 34]
>>> l.reverse()
>>> l
[34, 22, 10, 5, 4, 2, 1]
>>> l.sum()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    l.sum()
AttributeError: 'list' object has no attribute 'sum'
>>> l
[34, 22, 10, 5, 4, 2, 1]
>>> l.min()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    l.min()
AttributeError: 'list' object has no attribute 'min'
>>> l.min(0:3)
SyntaxError: invalid syntax
>>> l.min(0,3)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l.min(0,3)
AttributeError: 'list' object has no attribute 'min'
>>> pow2 = []
for x in range(10):
   pow2.append(2 ** x)
   
SyntaxError: multiple statements found while compiling a single statement
>>> pow2 = []
>>> for x in range(10):
	 pow2.append(2 ** x)

   
>>> pow2
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
>>> l.min_ele
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    l.min_ele
AttributeError: 'list' object has no attribute 'min_ele'
>>> min(l)
1
>>> ls
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> l
[34, 22, 10, 5, 4, 2, 1]
>>> 