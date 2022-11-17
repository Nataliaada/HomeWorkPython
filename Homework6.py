# # Задача 1. Создайте программу для игры в "Крестики-нолики".
#
# def create_array():
#     array = []
#     for i in range(3):
#         array_1 = []
#         for j in range(3):
#             array_1.append('-')
#         array.append(array_1)
#     return array
#
# def print_arr(array):
#     for i in range(3):
#         print(" ".join(array[i]))
#
# def check_win(array):
#     win = '-'
#     for i in range(3):
#         result = ''
#         for j in range(3):
#             result += array[i][j]
#         if result == 'xxx':
#             win = 'x'
#         if result == '000':
#             win = '0'
#     for j in range(3):
#         result = ''
#         for i in range(3):
#             result += array[i][j]
#         if result == 'xxx':
#             win = 'x'
#         if result == '000':
#             win = '0'
#
#     for i in range(3):
#         for j in range(3):
#             if array[0][0] == 'x' and array[1][1] == 'x' and array[2][2] == 'x':
#                 win = 'x'
#             if array[0][0] == '0' and array[1][1] == '0' and array[2][2] == '0':
#                 win = '0'
#     for i in range(3):
#         for j in range(3):
#            if array[0][2] == 'x' and array[1][1] == 'x' and array[2][0] == 'x':
#               win = 'x'
#            if array[0][2] == '0' and array[1][1] == '0' and array[2][0] == '0':
#               win = '0'
#     return win
#
# table = create_array()
# count = 0
# hod = 0
# while count < 10:
#     if hod == 0:
#      try:
#             row = int(input('Введите столбец :'))
#             line = int(input('Введите строку: '))
#      except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#     if table[row - 1][line - 1] != '-':
#             print('Эта клетка занята')
#     else:
#          table[row - 1][line - 1] = 'x'
#          hod = 1
#          count += 1
#     if count > 4:
#          if check_win(table) == 'x':
#             print("отработало проверка на Х выигрыш")
#             break
#     if count == 9:
#             print("Ничья!")
#             break
#     print_arr(table)
#     if hod == 1:
#         try:
#             row = int(input('Введите столбец :'))
#             line = int(input('Введите строку: '))
#         except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if table[row - 1][line - 1] != '-':
#             print('Эта клетка занята')
#         else:
#          table[row - 1][line - 1] = '0'
#          hod = 0
#          count += 1
#     if count > 4:
#             if check_win(table) == '0':
#                print("отработало проверка на 0 выигрыш")
#                break
#     if count == 9:
#             print("Ничья!")
#             break
#     print_arr(table)
# if hod == 1:
#     print(f'x ПОБЕДИЛ')
# if hod == 0:
#     print(f'0 ПОБЕДИЛ')

# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
#
# *Пример:*
#
# 2+2 => 4;
#
# 1+2*3 => 7;
#
# 1-2*3 => -5;
#
#

import re

a1 = '66-3*(25-5)/10+3'


def find_num(a):
    res = re.split(r'[\+\-\*\/]', a)
    list_digit = [float(item) for item in res]
    return list_digit


def find_oper(a):
    list_operate = ['+', '-', '/', '*']
    list_oper = []
    for i in a:
        if i in list_operate:
            list_oper.append(i)
    return list_oper


def calculate(list_digit, list_oper):
    for n in range(len(list_digit)):
        for i in range(len(list_oper)):
            if list_oper[i] == '*':
                list_digit[i] *= list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break
        for i in range(len(list_oper)):
            if list_oper[i] == '/':
                list_digit[i] /= list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break
        for i in range(len(list_oper)):
            if list_oper[i] == '-':
                list_digit[i] -= list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break
        for i in range(len(list_oper)):
            if list_oper[i] == '+':
                list_digit[i] += list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break
        return list_digit


def calculate_in_brackets(a):
    for i in a:
        if i == '(':
            part = a[a.find("("):a.find(")") + 1]
            part = part[1:len(part) - 1]
            res = calculate(find_num(part), find_oper(part))
            a = a.replace(a[a.find("("):a.find(")") + 1], str(res[0]))
    return a


def total_result(a):
    no_brackets = calculate_in_brackets(a)
    result = calculate(find_num(no_brackets), find_oper(no_brackets))
    return print(f'{a} =', result)


total_result(a1)


# try:

#     a1 = input('Веедите уравнение')
#     total_result(a1)
# except: print('Error')
