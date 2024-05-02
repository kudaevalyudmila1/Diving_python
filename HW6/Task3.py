"""
Напишите функцию в шахматный модуль.
 Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
 Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

import random
from Task2 import queens_battle


def shess_list(counts):
    shess_list_new = []
    while len(shess_list) < counts:
        queen_list_temp = []
        for j in range(8):
            new_x = random.randint(1, 8)
            new_y = random.randint(1, 8)
            queen_list_temp.append(list((new_x, new_y)))
        if queens_battle(queen_list_temp) == True:
            shess_list_new.append(queen_list_temp)
    return shess_list_new


print("Уcпешная случайная  расстановка: ")
print(*shess_list(1), sep="\n") 
"""Запрошен 1 вариант расстановки"""

 
 #[[5, 1], [3, 8], [4, 3], [1, 4], [2, 6], [7, 5], [8, 2], [6, 7]]
 