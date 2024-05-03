"""
Доработаем предыдущую задачу. 
Создайте новую функцию которая генерирует файлы с разными расширениями. 
Расширения и количество файлов функция принимает в качестве параметров. 
Количество переданных расширений может быть любым. 
Количество файлов для каждого расширения различно. 
Внутри используйте вызов функции из прошлой задачи.
"""
from Task4 import generate_files 

def generate_with_dictionary(dictionary: dict):
    for key, value in dictionary.items():
        generate_files(key, 'new_files', num_files=value)


if __name__ == '__main__':
    d = {
        'png': 10,
        'jpg': 5,
        'txt': 11,
        'doc': 10,
    }
    generate_with_dictionary(d)