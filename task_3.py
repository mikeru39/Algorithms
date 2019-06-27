# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 4
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_ = array[0]
max_ = 0
i = 0
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
imn = array.index(min_)
imx = array.index(max_)

array[imn],array[imx] = array[imx],array[imn]
print(array)