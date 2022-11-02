# можно юзать библиотекe re
# задача 1. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""


from random import randint
from random import *
import os


message = ('Приветствую!!\n'
                'Хотите сыграть в игру кому достанется 2021 конфета"?\n'
                'Правила простые:\n'
                'У нас на кону 2021 конфета, кто первый начинает определит случай,\n'
                'за один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
                'Ну что начнем?')
print(message)

message1 = ['твоя очередь', 'да бери уже', 'бери больше', 'не корову проигрываешь',
           'бери быстрее', 'да харош, так долго думать уже']


def player_vs_player():
    candies_total = 2021
    max_take = 28
    count = 0
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = input('\nА твоего соперника?: ')

    print(f'\nНу и так  {player_1} и  {player_2}  начинаем  !\n')
    print('\nДля начала опеределим кто первый начнет игру.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю {lucky} ты ходишь первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message1)} {lucky} = '))
            if step > candies_total or step > max_take or step < 0:
                step = int(input(
                    f'\nНе жадничай можно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 1
        else:
            print('Все кончились конфетки')

        if count == 1:
            step = int(input(f'\n{choice(message1)}, {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nНе жадничай можно взять только {max_take} конфет {loser}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 0
        else:
            print('Баста, карапузик, кончились конфетки')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')


player_vs_player()

# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# #
# import sys
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
# def decoding(text1):
#         number = ''
#         res = ''
#         for i in range(len(text1)):
#             if not text1[i].isalpha():
#                 number += text1[i]
#             else:
#                 res = res + text1[i] * int(number)
#                 number = ''
#         return res
#
#
# text_compression = rle_encode(my_text)
#
# with open('new_RLE_1.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{text_compression}')
# print(text_compression)
#
#
#
#
#
# with open('new_RLE_1.txt', 'r') as file:
#     my_txt = file.readline()
#     decodingtext = my_txt.split()
#
# decodingtext = decoding(my_txt)
#
# with open('new_RLE_2.txt', 'w',) as file:
#     file.write(f'{decodingtext}')
# print(decodingtext)



# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.
#
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

