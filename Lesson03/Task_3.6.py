"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз,
используйте один любой по вашему выбору.
"""

#  Берем первое вхождение максимального и минимального элемента

import random
lst =[]

for i in range(10):
    lst.append(random.randrange(0, 100))

index_max = 0
index_min = 0
result = 0
maximum = lst[0]
minimum = lst[0]

for index, i in enumerate(lst):
    if i > maximum:
        maximum = i
        index_max = index
    if i < minimum:
        minimum = i
        index_min = index

print(f'Исходныйный список:\n'
      f'{lst}')
print(f'Максимальное число {maximum}, его индекс {index_max}')
print(f'Минимально число {minimum}, его индекс {index_min}')

# учтём что минимальный элемент может стоять после максимального
if index_min > index_max: index_min, index_max = index_max, index_min
# сумма элементов среза не включая максимального и минимального элемента
for i in lst[index_min + 1:index_max]: result += i

print(f'Сумма чисел между максимальным и минимальным элементом равна: {result}')

