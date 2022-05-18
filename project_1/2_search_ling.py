'''Поисковые системы ранжируют текстовую информацию по степени соответствия запросу пользователя. 
Для этого поисковые системы анализируют
содержимое текста, в котором необходимо произвести поиск. Любой текст состоит из слов. 
В одних содержится немало информации о содержимом текста, а в других — нет. 
Примеры первых слов — white, whale, Captain, Ahab1 (узнали, откуда это?). 
Примеры слов второго типа — is, to, as, the, a и how, поскольку они содержатся в большинстве текстов. 
При реализации поисковых систем часто отфильтровывают слова, не несущие особого значения.
Простейший эвристический подход — отфильтровывать все слова из трех или менее букв. 
'''
text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have'''
w = [[x for x in line.split() if len(x) > 3 ] for line in text.split('/n')] # ищет ключевые 
#слова размером больше 3 символов
print(w)

