# #
# Foydalanuvchidan son qabul qilib,
# sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
# Natijalarni konsolga chiqaring.
def bolinish_alomatlari(son):
    for n in range(2,11):
        if son%n == 0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
bolinish_alomatlari(son = int(input("Sonni kiriting:")))    
    


