def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *=son
    return natija


print(kopaytma(5,6,4))