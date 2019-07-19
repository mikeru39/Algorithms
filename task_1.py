import random
import sys


# python = 3.7, 64 bit
# os windows 10, 64 bit


def memory_size(*args):
    size = 0
    for i in args:
        size += sys.getsizeof(i)
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                for key, value in i.items():
                    size += sys.getsizeof(key) + sys.getsizeof(value)
            elif not isinstance(i, str):
                for item in i:
                    size += sys.getsizeof(item)
    print(size)


# Вариант 1
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
print("Первое минимальное число: " + str(min_))
array.remove(min_)

i = 0
while i < SIZE - 1:
    if min_ == array[i]:
        i += 1
        continue
    if min_2 > array[i]:
        min_2 = array[i]
    i += 1
print("Второе минимальное число: " + str(min_2))
memory_size(min_, min_2, i, array, SIZE, MAX_ITEM, MIN_ITEM)
# Сумма = 176


# Вариант 2
SIZE = 4
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = min(array)
print("Первое минимальное число: " + str(min_))
array.remove(min_)

min_ = min(array)
print("Второе минимальное число: " + str(min_))

memory_size(min_, array, SIZE, MAX_ITEM, MIN_ITEM)
# Сумма = 148


# Вариант 3
SIZE = 4
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_1, min_2 = (0, 1) if array[0] < array[1] else (1, 0)
for i in range(2, len(array)):
    if array[i] < array[min_1]:
        spam = min_1
        min_1 = 1
        if array[spam] < array[min_2]:
            min_2 = spam
    elif array[i] < array[min_2]:
        min_2 = i
print(array[min_1])
print(array[min_2])

memory_size(min_2, min_1, array, i, SIZE, MAX_ITEM, MIN_ITEM)
# Сумма = 190
# Второй вариант лучше потому, что в нем использовано меньше всего переменных
