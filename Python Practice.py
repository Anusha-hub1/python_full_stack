Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
Fruits = ('Apple', 'Orange', 'Grapes')
Fruits
('Apple', 'Orange', 'Grapes')
Fruits.insert(1: 'Kiwi')
SyntaxError: invalid syntax
Fruits.insert(1, 'Kiwi')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Fruits.insert(1, 'Kiwi')
AttributeError: 'tuple' object has no attribute 'insert'
Fruits = ['Apple', 'Orange', 'Grapes']
Fruits
['Apple', 'Orange', 'Grapes']
Fruits.insert(1, 'Kiwi')
Fruits
['Apple', 'Kiwi', 'Orange', 'Grapes']
Fruits = ['Apple', 'Orange', 'Grapes']Fruits
SyntaxError: invalid syntax
Fruits
['Apple', 'Kiwi', 'Orange', 'Grapes']
Fruits(1:3) = 'Mango'
SyntaxError: invalid syntax
Fruits(1:3) = ['Mango']
SyntaxError: invalid syntax
Fruits[1:3] = ['Mango']
Fruits
['Apple', 'Mango', 'Grapes']
Fruits[1:2] = ['Mango', 'Berry']
Fruits
['Apple', 'Mango', 'Berry', 'Grapes']
['Apple', 'Mango', 'Berry', 'Grapes']
['Apple', 'Mango', 'Berry', 'Grapes']
Fruits.extend['Banana', 'Cherry']
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Fruits.extend['Banana', 'Cherry']
TypeError: 'builtin_function_or_method' object is not subscriptable
Fruits.extend(['Banana', 'Cherry'])
Fruits
['Apple', 'Mango', 'Berry', 'Grapes', 'Banana', 'Cherry']
Fruits.remove('Mango')
Fruits
['Apple', 'Berry', 'Grapes', 'Banana', 'Cherry']
Fruits.pop(4)
'Cherry'
Fruits
['Apple', 'Berry', 'Grapes', 'Banana']
del Fruits('Apple')
SyntaxError: cannot delete function call
del Fruits(0)
SyntaxError: cannot delete function call
del Fruits[0]
Fruits
['Berry', 'Grapes', 'Banana']
Fruits.clear()
Fruits
[]




Fruits = ['Apple', 'Mango', 'Berry', 'Grapes', 'Banana', 'Cherry']
Fruits
['Apple', 'Mango', 'Berry', 'Grapes', 'Banana', 'Cherry']
Fruits.sort()
Fruits
['Apple', 'Banana', 'Berry', 'Cherry', 'Grapes', 'Mango']
['Apple', 'Banana', 'Berry', 'Cherry', 'Grapes', 'Mango']
['Apple', 'Banana', 'Berry', 'Cherry', 'Grapes', 'Mango']


Fruits[1:2] = ['apple', 'banana']
Fruits
['Apple', 'apple', 'banana', 'Berry', 'Cherry', 'Grapes', 'Mango']
Fruits.sort()
Fruits
['Apple', 'Berry', 'Cherry', 'Grapes', 'Mango', 'apple', 'banana']
Fruits[5:7] = ['Apple','Banana']
Fruits
['Apple', 'Berry', 'Cherry', 'Grapes', 'Mango', 'Apple', 'Banana']
['Apple', 'Berry', 'Cherry', 'Grapes', 'Mango', 'Apple', 'Banana']
['Apple', 'Berry', 'Cherry', 'Grapes', 'Mango', 'Apple', 'Banana']

Fruits.sort()
Fruits
['Apple', 'Apple', 'Banana', 'Berry', 'Cherry', 'Grapes', 'Mango']
Fruits.sort(reverse = True)
Fruits
['Mango', 'Grapes', 'Cherry', 'Berry', 'Banana', 'Apple', 'Apple']
['Mango', 'Grapes', 'Cherry', 'Berry', 'Banana', 'Apple', 'Apple']
['Mango', 'Grapes', 'Cherry', 'Berry', 'Banana', 'Apple', 'Apple']



names = ('Anusha', 'Ammu', 'Riyu', 'Sathish')
names
('Anusha', 'Ammu', 'Riyu', 'Sathish')
('Anusha', 'Ammu', 'Riyu', 'Sathish')
('Anusha', 'Ammu', 'Riyu', 'Sathish')

names[1] = ('Anu')
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    names[1] = ('Anu')
TypeError: 'tuple' object does not support item assignment
nameList[1] = ('Anu')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    nameList[1] = ('Anu')
NameError: name 'nameList' is not defined
nameList = list(names)
names
('Anusha', 'Ammu', 'Riyu', 'Sathish')
('Anusha', 'Ammu', 'Riyu', 'Sathish')
('Anusha', 'Ammu', 'Riyu', 'Sathish')
namesList
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    namesList
NameError: name 'namesList' is not defined. Did you mean: 'nameList'?
nameList = list(names)
nameList
['Anusha', 'Ammu', 'Riyu', 'Sathish']
nameList[1] = ['Anu']
nameList
['Anusha', ['Anu'], 'Riyu', 'Sathish']
['Anusha', ['Anu'], 'Riyu', 'Sathish']
['Anusha', ['Anu'], 'Riyu', 'Sathish']
nameList.remove[1]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    nameList.remove[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
nameList.remove['Anu']
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    nameList.remove['Anu']
TypeError: 'builtin_function_or_method' object is not subscriptable
nameList[1] = 'Anu'
nameList
['Anusha', 'Anu', 'Riyu', 'Sathish']
nameList[1] = 'Ammu'
nameList
['Anusha', 'Ammu', 'Riyu', 'Sathish']
>>> nameList[0] = 'Anu'
>>> namrList
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    namrList
NameError: name 'namrList' is not defined. Did you mean: 'nameList'?
>>> nameList
['Anu', 'Ammu', 'Riyu', 'Sathish']
>>> names = nameList
>>> nameList tuple(names)
SyntaxError: invalid syntax
>>> nameList = tuple(names)
>>> names
['Anu', 'Ammu', 'Riyu', 'Sathish']
>>> ['Anu', 'Ammu', 'Riyu', 'Sathish']
['Anu', 'Ammu', 'Riyu', 'Sathish']
>>> 
>>> person = {'firstname' = 'Anusha', 'lastname' = 'Chinthanuri', 'mobile'= 0000000000}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> person = {'firstname' : 'Anusha', 'lastname' : 'Chinthanuri', 'mobile': 0000000000}
>>> person
{'firstname': 'Anusha', 'lastname': 'Chinthanuri', 'mobile': 0}
>>> person('firstname')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    person('firstname')
TypeError: 'dict' object is not callable
>>> person['firstname']
'Anusha'
>>> person['mobile'] = '0000000000'
>>> person
{'firstname': 'Anusha', 'lastname': 'Chinthanuri', 'mobile': '0000000000'}
>>> person.update({'mobile' = '9999999999'})
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> person.update({'mobile' : '9999999999'})
>>> person
{'firstname': 'Anusha', 'lastname': 'Chinthanuri', 'mobile': '9999999999'}
>>> person['age'] = 29
>>> person
{'firstname': 'Anusha', 'lastname': 'Chinthanuri', 'mobile': '9999999999', 'age': 29}
