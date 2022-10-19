#
# 3. Задайте список из n чисел последовательности (1+1/N)**N и выведите на экран их сумму.
#
# *Пример:*
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#
# def list_posl(number):
#    list = []
#    for i in range(1, number + 1):
#      list.append(round((1 + 1 / i) ** i, 3))
#    return list
#
# def sum_values_list(list):
#   sum = 0
#   for i in list:
#     sum += i
#   return sum
#
# try:
#  num = int(input('Введите целое число: '))
#
#  print(f'Последовательность равна: {list_posl(num)}')
#  print(f'Сумма элементов равна {sum_values_list(list_posl(num))}')
#
# except:
#  print('Введите целое число.')
# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# def check_digit(text):
#     check = False
#     while not check:
#       try:
#           number = int(input(f"{text}"))
#           check = True
#
#       except ValueError as error:
#           print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
#     return number
#
# m = check_digit('Введите число:')
# list1 = []
# for i in range(-m,m):
#     list1.append(i)
# print(list1)
#
# path = 'text1.txt'
# data = open(path, 'r')
# prod = 1
# for line in data:
#         prod *= list1[int(line)]
# print(prod)
# data.close()
# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def get_list_from_input(n):
   str_list = [''] * n
   for i in range(n):
      str_list[i] = input(f'Input row {i + 1}: ')

   return str_list

try:
   n = int(input('Input number of rows: '))
except ValueError as ex:
   print('Input natural number!')
   exit(ex)
new_list = get_list_from_input(n)

try:
   num = int(input('Input natural number: '))
except ValueError as ex:
  print('Input natural number!')
  exit(ex)

if str(num) in new_list:
   print(f'Number {num} is found in the list')
else:
   print(f'Number {num} is not found in the list')
# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1
#
