"""
4. Определить, какое число в массиве встречается чаще всего.

В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз,
используйте один любой по вашему выбору.
"""
import random
lst =[]

for i in range(20):
    lst.append(random.randrange(0, 10))

maximum_count = 0
num = 0
tmp_count = 1
tmp = 0

# Берем первый встречающийся максимальное кол-во раз элемент
for i in lst:
    tmp_count = 0
    tmp = i
    for j in lst:
        if i == j:
            tmp_count += 1
    if tmp_count > maximum_count:
        maximum_count = tmp_count
        num = tmp

print(f'В списке {lst}\n'
      f'самое частое число {num}. Оно встречается {maximum_count} раз.')
