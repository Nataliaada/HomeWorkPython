# можно юзать библиотекe re
# задача 1. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""

#
# from random import randint
#
# messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
#             'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']
# def play_game(n, m, players, messages):
#     count = 0
#     if n % 10 == 1 and 9 > n > 10:
#         letter = 'а'
#     elif 1 < n % 10 < 5 and 9 > n > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while n > 0:
#         print(f'{players[count % 2]}, {random.choice(messages)}')
#         move = int(input())
#         if move > n or move > m:
#             print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
#             attempt = 3
#             while attempt > 0:
#                 if n >= move <= m:
#                     break
#                 print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                 move = int(input())
#                 attempt -= 1
#             else:
#                 return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         n = n - move
#         if n > 0:
#             print(f'Осталось {n} конфет{letter}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]
#
#
#
#
# player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
# player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
# players = [player1, player2]
#
# n = int(input('Сколько конфет будем разыгрывать?\n '))
# m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
#
# winer = play_game(n, m, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

#
#
# def find_best_number(num, count):
#
#          return  num % (count+1)
#
#
#
# try:
#   k = int(input('Введите количество конфет: '))
#   maxk = int(input('Введите максимальное количество конфет: '))
#   print(f"{find_best_number(k, maxk)} конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента")
#
#
# except:
#   print('Введите  число.')



# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
import sys
#
# with open('RLE_1.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Напишите текст необходимый для сжатия: '))
# with open('RLE_1.txt', 'r') as file:
#     my_text = file.readline()
#     text_compression = my_text.split()
#
# print(my_text)
#
#
# def rle_encode(text):
#     enconding = ''
#     prev_char = ''
#     count = 1
#     if not text:
#         return ''
#
#     for char in text:
#         if char != prev_char:
#             if prev_char:
#                 enconding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         enconding += str(count) + prev_char
#         return enconding
#
#
# text_compression = rle_encode(my_text)
#
# with open('new_RLE_1.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{text_compression}')
# print(text_compression)
#




# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

# def delet_word(t):
#      word = "абв"
#      lst = [i for i in t.split() if word not in i]
#      print(f'Результат: {" ".join(lst)}')
#
# try:
#   text = input('Введите текст , из которого будем удалять')
#   print(f"Исходный текст: {text}")
#   delet_word(text)
#
#
# except:
#  print(f'Пожалуйста, введите текст ')
#
#
#
#
#

# задача 5 необязательная Дан список чисел. Создайте список, в который попадают числа,
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
#
# *Пример:*
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
#
#     [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]




from random import randint



nums = [randint(1, 9) for i in range(10)]
print('Задан список: ', nums)


def get_create(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups


print('Последовательность: ', get_create(nums))

largest = 0
index = 0

for i in range(len(nums)):
    if len(get_create(nums[i:])) > largest:
        largest = len(get_create(nums[i:]))
        index = i

print('Итого, создан список: ', nums[index:])
print('Итого, последовательность: ', get_create(nums[index:]), '\n')
