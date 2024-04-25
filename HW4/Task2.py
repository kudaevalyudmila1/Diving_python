"""
Напишите функцию принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента. Если ключ не хешируем, используйте 
его строковое представление.
"""

def dict1(**kwargs):
  dct = {}
  st = set()
  for key, value in kwargs.items():
    try:
      st.add(value)
    except:
      value = str(value)
    dct[value] = key
  return dct

print(dict1(a=2, b=5, c=7))