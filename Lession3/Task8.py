"""
Три друга взяли вещи в поход. Сформируйте 
словарь, где ключ — имя друга, а значение — 
кортеж вещей. Ответьте на вопросы:
Какие вещи взяли все три друга
Какие вещи уникальны, есть только у одного друга
Какие вещи есть у всех друзей кроме одного 
и имя того, у кого данная вещь отсутствует
Для решения используйте операции 
с множествами. Код должен расширяться 
на любое большее количество друзей.
"""

dic_things = {
    'Юра':{"палатка","рюкзак","котелок"},
    'Сергей':{"палатка","рюкзак","списки","лопата"},
    'Олег':{"стол","рюкзак","продукты"},
    }
first = list(dic_things.keys())[0]
res = set(dic_things[first])


for k, v in dic_things.items():
    res = res.intersection(set(v))
print(f'у всех есть {res}')

dic_count = {}
for k, v in dic_things.items():
    for value in v:
        dic_count[value] = dic_count.get(value,0 ) +1
print(dic_count)
friends = len(list(dic_things.keys()))-1
things = []

for k, v in dic_count.items():
    if v == friends:
        things.append(k)

for k,v in dic_things.items():
    for  item in things:
        if item not in v:
            print(f'{item} нет у {k}')
            break
one_things = []
for k, v in dic_count.items():
    if v == 1:
        one_things.append(k)
print(f'{one_things} есть у одного')