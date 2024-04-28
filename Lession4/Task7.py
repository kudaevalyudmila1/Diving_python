"""
Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные, верните истину,
 а если хотя бы одна убыточная — ложь.
 """

def all_profitable(profits: dict)-> bool:
    """Подсчет убыточности."""
    lst = [sum(value) > 0 for value in profits.values()]
    return all(lst)


if __name__ == '__main__':
    profits = {"hp": [100, -100, 52, 500, -1 ],
                "Ms": [100, -130, -502, -500, -1 ],
                }
    print(all_profitable(profits))