Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> letter
'a'
>>> letter = fruit[0]
>>> print(letter)
b
>>> letter = fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    letter = fruit[1.5]
TypeError: string indices must be integers
>>> letter = fruit[1+3]
>>> letter
'n'
>>> fruit = 'banana'
>>> len(fruit)
6
>>> length = len(fruit)
>>> length
6
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> last = fruit[length-1]
>>> print(last)
a
>>> fruit[-1]
'a'
>>> fruit[-2]
'n'
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 2, in <module>
    fruit = raspberry
NameError: name 'raspberry' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a
r
Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 11, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

y
r
r
e
b
p
s
a
r
Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 11, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> fruit[index]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fruit[index]
IndexError: string index out of range
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a
r
Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 11, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 10, in <module>
    while index < len(fruit) and index != len(fruit-1):
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a
r
Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 11, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a
r
Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 11, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a
r
Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 11, in <module>
    letter = fruit[index]
IndexError: string index out of range
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 10, in <module>
    while index < len(fruit) and index != -1(len(fruit)):
TypeError: 'int' object is not callable
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a
n
o
h
t
y
p
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net

n
o
h
t
y
p
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y
>>> #String slices
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit[3:3]
''
>>> fruit[:]
'banana'
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
 \Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

>>> greeting = 'Hello, world!'
>>> greeting[0]
'H'
>>> greeting[0]='J'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    greeting[0]='J'
TypeError: 'str' object does not support item assignment
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
>>> print('\n Looping and counting\n')

 Looping and counting

>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count=count+1
print(count)
SyntaxError: invalid syntax
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

>>> count(banana,a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    count(banana,a)
NameError: name 'banana' is not defined
>>> count('banana','a')
Enter string: banana
Enter countable letter: a
0
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

>>> count()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    count()
TypeError: count() missing 2 required positional arguments: 'string' and 'letter'
>>> count('a','a')
Enter string: banana
Enter countable letter: a
3
>>> count('banana','a')
Enter string: 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

>>> count('banana','a')
3
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

>>> count(a,b)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    count(a,b)
NameError: name 'a' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

>>> count(a,g)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    count(a,g)
NameError: name 'a' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

2
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

2

 String comparison 

Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 48, in <module>
    word = banana
NameError: name 'banana' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

2

 String comparison 

All right, bananas.
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

2

 String comparison 

Enter a word/string for comparidon with bananas!!!
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

2

 String comparison 

Enter a word/string for comparidon with bananas!!! : banana
Your word, banana, comes before banana.
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

2

 String comparison 

Enter a word/string for comparidon with bananas!!! :banana
All right, bananas.
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========
>>> 

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

2

 String comparison 

Enter a word/string for comparidon with bananas!!! :Paiiinepl
Your word,Paiiinepl, comes before banana.
>>> stuff = 'Hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.capitalize)
Help on method_descriptor:

capitalize(...)
    S.capitalize() -> str
    
    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

2

 String comparison 

Enter a word/string for comparidon with bananas!!! :been
Your word,been, comes after banana.
/n String methods /n
Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

2

 String comparison 

Enter a word/string for comparidon with bananas!!! :
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 45, in <module>
    count('am I a joke to you? Nintendo vs SEGA!','e')
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 44, in count
    print('We counted ' +counter+ 'letters')
TypeError: must be str, not int
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

 String comparison 

Enter a word/string for comparidon with bananas!!! :bb
Your word,bb, comes after banana.

 String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :b
Your word,b, comes before banana.
\>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :ben
Your word,ben, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA
1
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :bb
Your word,bb, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :
Your word,, comes before banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :b
Your word,b, comes before banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
Here we go
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :gg
Your word,gg, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
Here we go
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   Here we go
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go
>>> word.find('na',1)
2
>>> word.find('na',2)
2
>>> word.find('na',3)
4
>>> word.find('na',4)
4
>>> word.find('na',5)
-1
>>> word = Viens'
SyntaxError: EOL while scanning string literal
>>> word = 'Viens'
>>> word.find('ns',2)
3
>>> word.find('Vi',3)
-1
>>> word.find('Vi',1)
-1
>>> word.find('Vi',0)
0
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :nope
Your word,nope, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :beeen!
Your word,beeen!, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go
/nSome methods such as "startswith" return boolean values
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :b'ladanas
Your word,b'ladanas, comes before banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 78, in <module>
    print(line = 'Have a nice day')
TypeError: 'line' is an invalid keyword argument for this function
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :buu
Your word,buu, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :blubjerry
Your word,blubjerry, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :geez
Your word,geez, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :hh
Your word,hh, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
3
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :huh
Your word,huh, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
>>> howmanyinbanana('a')
Inputt'o a letter'o! For bananaS.S.S. Squad! : a
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    howmanyinbanana('a')
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 96, in howmanyinbanana
    if not re.match('^[a-z*$', lettery):
  File "/usr/lib/python3.6/re.py", line 172, in match
    return _compile(pattern, flags).match(string)
  File "/usr/lib/python3.6/re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.6/sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.6/sre_parse.py", line 855, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.6/sre_parse.py", line 416, in _parse_sub
    not nested and not items))
  File "/usr/lib/python3.6/sre_parse.py", line 523, in _parse
    source.tell() - here)
