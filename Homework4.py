# Урок 4. Данные, функции и модули в Python. Продолжение
# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#
# def find_List(num):
#     i = 2  # первое простое число
#     lst = []
#     K = num
#     while i <= num:
#         if num % i == 0:
#             lst.append(i)
#             num //= i
#             i = 2
#         else:
#             i += 1
#     print(f"Простые множители числа {K} : {lst}")
#
#
# try:
#   n = int(input('Введите целое число: '))
#   find_List(n)
#
# except:
#   print('Введите  число!')
#


# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#
# def list_of_only_num(list):
#     new_list = []
#     [new_list.append(i) for i in list if i not in new_list]
#
#
#     print(f"Список из неповторяющихся элементов: {new_list}")
#
# try:
#
#  data = list(map(int, input('Введите числа через пробел').split()))
#  print(data)
#
#  list_of_only_num(data)
#
# except:
#  print(f'Пожалуйста, введите именно  число ')
#
#
#

# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# *Пример:*
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def write_file(st):
    with open('file1.txt', 'w') as data:
        data.write(st)
    data.close()

def rnd():
    return random.randint(0, 101)


def create_mn(k):
    lst = [rnd() for i in range(k + 1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}*x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}*x'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))





# задача 4 необязательная. НА ВХОДЕ ИМЕННО СТРОКА! Найдите корни квадратного уравнения, уравнение вводит через строку пользователь.
# например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения. Предусмотреть все варианты, сделать обработку исключений.



#
# задача 5 необязательная Сделать локальный чат-бот с JSON хранилищем на основе приложенного буткемпа.
# Тема чат-бота любая. Просьба - постараться не использовать простой одномерный список или простой одномерный словарь