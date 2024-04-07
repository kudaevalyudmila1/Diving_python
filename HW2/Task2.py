"""Напишите программу, которая принимает две строки вида “a/b” -
 дробь с числителем и знаменателем. Программа должна возвращать
сумму и произведение* дробей. Для проверки своего кода
 используйте модуль fractions"""

from fractions import Fraction


fract1 = input("Введите первую дробь (в виде a/b): ")
fract2 = input("Введите вторую дробь (в виде a/b): ")

num1 = fract1.split(sep= '/')
num2 = fract2.split(sep= '/')

chisl = int(num1[0]) * int(num2[1]) + int(num2[0]) * int(num1[1])
znam = int(num1[1]) * int(num2[1])
sum1 = str(chisl) + '/' + str(znam)
print(f'Сумма дробей равна:  {sum1}')

multiplication = str(int(num1[0])*int(num2[0])) + '/' + str(int(num1[1])*int(num2[1]))
print(f'Произведение дробей равно: {multiplication}')

print('')
x = Fraction(fract1)
y = Fraction(fract2)

print(f'Сумма дробей равна: {x+y}')
print(f'Произведение дробей равно: {x*y}')