sre_constants.error: unterminated character set at position 1
>>> howmanyinbanana
<function howmanyinbanana at 0x7f6f1d6732f0>
>>> howmanyinbanana()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    howmanyinbanana()
TypeError: howmanyinbanana() missing 1 required positional argument: 'lettery'
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
>>> howmanyinbanana()
Inputt'o a letter'o! For bananaS.S.S. Squad! : 'a'
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    howmanyinbanana()
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 96, in howmanyinbanana
    if not re.match('^[a-z*$', lettery):
  File "/usr/lib/python3.6/re.py", line 172, in match
    return _compile(pattern, flags).match(string)
  File "/usr/lib/python3.6/re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.6/sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.6/sre_parse.py", line 855, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.6/sre_parse.py", line 416, in _parse_sub
    not nested and not items))
  File "/usr/lib/python3.6/sre_parse.py", line 523, in _parse
    source.tell() - here)
sre_constants.error: unterminated character set at position 1
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
>>> howmanyinbanana()
Inputt'o a letter'o! For bananaS.S.S. Squad! : a
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    howmanyinbanana()
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 97, in howmanyinbanana
    if not re.match('^[a-z*$', lettery):
  File "/usr/lib/python3.6/re.py", line 172, in match
    return _compile(pattern, flags).match(string)
  File "/usr/lib/python3.6/re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.6/sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.6/sre_parse.py", line 855, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.6/sre_parse.py", line 416, in _parse_sub
    not nested and not items))
  File "/usr/lib/python3.6/sre_parse.py", line 523, in _parse
    source.tell() - here)
sre_constants.error: unterminated character set at position 1
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
>>> homanyinbanana()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    homanyinbanana()
NameError: name 'homanyinbanana' is not defined
>>> howmanyinbanana()
Inputt'o a letter'o! For bananaS.S.S. Squad! : a
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    howmanyinbanana()
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 97, in howmanyinbanana
    if not re.match('^[a-z*$', lettery):
  File "/usr/lib/python3.6/re.py", line 172, in match
    return _compile(pattern, flags).match(string)
  File "/usr/lib/python3.6/re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.6/sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.6/sre_parse.py", line 855, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.6/sre_parse.py", line 416, in _parse_sub
    not nested and not items))
  File "/usr/lib/python3.6/sre_parse.py", line 523, in _parse
    source.tell() - here)
sre_constants.error: unterminated character set at position 1
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
>>> howmanyinbanana()
Inputt'o a letter'o! For bananaS.S.S. Squad! : a
3
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :ban
Your word,ban, comes before banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
>>> howmanyinbanana()
Inputt'o a letter'o! For bananaS.S.S. Squad! : a
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    howmanyinbanana()
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 99, in howmanyinbanana
    if not re.match("^[a-z*$", lettery):
  File "/usr/lib/python3.6/re.py", line 172, in match
    return _compile(pattern, flags).match(string)
  File "/usr/lib/python3.6/re.py", line 301, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/usr/lib/python3.6/sre_compile.py", line 562, in compile
    p = sre_parse.parse(p, flags)
  File "/usr/lib/python3.6/sre_parse.py", line 855, in parse
    p = _parse_sub(source, pattern, flags & SRE_FLAG_VERBOSE, 0)
  File "/usr/lib/python3.6/sre_parse.py", line 416, in _parse_sub
    not nested and not items))
  File "/usr/lib/python3.6/sre_parse.py", line 523, in _parse
    source.tell() - here)
sre_constants.error: unterminated character set at position 1
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :baa
Your word,baa, comes before banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
>>> howmanyinbanana()
Inputt'o a letter'o! For bananaS.S.S. Squad! : a
3
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :f
Your word,f, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
Inputt'o a letter'o! For bananaS.S.S. Squad! : oboze
ERROR!!!! Can U type just one letter?! Geez..
Traceback (most recent call last):
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 105, in <module>
    howmanyinbanana()
  File "/home/ren/RTR108_2020/4WEEK/7th_Exercises.py", line 103, in howmanyinbanana
    sys.exit()
