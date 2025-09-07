mahsulotlar = ['sabzi','piyoz','kartoshka','uzum','banan','tarvuz','non','anor','olma','nok']
savat = []
for n in range(5):
    mahsulot = input(f"Savatga {n+1}-mahsulotni qo'shing:\n>>>") 
    savat.append(mahsulot)
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")