Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> '''slicing is a process of fetching a group of characters or values from a collection'''
'slicing is a process of fetching a group of characters or values from a collection'
>>> a='roses are red'
>>> a[0:5:1]
'roses'
>>> a[2:5:1]
'ses'
>>> a[3:9:1]
'es are'
>>> a[3:11:1]
'es are r'
>>> a[7:10:3]
'r'
>>> a[7:10:2]
'r '
>>> a[8:12:2]
'er'
>>> a[8:12:3]
'ee'
>>> a[0:5:2]
'rss'
>>> a[10:13:2]
'rd'
a[:5:1]
'roses'
a[:5:]
'roses'
a[7::1]
're red'
a[7::1]
're red'
a[5::]
' are red'
a[::1]
'roses are red'
a[::2]
'rssaerd'
a[::-1]
'der era sesor'
b=(([10,20,30,40.'hi','hello'],(11),(12,3),'python','is','good',(1, ),[[1,2,3],4,5],{2,3},'language')
   
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b=(([10,20,30,40,'hi','hello'],(11),(12,3),'python','is','good',(1, ),[[1,2,3],4,5],{2,3},'language')

   b
   
SyntaxError: '(' was never closed
b=(([10,20,30,40,'hi','hello'],(11),(12,3),'python','is','good',(1, ),[[1,2,3],4,5],{2,3},'language'))
   
b
   
([10, 20, 30, 40, 'hi', 'hello'], 11, (12, 3), 'python', 'is', 'good', (1,), [[1, 2, 3], 4, 5], {2, 3}, 'language')
len(b)
   
10
b=(([10,20,30,40,'hi','hello'],(11),(12,3),'python','is','good',(1, )),[[1,2,3],4,5],{2,3},'language')
   
len(b)
   
4
b[3:20:3]
   
('language',)
b[1:10:5]
   
([[1, 2, 3], 4, 5],)
b[0][0][::-1]
   
['hello', 'hi', 40, 30, 20, 10]
b[0][0][-1][2::2]
   
'lo'
b[0][2][::2]
   
(12,)
b[0][2][::-2]
   
(3,)
b[3::3]
   
('language',)

b[-2::-2]
   
({2, 3}, ([10, 20, 30, 40, 'hi', 'hello'], 11, (12, 3), 'python', 'is', 'good', (1,)))
b[-1][::-2]
   
'eaga'
b[-3][::-1]
   
[5, 4, [1, 2, 3]]
b[-3::-3]
   
([[1, 2, 3], 4, 5],)
b[0][0][-2][:]
   
'hi'
b[0][0][::-5]
   
['hello', 10]
b[:-10:-2]
   
('language', [[1, 2, 3], 4, 5])
b[0][-1][::-1]
   
(1,)
