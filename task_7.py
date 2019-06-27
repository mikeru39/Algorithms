# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = 4
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_ = array[0]
min_2 = array[1]
i = 0

while i < SIZE:
    if min_ > array[i]:
        min_ = array[i]
    i += 1
print("Первое минимальное число: " + min_)
array.remove(min_)

i = 0
while i < SIZE - 1:
    if min_ == array[i]:
        i += 1
        continue
    if min_2 > array[i]:
        min_2 = array[i]
    i += 1
print("Второе минимальное число: " + min_2)
