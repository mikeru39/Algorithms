# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
array = [i for i in range(2, 100)]
array2 = [0] * 8
a = 0
b = 2
while b < 10:
    for i in array:
        if i % b == 0:
            array2[a] += 1
    a += 1
    b += 1
i = 0
while i < len(array2):
    print(i+2, ' = ', array2[i])
    i += 1
