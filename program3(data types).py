Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=2
>>> type(a)
<class 'int'>
>>> b=2.5
>>> type(b)
<class 'float'>
>>> print(type(b))
<class 'float'>
>>> type b
SyntaxError: invalid syntax
>>> type(b)
<class 'float'>
>>> c=complex(2,3)
>>> type(c)
<class 'complex'>
>>> c
(2+3j)
>>> d=0o113
>>> type(d)
<class 'int'>
>>> e=ox34f
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    e=ox34f
NameError: name 'ox34f' is not defined
>>> e=ox34G
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    e=ox34G
NameError: name 'ox34G' is not defined
>>> e=ox7C
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    e=ox7C
NameError: name 'ox7C' is not defined
>>> e=0x34C
>>> type(c)
<class 'complex'>
>>> oct(29)
'0o35'
>>> hex(33)
'0x21'
>>> name = "Sivasai"
>>> type(name)
<class 'str'>
>>> 
>>> 
================================ RESTART: Shell ================================
>>> 