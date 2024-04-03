"""Программа загадывает число от 0 до 1000. Необходимо 
угадать число за 10 попыток. Программа должна подсказывать 
“больше” или “меньше” после каждой попытки. Для генерации 
случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)"""

from random import randint

LOWER_LIMIT = 1
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(1, 11):
    num1 = int(input("Ведите число от 0 до 1000: "))
    if num1 == num:
        print("Вы отгадали!")
        break
    elif num > num1:
        print(f"Ваше число меньше загаданного, осталось {10 - i} попыток:")    
    elif num < num1:
        print(f"Ваше число больше загаданного, осталось {10- i} попыток:") 
if  num1 != num:
        print("К сожалению, Вы не смогли угадать число. Попробуйте позже, вам повезет")