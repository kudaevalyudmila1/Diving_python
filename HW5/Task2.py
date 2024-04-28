"""
Напишите однострочный генератор словаря, который
 принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии 
в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
"""


names = ["Oleg", "Vladimir", "Anton"]
rates = [60_000, 75_000, 85_000]
percents = ['10.25%', '8.0%', '4.5%']
calculate_bonus = {names: rates * float(percents[:-1]) for names, rates, percents in zip(names, rates, percents)}
print(*calculate_bonus.items())












