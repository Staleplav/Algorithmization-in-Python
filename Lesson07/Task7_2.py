"""

2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""


import random

def merge_sort(array,level = 0):
    # вырожденный случай
    if len(array) <= 1:
        return array

    # для двух элементов
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array

    # вызываем для первой и второй половины
    left = merge_sort(array[:len(array) // 2], level+1)
    right = merge_sort(array[len(array) // 2:], level+1)
    i, j = 0, 0

    # объединяем левую и правую часть
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            array[i + j] = left[i]
            i += 1
        else:
            array[i + j] = right[j]
            j += 1
    # добрасываем левую часть в итоговый массив в случае если левая больше правой
    while len(left) > i:
        array[i + j] = left[i]
        i += 1
    # добрасываем правую часть в итоговый массив в случае если левая меньше либо равна правой
    while len(right) > j:
        array[i + j] = right[j]
        j += 1

    return array


data = [round(random.uniform(1, 50, ), 2) for i in range(10)]
print(data)
merge_sort(data)
print(data)
