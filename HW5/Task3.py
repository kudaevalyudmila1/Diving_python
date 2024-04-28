"""
Создайте функцию генератор чисел Фибоначчи
"""

def fibonachi_number(n):
    a = 0
    b = 1
    yield a
    yield b
    for _ in range(n - 2):
        yield a + b
        a, b = b, a + b


num = int(input('Введите число  для расчетапоследовательности Фибоначчи:'))
result = [i for i in fibonachi_number(num)]
print(result)
   
   
   
   




