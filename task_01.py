import random


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


SIZE = 10
array = [random.randint(-100, 100) for i in range(SIZE)]
print(array)
print(bubble_sort(array))
