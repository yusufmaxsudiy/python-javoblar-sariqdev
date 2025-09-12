ebozor = {'qop':6700,
          'ilgich':12400,
          'latta':4500,
          'tova':46900,
          'naushnik':43200,
          'gilof':9700,
          'kofe':73700}
tovarlar = []
while True:
    savol = "Mahsulotni kiriting(chiqish uchun stop yozing):"
    tovar = input(savol)
    tovarlar.append(tovar)
    if tovar == 'stop':
        break
    if tovar in ebozor:
        print(f"{tovar.title()}ning narxi {ebozor[tovar]}")
    else:
        print("Bizda bu mahsulot yo'q")