mahsulotlar = {}
ishora = True
while ishora:
    mahsulot = input("Mahsulot nomini kiriting:")
    narx = input("Mahsulot narxini kiriting:")
    mahsulotlar[mahsulot] = float(narx)
    takror = input("Davom etasizmi? (ha/yo'q)")
    if takror == "yo'q":
        ishora = False
for m,n in mahsulotlar.items():
    print(f"{m.title()}ning narxi {n} so'm")