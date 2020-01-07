"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба минимальны), так и различаться.
"""
import random

lst =[]

for i in range(10):
    lst.append(random.randrange(0, 100))

index_min1 = 0
index_min2 = 0
# инициализируем максимальным значением
minimum1 = 100
minimum2 = 100

for index, i in enumerate(lst):
# если элемент меньше двух минимальных значений, то сдвигаем значения вправо на этот элемент
    if (i < minimum1) & (i < minimum2):
        minimum2 = minimum1
        minimum1 = i
        index_min2 = index_min1
        index_min1 = index
# если элемент больше первого, но меньше второго минимального значения, то перезаписываем второй элемент
    elif i < minimum2:
        minimum2 = i
        index_min2 = index




print(f'Исходныйный список:\n'
      f'{lst}')
print(f'Первое минимальное число {minimum1}, его индекс {index_min1}')
print(f'Второе инимальное число {minimum2}, его индекс {index_min2}')



