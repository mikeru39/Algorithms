import random

SIZE = 10
array = [random.uniform(0, 50) for i in range(SIZE)]
print(array)


def sort(array):
    if len(array) < 2:
        return array
    left = sort(array[:len(array) // 2])
    right = sort(array[len(array) // 2:len(array)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1
    return array


print(sort(array))
