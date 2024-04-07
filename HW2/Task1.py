"""Напишите программу, которая получает целое число и 
возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата."""

BASE = 16

num = int(input("введите число для перевода в шеснадцатиричное представление: "))
print(hex(num))
number_str = '0123456789ABCDEF'
num_str =''
if num < BASE:
    print(f'Искомое число: {number_str[num]}')
else:
    while num > BASE:
        num_str += number_str[num % BASE] 
        num = num // BASE
    num_str += number_str[num]   
    print(f'Искомое число: {num_str[::-1]}') 
