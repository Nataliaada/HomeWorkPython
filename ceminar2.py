# sp = []
# for i in range(3):
#     sp1=[]
#     for j in range(3):
#         sp1.append(99)
#     sp.append(sp1)
#
# for i in range(len(sp)):
#     print(sp[i])
#
# sp.insert(0,[8,9])
# print("------")
#
# sp.remove([8,9])
# a=sp.pop(-1)
#
# print(a)
# print("одномерный список")
# print(a[::-1])
# a=a + [15,11,99]
# print(a)
# print(a[2:5])

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон
# # возможных координат точек в этой четверти (x и y).
# def show_diapason(num):
#   if num == 1:
#     print('Диапазон Х от 0 до +inf / Y от 0 до +inf')
#   elif num == 2:
#     print('Диапазон Х от 0 до -inf / Y от 0 до +inf')
#   elif num == 3:
#    print('Диапазон Х от 0 до -inf / Y от 0 до -inf')
#   elif num == 4:
#    print('Диапазон Х от 0 до +inf / Y от 0 до -inf')
#   else:
#    print('Введите номер четверти от 1 до 4')
#
# try:
#   n = int(input('Введите номер четверти:'))
#   show_diapason(n)
# except:
#   print('Введено не число')
#
# Второй вариант решения:
# num = int(input("Введите номер четверти: "))
#
# match num:
#   case 1:
#     print(" x > 0; y > 0")
#   case 2:
#     print(" x < 0; y > 0")
#   case 3:
#     print(" x < 0; y < 0")
#   case 4:
#    print(" x > 0; y < 0")
#   case _:
#    print("Что то не так")
#
# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# *Пример:*
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# import math
# try:
#     coordA = []
#     for i in range(2):
#       coordA.append(int(input("введите координату точки А: ")))
#     coordB = []
#     for i in range(2):
#       coordB.append(int(input('введите координату точки В: ')))
#     print(coordA, coordB)
#
#     distan = math.sqrt((coordB[0]- coordA[0])**2 + (coordB[1]- coordA[1])**2)
#     print(round(distan, 3))
# except:
#     print('Введите числа')
# #
# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#
# *Пример:*
#
# - Для N = 5: 1, -3, 9, -27, 81
# def show_sequence(num):
#     for i in range(num):
#        print((-3) ** i, end=' ')
#     print()
#
# try:
#   n = int(input('Input N: '))
#   show_sequence(n)
# except ValueError:
#   print('Input real numbers!')


# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#
# *Пример:*
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#
# n = int(input("Введите число: "))
# book = {}
# for i in range (n):
#    book [i + 1] = 3*(i + 1) + 1
# print(book)
#
# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11
#
#
# try:
#  n = input('Введите число: ')
#  sum = 0
#  for digit in n:
#       if digit.isdigit():
#         sum += int(digit)
#  print("Сумма:", sum)
#
# except:
#  print('Error')
# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# *Пример:*
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# #
# try:
#    n = int(input('Введите число: '))
#    proiz = 1
#
#    for i in range(1,n+1):
#        proiz = proiz * i
#        print(proiz, end = ',')
# except:
#    print('Error')
#SECOND

n = int(input("Введите число N: "))
num = 1
x = []
for i in range(1, n + 1):
    num = num * i
    x.append(num)
print(f"Произведение чисел от 1 до {n} = {x}")

# Задача 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений
# одной строки в другой. COUNT или FIND нельзя юзать! говорил же на семинаре.
# #
# s1 = input('Введите строку в которой будем искать')
# s2 = input("Введите строку которую ищем")
# count = 0
#
# for i in range(len(s1)):
#     if s1[i: i + len(s2)] == s2:
#             count=count+1
# print(count)
