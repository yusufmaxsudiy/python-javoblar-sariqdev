davlatlar = {"aqsh":"washington d.c",
             "italiya":"rim",
             "malayziya":"kuala-lumpur",
             "o'zbekiston":"toshkent",
             "qirg'iziston":"bishkek",
             "qozog'iston":"ostona",
             "rossiya":"moskva",
             "singapur":"singapur",
             "tojikiston":"dushanbe"}

davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz?:")
davlat = davlat.lower()
if davlat in davlatlar:
    print(f"{davlat.upper()}ning poytaxti {davlatlar[davlat].title()}")
else:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")