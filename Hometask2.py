
#
# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
#
# *Пример:*
#
# - 6782 -> 23
# - 0,56 -> 11
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
def mult(n)
 proiz = 1
 x = []
 for i in range(1, n + 1):
     proiz = proiz * i
     x.append(proiz)
 print(f"Произведение чисел от 1 до {n} = {x}")

def check_digit(text):
    check = False
    while not check:
      try:
          number = int(input(f"{text}"))
          check = True

      except ValueError as error:
          print(f"Пожалуйста, введите именно ЦЕЛОЕ число - {error}")
    return number



# Задача 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений
# одной строки в другой.
# #
# s1 = input('Введите строку в которой будем искать')
# s2 = input("Введите строку которую ищем")
# count = 0
#
# for i in range(len(s1)):
#     if s1[i: i + len(s2)] == s2:
#             count=count+1
# print(count)
