'''
Получая на входе список строковых значений, 
создаем новый список кортежей, 
каждый из которых состоит из булева значения и исходной строки. 
Булево значение указывает, 
встречается ли в исходном строковом значении строка символов 'anonymous'! 
Мы назвали полученный в результате список mark, 
поскольку булевы значения отмечают (mark) строковые элементы в списке,
содержащие строку символов 'anonymous'.
'''
from itertools import tee


txt = ['lambda functions are anonymous functions.',
'anonymous functions dont have a name.',
'functions are objects in Python.']
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt) # добавляет к каждому строковому элементу буль
print(list(mark))
mark = [(True, s) if 'anonymous' in s else (False, s) for s in txt] # второй способ
print(mark)