# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input("Введите любое число: "))
b = int(input("Введите любое число: "))
c = int(input("Введите любое число: "))
if b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
elif b < c < a or a < c < b:
    print(c)
