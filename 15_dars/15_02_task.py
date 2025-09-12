davlatlar = {"aqsh":"washington d.c",
             "italiya":"rim",
             "malayziya":"kuala-lumpur",
             "o'zbekiston":"toshkent",
             "qirg'iziston":"bishkek",
             "qozog'iston":"ostona",
             "rossiya":"moskva",
             "singapur":"singapur",
             "tojikiston":"dushanbe"}
print("Dunyo davlatlari:")
for k in sorted(davlatlar.keys()):
    print(k.upper())
print("Davlatlarning poytaxtlari:")
for q in sorted(davlatlar.values()):
    print(q.title())