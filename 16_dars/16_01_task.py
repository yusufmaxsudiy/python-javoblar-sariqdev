adib0 = {
    'ism':'Alisher Navoiy',
    'tyil':1441,
    'vafot':1501,
    'tshahar':'hirot',
    }
adib1 = {
    'ism':'erkin vohidov',
    'tyil':1936,
    'vafot':2016,
    'tshahar':'oltiariq',
    }
adib2 = {
    'ism':'zahiriddin muhammad bobur',
    'tyil':1483,
    'vafot':1530,
    'tshahar':'andijon',
}
adiblar = [adib0, adib1, adib2]
for adib in adiblar:
    print(f"{adib['ism'].title()} {adib['tyil']}-yilda {adib['tshahar'].title()}da tavallud topgan. "
          f"{adib['vafot']-adib['tyil']} yil umr ko'rgan.")