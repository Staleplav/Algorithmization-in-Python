"""
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""

import cProfile

# рекурсивное решение задачи
def recursion (k, itog):
    k -= 1
    if k > 0:
        itog += (-0.5) * recursion(k, itog)
    return itog

# итерационное решение задачи
def iteration (k, itog):
    result = itog
    k -= 1
    while k:
        result = (-0.5) * result
        itog = itog + result
        k -= 1
    return itog

# итерационное решение задачи с использованием списка для хранения вычисленных элементов
def array (k, itog):
    result = [1,]
    i = 1
    while i < k:
        result.append((-0.5) * result[i-1])
        itog = itog + result[i]
        i += 1
    return itog


# на основании измерений оптимальным решением является вариант вычисленния суммы ряда посредством итеративной процедуры
# сложность итерационного алгоритма составляет O(n)

#cProfile.run('recursion (9000,1)')
# 900            900/1    0.001    0.000    0.001    0.001 Task4_1.py:8(recursion)

#cProfile.run('iteration (10000000,1)')
# 900              1    0.000    0.000    0.000    0.000 Task4_1.py:15(iteration)
# 500 000          1    0.077    0.077    0.077    0.077 Task4_1.py:15(iteration)
# 700 000          1    0.105    0.105    0.105    0.105 Task4_1.py:15(iteration)
# 1 000 000        1    0.131    0.131    0.131    0.131 Task4_1.py:15(iteration)
# 10 000 000       1    1.395    1.395    1.395    1.395 Task4_1.py:15(iteration)


#cProfile.run('array (10000000,1)')
# 900              1    0.000    0.000    0.000    0.000 Task4_1.py:25(array)
# 500 000          1    0.231    0.231    0.289    0.289 Task4_1.py:25(array)
# 700 000          1    0.372    0.372    0.461    0.461 Task4_1.py:25(array)
# 1 000 000        1    0.466    0.466    0.584    0.584 Task4_1.py:25(array)
# 10 000 000       1    4.596    4.596    5.778    5.778 Task4_1.py:25(array)


#x = recursion(900,1)
# "Task4.recursion(100,1)"  100 loops, best of 5: 19.9 usec per loop
# "Task4.recursion(500,1)"  100 loops, best of 5: 128 usec per loop
# "Task4.recursion(900,1)"  100 loops, best of 5: 217 usec per loop

#x = iteration(10000000,1)
# "Task4.iteration(100,1)"    100 loops, best of 5: 17.7 usec per loop
# "Task4.iteration(500,1)"    100 loops, best of 5: 49.1 usec per loop
# "Task4.iteration(900,1)"    100 loops, best of 5: 93.5 usec per loop
# "Task4.iteration(500000,1)" 100 loops, best of 5: 73.6 msec per loop

#x = array (10000000,1)
# "Task4.array(100,1)"    100 loops, best of 5: 26.2 usec per loop
# "Task4.array(500,1)"    100 loops, best of 5: 150 usec per loop
# "Task4.array(900,1)"    100 loops, best of 5: 271 usec per loop
# "Task4.array(500000,1)" 100 loops, best of 5: 186 msec per loop

