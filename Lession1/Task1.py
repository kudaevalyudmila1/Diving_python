## Задача 1. Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
## Используйте while и if.
## Попробуйте разные значения e и n.

n = int(input("Введите число n:"))
e = int(input("Введите число e:"))
sum_num = 0
n1 = 2
while n1 <= n:
    if n1 % e != 0:
        sum_num = sum_num + n1
        n1 += 2
    else:
        n1 += 2
print ("Сумма чисел=", sum_num) 