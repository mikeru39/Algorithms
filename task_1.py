from collections import Counter
i = int(input("Кол-во предприятий: "))
r = Counter()
a = 0
sred = 0
while a < i:
    name = input("Имя предприятия: ")
    b = 0
    d = 0
    while b < 4:
        d += int(input(f"Прибыль за {b + 1} квартал: "))
        b += 1
    d = d // 4
    r[name] = d
    sred += d
    a += 1

sred = sred // i

for keys in r.keys():
    a = r[keys]
    if a > sred:
        print(f"Имя предприятия: {keys}. Средняя прибыль за год: {a}. Прибыль выше среднего.")
    else:
        print(f"Имя предприятия: {keys}. Средняя прибыль за год: {a}. Прибыль ниже среднего.")

