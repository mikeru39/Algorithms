#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_ = array[0]
max_ = 0
i = 0
sum_ = 0

while i < SIZE:
    if min_ > array[i]:
        min_ = array[i]
    i += 1
i = 0
while i < SIZE:
    if max_ < array[i]:
        max_ = array[i]
    i += 1
print(min_)
print(max_)
id_min = array.index(min_)
id_max = array.index(max_)
if id_max > id_min:
    i = id_min + 1
    while i < id_max:
        sum_ += array[i]
        i += 1
else:
    i = id_max + 1
    while i < id_min:
        sum_ += array[i]
        i += 1

print("сумма = " + str(sum_))
