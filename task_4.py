# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с
# клавиатуры.
n = int(input("Введите число: "))
i = 1
quantity = 1
count = 1
while i < n:
    i += 1
    if i % 2 == 0:
        count = count / 2
        quantity -= count

    else:
        count = count / 2
        quantity += count

print(quantity)