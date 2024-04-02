## Напишите программу, которая запрашивает год и проверяет его на високосность.
## Распишите все возможные проверки в цепочке elif
## Откажитесь от магических чисел
## Обязательно учтите год ввода Григорианского календаря (1582)
## В коде должны быть один input и один print
## Високосный год: делится на 4, но либо делится на 400, либо не делится на 100

IGNORE = 1582
year = int (input("Введите год позже 1582:"))
if year < IGNORE:
    print("Слишком ранний период")
elif year % 4 != 0: 
    print(year, "не високосный год")
elif year % 400 == 0 and year % 100 != 0:
    print (year, " високосный год")
