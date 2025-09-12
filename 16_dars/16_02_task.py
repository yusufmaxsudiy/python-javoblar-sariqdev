adib0 = {
    'ism':'Alisher Navoiy',
    'tyil':1441,
    'vafot':1501,
    'tshahar':'hirot',
    'asarlari':['xamsa','lison ut-tayr']
    }
adib1 = {
    'ism':'erkin vohidov',
    'tyil':1936,
    'vafot':2016,
    'tshahar':'oltiariq',
    'asarlari':['tong nafasi', 'oltin devor', 'nido']
    }
adib2 = {
    'ism':'zahiriddin muhammad bobur',
    'tyil':1483,
    'vafot':1530,
    'tshahar':'andijon',
    'asarlari':['boburnoma','topmadim']
}
adiblar = [adib0, adib1, adib2]

for adib in adiblar:
    print(f"\n{adib['ism'].title()} ning mashxur asarlari:")
    for asar in adib['asarlari']:
        print(asar.capitalize())
        # print("\033[1m" +asar.capitalize() + "\033[0m")