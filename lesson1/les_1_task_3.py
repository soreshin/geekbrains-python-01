# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
#
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f',
# то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

print('Введите границы диапазона целых чисел:')
min = int(input('нижняя граница >>> '))
max = int(input('верхняя граница >>> '))
res = random.randint(min, max)
print(f'Случайное целое число в заданном диапазоне {res}')

print('Введите границы диапазона вещественных чисел:')
min = float(input('нижняя граница >>> '))
max = float(input('верхняя граница >>> '))
res = random.uniform(min, max)
print(f'Случайное вещественное число в заданном диапазоне {res}')

print('Введите границы диапазона символов между "a" и "z"')
min = input('нижняя граница >>> ')
max = input('верхняя граница >>> ')
min_int = ord(min)
max_int = ord(max)
res = random.randint(min_int, max_int)
print(f'Случайный символ между {min} и {max} получился: {chr(res)}')