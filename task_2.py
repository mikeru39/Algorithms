def toDex(number):
    a = 0
    i = 0
    number.reverse()
    while i < len(number):
        a += HEX_NUMBERS[number[i]] * 16 ** i
        i += 1
    return a
def toHex(number):
    b = []
    rezult = ""
    el = '0123456789ABCDEF'
    while number > 0:
        b.append((number % 16))
        number = number // 16
    b.reverse()
    for i in b:
        rezult += el[i]

    return rezult


a = input("Введите первое число: ")
b = input("Введите второе число: ")
first = [i for i in a]
second = [i for i in b]
HEX_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,'6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,'C': 12, 'D': 13, 'E': 14, 'F': 15}
a = toDex(first)
b = toDex(second)

print(f"Сумма = {toHex(a+b)}")
print(f"Проищведение = {toHex(a*b)}")