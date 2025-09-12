# print("Yaqin do'stlar ro'yxatini tuzamiz.")
# ismlar = []
# n=1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != 'ha':
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kirirting:")
#     yosh = input(f"{ism.title()}ning yoshini kirirting:")
#     dostlar[ism] = int(yosh)

#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
# for ism , yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# car = 'lacetti'
# while car in cars:
#     cars.remove(car)
# print(cars)

talabalar = ['hasan','husan','olim','botir']
baholanganlar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting:")
    print(f"{talaba.title()} baholandi")
    baholanganlar[talaba] = int(baho)
for n in baholanganlar.items():
    print(n)





