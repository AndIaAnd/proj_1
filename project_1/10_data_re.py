'''
Функция zip() принимает на входе итерируемые объекты 
iter_1, iter_2, ..., iter_n и агрегирует их в один итерируемый объект 
путем выстраивания соответствующих i-х значений в один кортеж. 
В результате получается итерируемый объект из кортежей
'''
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

zipp = list(zip(lst_1, lst_2))
print(zipp)

#back 

lst_1_1, lst_2_2 = zip(*zipp) # * оператор служит для распаковки всех элементов
print(lst_1_1, lst_2_2)
'''
Теперь представьте, что работаете в IT-подразделении вашей компании. 
У вас есть база данных всех сотрудников 
с названиями столбцов 'name', 'salary' и 'job'. 
Однако ваши данные не маркированы, 
они представляют собой просто набор строк вида 
('Bob', 99000, 'mid-level manager'). 
Необходимо связать эти названия столбцов с элементами данных и привести их 
в удобочитаемый вид: 
{'name': 'Bob', 'salary': 99000, 'job': 'mid-level manager'}. 
Как это сделать?
'''
#data
column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180000, 'data scientist'),
('Bob', 99000, 'mid-level manager'),
('Frank', 87000, 'CEO')]
#logic
db = [dict(zip(column_names, row)) for row in db_rows]
#out
print(db)
'''
Контекст состоит из кортежей для всех строк в переменной db_rows. 
Выражение zip(column_names, row) упаковывает вместе схему и строки. 
Например, первым из созданных списковым включением элементов будет 
zip(['name', 'salary', 'job'], ('Alice', 180000, 'data scientist')), 
объект, который после преобразования в список приобретает вид 
[('name', 'Alice'), ('salary', 180000), ('job', 'data scientist')]. 
Форма элементов — (ключ, значение), 
поэтому можно преобразовать их в ассоциативный массив
с помощью функции преобразования dict(), 
чтобы получить желаемый формат базы данных.
Для функции zip() не важно, что одно из входных значений — список, 
а другое — кортеж. Ей необходимо только, чтобы входные данные представляли 
собой итерируемые объекты (а и списки, и кортежи — итерируемые).
'''