NameError: name 'sys' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :v
Your word,v, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"

Inputt'o a letter'o! For bananaS.S.S. Squad! : ozooo
ERROR!!!! Can U type just one letter?! Geez..
>>> howmanyinbanana()

Inputt'o a letter'o! For bananaS.S.S. Squad! : u
0
>>> howmanyinbanana()

Inputt'o a letter'o! For bananaS.S.S. Squad! : W
Error'Ah! Only letterz a to z allAwd!
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :f
Your word,f, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"
Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :f
Your word,f, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : WAI
Error'Ah! Only letterz a to z allAwd!
>>> howmanybanana()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    howmanybanana()
NameError: name 'howmanybanana' is not defined
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : WAI?
Error'Ah! Only letterz a to z allAwd!
>>> howmanyinbanana()


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : ok
ERROR!!!! Can U type just one letter?! Geez..
>>> howmanyinbanana()


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : a
3
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :c
Your word,c, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : f
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : g
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : g
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

42
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :j
Your word,j, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : j
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : g
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
In 3 years I have spotted 0.1 camels
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :h.
Your word,h., comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : h
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
In 3 years I have spotted 0.1 camels

 Exercise 5 

>>> print(itog)
ce: 0.8475
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : g
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
In 3 years I have spotted 0.1 camels

 Exercise 5 

We extracted this:  0.8475
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :f
Your word,f, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : f
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
In 3 years I have spotted 0.1 camels

 Exercise 5 

We extracted this:  .8475
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :f
Your word,f, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : f
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
In 3 years I have spotted 0.1 camels

 Exercise 5 

We extracted this: 0.8475
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : g
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
In 3 years I have spotted 0.1 camels

 Exercise 5 

We extracted this: 0.8475
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :f
Your word,f, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : f
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
In 3 years I have spotted 0.1 camels

 Exercise 5 

We extracted this: 0.8475
We got a floating number point: 0.8475
>>> type(konvert)
<class 'float'>
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :f
Your word,f, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : f
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
In 3 years I have spotted 0.1 camels

 Exercise 5 

We extracted this: 0.8475
We got a floating number point: 0.8475
<class 'float'>
>>> 
=========== RESTART: /home/ren/RTR108_2020/4WEEK/7th_Exercises.py ===========

 Traversal through a string with a loop

r
a
s
p
b
e
r
r
y

 Exercise 1 
 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a seperate line, except backwards

r
y
r
r
e
b
p
s
a

Function found on the net:

n
o
h
t
y
p

 Another way to write a traversal is with a "for" loop:

r
a
s
p
b
e
r
r
y

 Exercise 2
Given that "fruit" is a string, what does "fruit[:]" mean? It means that the whole string will be assigned.

raspberry

Looping and counting

3

 Exercise 3 
 Encapsulate this code in a fucntion named "count", and generalize it so that it accepts the string and the letter as arguments 

We counted 2 letters

>String comparison 

Enter a word/string for comparidon with bananas!!! :g
Your word,g, comes after banana.

>String methods 

Help on method_descriptor:

upper(...)
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

BANANA

 For example, there is a string method named _find_ that searches for the position of one string within another: 
1

The find method can find substrings as well as characters:

2
4

 One common tas is to remove white spaces (spaces, tabs, or newlines) from the beginning and end of a string using the strip method: 
   Here we go   
 Here we go

Some methods such as "startswith" return boolean values

Have a nice day
Line starts with Have? True
Line starts with h? False
If using "lower" methond on line:  have a nice day
Line starts with h if it's mapped as lowercase? True

 Exercise 4 
 There is a string method called "count" that is similar to the function in the previous exercise. Read the documentation of this method and write an invocation that counts the number of times the letter "a" occurs in "banana"


Welcome to a program which counts how many user specified letters are in a word "banana"!
It's absolutely useful so I hope you'l have fun with it!

Inputt'o a letter'o! For bananaS.S.S. Squad! : g
0

Parsing strings

From stephen.marquard@utc.at.za Sat Jan 5 09"14"16 2008 Symbol @ is at:  21
Where's the next space after @ symbol? : 31
utc.at.za

Format operators

I have spotted 42 camels
In 3 years I have spotted 0.1 camels

 Exercise 5 

We extracted this: 0.8475
<class 'str'>
We got a floating number point: 0.8475
<class 'float'>
>>> 
