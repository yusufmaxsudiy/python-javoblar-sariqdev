son = int(input("Son kiriting:\n>>>"))
sonlar = list(range(2,11))
for n in sonlar:
    if son%n==0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")