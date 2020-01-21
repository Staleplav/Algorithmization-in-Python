"""
Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти.

"""

"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""

import cProfile
import sys

SHOW_VARS = True
DETAIL = True

# рекурсивное решение задачи
def recursion (k, itog):
    k -= 1
    if k > 0:
        itog += (-0.5) * recursion(k, itog)

    print(var_size(itog))
    return itog

# итерационное решение задачи
def iteration (k, itog):
    result = itog
    k -= 1
    while k:
        result = (-0.5) * result
        itog = itog + result
        k -= 1
    print(var_size(result))
    print(var_size(itog))
    return itog

# итерационное решение задачи с использованием списка для хранения вычисленных элементов
def array (k, itog):
    result = [1,]
    i = 1
    while i < k:
        result.append((-0.5) * result[i-1])
        itog = itog + result[i]
        i += 1
    print(var_size(result))
    print(var_size(itog))
    return itog


def var_size(x, level=0):
    res = 0
    if DETAIL:
        print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                res += var_size(key, level + 1)
                res += var_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
               res += var_size(item, level + 1)
    else: res = sys.getsizeof(x)
    return res

print(sys.version, sys.platform)


print('*******Iteration********', iteration(10,1))
print('*******Recursion********', recursion(10,1))
print('*******WithArray********', array(10,1))

# на основе проведённых измерений наиболее оптимальным вариантом по потреблению памяти является итеративный вариант
# его потребление памяти равно 32 байтам. Рекурсивный вариант потребляет 158 байт. Вариант с массивом - 174 байт.

#3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] win32
# type=<class 'float'>, size=16, object=-0.001953125
# type=<class 'float'>, size=16, object=0.666015625
# 32
#********iteration******* 0.666015625

# type=<class 'int'>, size=14, object=1
# type=<class 'float'>, size=16, object=0.5
# type=<class 'float'>, size=16, object=0.75
# type=<class 'float'>, size=16, object=0.625
# type=<class 'float'>, size=16, object=0.6875
# type=<class 'float'>, size=16, object=0.65625
# type=<class 'float'>, size=16, object=0.671875
# type=<class 'float'>, size=16, object=0.6640625
# type=<class 'float'>, size=16, object=0.66796875
# type=<class 'float'>, size=16, object=0.666015625
# 158
#*******Recursion******** 0.666015625

# type=<class 'list'>, size=96, object=[1, -0.5, 0.25, -0.125, 0.0625, -0.03125, 0.015625, -0.0078125, 0.00390625, -0.001953125]
#	 type=<class 'int'>, size=14, object=1
#	 type=<class 'float'>, size=16, object=-0.5
#	 type=<class 'float'>, size=16, object=0.25
#	 type=<class 'float'>, size=16, object=-0.125
#	 type=<class 'float'>, size=16, object=0.0625
#	 type=<class 'float'>, size=16, object=-0.03125
#	 type=<class 'float'>, size=16, object=0.015625
#	 type=<class 'float'>, size=16, object=-0.0078125
#	 type=<class 'float'>, size=16, object=0.00390625
#	 type=<class 'float'>, size=16, object=-0.001953125
# type=<class 'float'>, size=16, object=0.666015625
# 174
# *******WithArray******** 0.666015625