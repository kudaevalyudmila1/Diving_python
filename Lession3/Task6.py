"""
Пользователь вводит строку текста. 
Подсчитайте сколько раз встречается 
каждая буква в строке без использования 
метода count и с ним. 
Результат сохраните в словаре, где ключ — символ, а значение — частота встречи 
символа в строке. 
Обратите внимание на порядок ключей. Объясните почему они совпадают 
или не совпадают в ваших решениях.
"""
text_lst = input('Введите строку: ').split()
text_lst.sort()

max_len = max([len(word) for word in text_lst])
max_len1 = len(max(text_lst, key=len))

for i, word in enumerate(text_lst, 1):
    print(f'{i} {word:>{max_len}}')