def create_array():
    array = []
    for i in range(3):
        array_1 = []
        for j in range(3):
            array_1.append('-')
        array.append(array_1)
    return array


def print_arr(array):
    for i in range(3):
        print(" ".join(array[i]))


def check_win(array):
    win = '-'
    for i in range(3):
        result = ''
        for j in range(3):
            result += array[i][j]
        if result == 'xxx':
            win = 'x'
        if result == '000':
            win = '0'
    for j in range(3):
        result = ''
        for i in range(3):
            result += array[i][j]
        if result == 'xxx':
            win = 'x'
        if result == '000':
            win = '0'

    for i in range(3):
        result = ''
        for j in range(3):
            if i == j:
             result += array[i][j]
        return result
    if result == 'xxx':
              win = 'x'
    if result == '000':
              win = '0'

    for i in range(3):
        for j in range(3):
            result += array[0][2] + array[1][1] + array[2][0]
    if result == 'xxx':
        win = 'x'
    elif result == '000':
        win = '0'

    return win


table = create_array()
count = 0
hod = 0
while count < 10:
    print_arr(table)
    if hod == 0:
        try:
            row = int(input('Введите столбец :'))
            line = int(input('Введите строку: '))

        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue

        table[row - 1][line - 1] = 'x'
        hod = 1
        count += 1
        if count > 4:
            if check_win(table) == 'x':
                break
        if count == 9:
            print("Ничья!")
            break
    print_arr(table)
    if hod == 1:
        try:
            row = int(input('Введите столбец :'))
            line = int(input('Введите строку: '))
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue

        table[row - 1][line - 1] = '0'
        hod = 0
        count += 1
        if count > 4:
            if check_win(table) == '0':
                break
        if count == 9:
            print("Ничья!")
            break
if hod == 1:
    print(f'x ПОБЕДИЛ')
if hod == 0:
    print(f'0 ПОБЕДИЛ')

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
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#
# *Пример:*
#
# 1+2*3 => 7;
#
# (1+2)*3 => 9;


