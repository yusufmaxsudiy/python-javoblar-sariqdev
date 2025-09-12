# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'maxsudov',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#  }
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit:{kalit}")
#     print(f"Qiymat:{qiymat}\n")
##################################################
# telefonlar = {'ali': 'iphon x',
#               'vali': 'galaxy',
#               'olim': 'nokia',
#               'orif': 'mi 10',
#               'anvar': 'pixel 3xl'
#               }
# for k,q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")
#
##################################################

mevalar = {'olma':10000,
             'tarvuz':12000,
            'qovun':7000,
             'uzum':25000,
             "anjir":40000
             }
# # print(mevalar.keys())
# print("Do'kondagi mahsulotlar:")
# for mahsulot in mevalar.keys():
#     print(mahsulot.title())

# print("Do'kondagi mahsulotlar:")
# for mahsulot in mevalar:
#     print(mahsulot.title())
##############################################
bozorlik = ['anor','uzum','non','anjir']
for mahsulot in mevalar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mevalar[mahsulot]} so'm")
for buyum in bozorlik:
    if buyum not in mevalar:
        print(f"Iltimos, do'konga {buyum} ham olib keling")

print(type(bozorlik))
#
####################################
# print("Bor mahsulotlar:")
# for mahsulot in sorted(mevalar):
#     print(mahsulot.title())
###############################

# telefonlar = {'ali': 'iphon x',
#               'vali': 'galaxy',
#                'olim': 'nokia',
#                'orif': 'mi 10',
#                'anvar': 'pixel 3xl',
#                'zulfizar':'iphon x',
#                'anvar':'iphon x',
#                'behzod':'note 9',
#                'bilol':'nokia'
#                }
# # print(telefonlar.values())

# print("Quyidagi telefonlarni ishlatadi:")
# for tel in set(telefonlar.values()):
#     print(tel)

# ####################################
# toys = {"ball","car","lamp","ball"}
#####################################
# python_lugat = {"boolean":"Mantiqiy qiymat",
#                 "float":"O'nlik son",
#                 "for":"Biror amalni qayta-qayta bajarish sikli",
#                 "if":"Shartlarni tekshirish operatori",
#                 "integer":"Butun son",
#                 "string":"Matnli qiymat",
#                 "round":"Butun qiymatini oladi",
#                 "list":"ro'yxat",
#                 "dictionary":"Lug'at ma'lumot turi",
#                 }

# for k,q in sorted(python_lugat.items()):
#     print(f"{k.title()} - {q}")





