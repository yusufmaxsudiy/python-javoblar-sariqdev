mahsulotlar = ['sabzi','piyoz','kartoshka','uzum','banan','tarvuz','non','anor','olma','nok']

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:\n>>>"))

bor_mahsulotlar = []
mavjud_emas = []

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# print('\n'.join(savat))