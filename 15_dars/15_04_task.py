menu = {"osh":35000,
        "norin":85000,
        "sho'rva":25000,
        "bishteks":40000,
        "lag'mon":38000,
        "manti":28000,
        "salat":17000,
        "shashlik":15000,
        "no'xot":17000,
        "non":5000}
taomlar = []
print("3 ta taom buyurtma bering.")
for n in range(3):
    element = input(f"{n+1}-taom:")
    taomlar.append(element)

for k in menu:
    if k in taomlar:
        print(f"{k.title()} {menu[k]}")
for k2 in taomlar:
    if k2 not in menu: 
        print(f"Kechirasiz, bizda {k2} yo'q")
