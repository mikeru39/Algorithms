# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random


# Вариант 1
def main(SIZE):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

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

    imn = array.index(min_)
    imx = array.index(max_)

    array[imn], array[imx] = array[imx], array[imn]


# "task_3.main(10)"
# 100 loops, best of 5: 27.4 usec per loop

# "task_3.main(20)"
# 100 loops, best of 5: 53.5 usec per loop

#  "task_3.main(40)"
# 100 loops, best of 5: 104 usec per loop


# Вариант 2


def main(SIZE):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

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

    imn = array.index(min_)
    imx = array.index(max_)

    array[imn], array[imx] = array[imx], array[imn]


# "task_3.main(10)"
# 100 loops, best of 5: 27.4 usec per loop

# "task_3.main(20)"
# 100 loops, best of 5: 53.5 usec per loop

#  "task_3.main(40)"
# 100 loops, best of 5: 104 usec per loop




# Вариант 3

def main(SIZE):
    MIN_ITEM = -100
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    # print(array)

    min_ = min(array)
    max_ = max(array)
    imx = array.index(max_)
    imn = array.index(min_)
    array[imn], array[imx] = array[imx], array[imn]
# "task_3.main(10)"
# 100 loops, best of 5: 25 usec per loop
# "task_3.main(20)"
# 100 loops, best of 5: 46.8 usec per loop
# "task_3.main(40)"
# 100 loops, best of 5: 91.3 usec per loop
