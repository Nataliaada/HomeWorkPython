# Урок 3. Данные, функции и модули в Python
# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
## *Пример:*
## - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import re


#
# def sum_odd_index(data):
#     s = 0
#     for i in range(len(data)):
#         if i % 2 != 0:
#            s += data[i]
#     print(f"Сумма равна: {s}")
# try:
#
#  data = list(map(int,input('Введите числа через пробел').split()))
#  print(data)
#
#  sum_odd_index(data)
#
# except:
#  print(f'Пожалуйста, введите именно  число ')

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# *Пример:*
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def find_proizv(list):
#     new_list = []
#     for i in range(len(list) // 2):
#         new_list.append(list[i] * list[len(list) - i - 1])
#     if len(list)%2 !=0:
#         a = list[len(list)//2]
#         list[len(list) // 2] = a * a
#         new_list.append(list[len(list)//2])
#     print(new_list)
#
#
# try:
#     data = list(map(int, input('Введите числа через пробел').split()))
#     print(data)
#     find_proizv(data)
#
# except:
#     print(f'Error')

# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# *Пример:*
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find(my_list):
  min = 1
  max = 0
  for i in my_list:
    if (i - int(i)) <= min:
        min = round(i - int(i),2)
    if (i - int(i)) >= max:
        max = round(i - int(i),2)
  print(f'разница между максимальным и минимальным значением дробной части элементов', {max-min})

try:
  li = list(map(float,input('Введите числа через пробел').split()))

  find(li)
except:
  print ('Введено не  число')
# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Нельзя использовать готовые функции.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
#
#
# try:
#
#  x = int(input('Введите число: '))
#  list = []
#  while x > 0:
#          y = x%2
#          list.append(y)
#          x = x//2
#  for i in range(len(list)//2):
#      tmp = list[i]
#      list[i] = list[len(list) - i - 1]
#      list[len(list) - i - 1] = tmp
#  print (*list)
#
# except:
#   print ('Введено не дробное число')

