print("Buyurtmalarni qabul qiluvchi dastur:")
buyurtmalar = []
while True:
    savol = f"Buyurtmangizni kiriting:"
    javob = input(savol)
    buyurtmalar.append(javob)
    takror = input("Davom ettirasizmi? (ha/yo'q)")
    if takror !='ha':
        break
print("buyurtmalar ro'yxati:")
for n in buyurtmalar:
    print(n.title())