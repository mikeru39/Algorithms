# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input("Введите  трехзначное число: "))
s1 = a // 100
s2 = a % 10
s3 = a % 100 // 10
b = s1 + s2 + s3
c = s1 * s2 * s3
print("сумма чисел = ", b)
print("Произведение чисел = ", c)
