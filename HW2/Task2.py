"""Напишите программу, которая принимает две строки вида “a/b” -
 дробь с числителем и знаменателем. Программа должна возвращать
сумму и произведение* дробей. Для проверки своего кода
 используйте модуль fractions"""

from fractions import Fraction


fract1 = input("Введите первую дробь (в виде a/b): ")
fract2 = input("Введите вторую дробь (в виде a/b): ")

numer1, denominator1 = fract1.split('/')
numer1 = int(numer1)
denominator1 = int(denominator1)

numer2, denominator2 = fract2.split('/')
numer2 = int(numer2)
denominator2 = int(denominator2)

fract1 = Fraction(numer1, denominator1)
fract2 = Fraction(numer2, denominator2)

sum_fraction = fract1 + fract2
multiplication_fraction = fract1 * fract2

print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", multiplication_fraction)