# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def kattasini_chiqar(son1, son2):
    if son1>son2:
        print(son1)
    elif son1<son2:
        print(son2)
    else:
        print("Sonlar teng")
kattasini_chiqar(son1 = int(input("1-sonni kiriting:")), son2 = int(input("2-sonni kiriting:")))




