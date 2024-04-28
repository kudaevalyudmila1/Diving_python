"""
Напишите функцию, которая принимает на вход строку - 
абсолютный путь до файла. Функция возвращает кортеж из
трёх элементов: путь, имя файла, расширение файла.
"""


def file_info(fl):

    file_extension = fl.split('.')
    name = str(file_extension[:-1])
    name_result = name.split('/')
    return fl,name_result[-1],file_extension[-1]


file = 'C:/Users/Roman/Desktop/vesna.jpg'
print(file_info(file))