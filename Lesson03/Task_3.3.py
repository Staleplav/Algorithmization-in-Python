"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

lst[index_max], lst[index_min] = lst[index_min], lst[index_max]

print(f'Итоговый список с замененными максимальными и минимальными элементами:\n'
      f'{lst}')

