Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print(10,20,30 sep='xyz')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(10,20,30, sep='xyz')
10xyz20xyz30
print(10,20,30, end='$')
10 20 30$
print(10,20,30,sep='#',end='@')
10#20#30@
>>> print(10,20,30,sep='\n')
10
20
30
>>> a=[1,2,3]
>>> b=a.append(4)
>>> print(b)
None
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
>>> a.pop()
5
>>> print(a)
[1, 2, 3, 4]
>>> print(print(print(10)))
10
None
None
>>> print("he is mad","who are you",sep="\n\n\n")
he is mad


who are you
