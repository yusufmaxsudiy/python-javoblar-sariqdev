
# # print("Salom, Dunyo!")
# # print("Salom, \tDunyo!")
# # print("Salom, \nDunyo!")

# # ism = 'Muhammad'
# # familiya = 'Ali'

# # print()

# # ism = input("Ismingiz nima?\n>>>")
# # print("Salom, " + ism.upper())

# # kocha = input("Qaysi ko'chada yashaysiz?\n")
# # mahalla = input("Mahallani ayting?\n")
# # print(kocha, " kochasi,", mahalla, " mahallasida yashayman")
# print(kocha , "ko'chasi,\n", mahalla, "mahallasi,\n", tuman, "tumani,\n" , viloyat, "viloyati\n")

# a = 20
# b = 5.5
# temp = 36.6
# print(type(a))
# aholi_soni = 7_594_376_567
# print(aholi_soni)
# c = a*b

# radius = 20
# PI = 3.14159
# diametr = 2*radius
# print("Aylana uzunligi=", PI*diametr)

# t_yil = int(input("Tug'ilgan yilingizni kiriting:\n"))
# yosh = 2025 - t_yil
# print("Siz ", yosh, " yoshdasiz")

# son = int(input("Istalgan sonni kiriting:\n"))
# print(son, " ning kvadrati ", son**2, " ga teng")
# print(son, " ning kubi ", son**3, " ga teng")

# yosh = int(input("Yoshingiz nechida?\n"))
# print("Siz ", 2025-yosh, " da tug'ilgansiz")

# son1 = float(input("Birinchi sonni kiriting:\n"))
# son2 = float(input("Ikkinchi sonni kiriting:\n"))
# print((son1), '+', (son2), '=', (son1)+(son2))
# print((son1), '-', (son2), '=', (son1)-(son2))
# print((son1), '*', (son2), '=', (son1)*(son2))
# print((son1), '/', (son2), '=', (son1)/(son2))

# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# print(f"{a}+{b}=", a+b)
# print(f"{a}-{b}=", a-b)
# print(f"{a}x{b}=", a*b)
# print(f"{a}/{b}=", a/b)

# mevalar = ['olma','anjir','shaftoli','nok']
# print(mevalar)
# ismlar = ['Ali', 'Vali', "G'ani"]
# print(f"Salom {ismlar[-3]}, bugun choyxona bormi?")
# print(f"{ismlar[-2]}, choyxonaga borasanmi?")

# sonlar = [4,8,9,6.3,7,-15,-5.69]
# sonlar[0] = sonlar[0]+2
# sonlar[3]=8956532
# print(sonlar)

# t_shaxslar = ["Imom Buxoriy", "Forobiy", "Termiziy", "Farg'oniy"]
# z_shaxslar = ["Zafar Xoshimov", "Mask", "Mirziyoyev"]
# t_xohlayman = t_shaxslar.pop(2)
# z_xohlayman = z_shaxslar.pop(2)
# print(f"Men tarixiy shaxslardan {t_xohlayman} bilan, zamonaviy shaxslardan esa {z_xohlayman} bilan suhbat qilishni istar edim")

# cars = ['bmw','mercedes benz','volvo','general motors','tesla','audi']
# cars.sort()
# print(cars)



# mehmonlar = ['Ali','Vali','Hasan','Olim','Sanjar']
# for mehmon in mehmonlar:
#     print("Salom", mehmon)
#     print("Hayr", mehmon)


# mehmonlar = ['Ali','Vali','Hasan','Olim','Sanjar']
# for mehmon in mehmonlar:
#     print(f"\nHurmatli {mehmon}, sizni 6-sentabr kuni nahorgi oshga taklif etamiz")
#     print("Hurmat bilan, Maxsudovlar oilasi\n")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)


# dostlar = []
# print("5 ta do'stingizni kiriting")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-dostingizni kiriting:\n"))
# print(dostlar)

# tanishlar = ['Salim','Karim','Hasan','Husan','Nodir']
# for tanish in tanishlar:
#     print(f"Salom {tanish}, nima gaplar")
# print(f"Kod {len(tanishlar)} marta takrorlandi")



# toqlar = list(range(11,101,2))
# for son in toqlar:
#     print(f"{son**3}")

# kinolar = []
# print("Eng yaxshi ko'rgan 5ta kinoyingiz qaysilar?")
# for n in range(5):
#     kinolar.append(input(f"{n + 1}-kinoni kiriting: "))
# print(kinolar)


# odamlar = []
# soni = int(input("Bugun necha kishi bilan suhbat qildingiz?>>>"))
# for n in range(soni):
#     odamlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi:"))
# print(odamlar)


# avtolar = ['audi','bmw','volvo','kia','hyundai']

# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# ism = input('Ismingiz nima?\n>>>')
# if ism.lower() != 'ali':
#     print(f"Uzur, {ism.title()} biz Alini kutyapmiz.")
# else:
#     print("Salom, Ali")


# javob = float(input("12*6 nechiga teng?>>>"))
# if javob != 72:
#     print("Javob xato!!!")


# yosh = int(input("Yoshingizni kiriting:\n>>>"))
# if yosh>=18:
#     print("Xush kelibsiz")
# else:
#     print("Kirish mumkin emas!!!")

# print(yosh)

# login = input("Yangi login tanlang:")
# if len(login)<=5:
#     print("Login 5 xarfdan ko'p bo'lishi kerak!")
# else:
#     print(f"Login: {login}")

# yil = int(input("Yilingizni kiriting:"))
# if 2025-yil<18:
#     print(f"Yoshingiz {2025-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz")

# yosh =int(input("Yoshingiz nechida?>>"))
# if yosh>65: print("Siz covid riski guruhida ekansiz")

# x, y = 50, 50
# print("x>y") if x>y else print("x<y")

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# ism = input("Ismingiz?\n>>>")
# if ism.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {ism}!")




# son = float(input("Istalgan sonni kiriting:\n>>>"))
# if son<0:
#     print("Musbat son kiriting")
# else:
#     print(f"ildizi: {(son**0.5)}")

# son = 50
# if son<0:
#     print("Manfiy son")
# else:
#     print("Musbat son")


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     narx = 0
# elif yosh<=12:
#     narx = 5000
# elif yosh <=18:
#     narx = 8000
# else:
#     narx = 10000
# print(f"Sizga kirish {narx} so'm")

# kun = input("Bugun qaysi kun?>>>")
# if kun.lower()=='shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print("Bugun ish kuni.")

# kun = input("Bugun qaysi kun?")
# harorat = float(input("Havo harorati qanday?"))

# if (kun.lower() == 'yakshanba' or kun.lower()== 'shanba')and harorat>=30:
#     print("Ketdik")
# elif (kun.lower() == 'yakshanba' or kun.lower()== 'shanba') and harorat<30:
#     print("Uydamiz")


# narx = 15000

# choy = True
# salat = True

# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000

# print(f"Jami {narx} som")


# narx = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1

# if choy:
#     print("Mijoz choy ichdi.")
#     narx = narx + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narx = narx + 5000
# if non:
#     print("Mijoz non oldi.")
#     narx = narx + 4000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narx = narx + 7000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narx = narx + 15000

# print(f"Jami {narx}")

# menu = ['osh','somsa','norin','shashlik','manti']
# ovqat = input("Nima ovqat yeysiz?\n>>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday taom yo'q")

menu = ['osh','norin','shashlik','manti']
buyurtmalar = ['osh','somsa','manti']
for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")











