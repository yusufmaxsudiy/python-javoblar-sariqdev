# 16-dars nesting

# car0 = {'model':'lacetti',
#         'rangi':'oq',
#         'yil':2020,
#         'narx':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {'model':'nexia 3',
#         'rangi':'qora',
#         'yil':2021,
#         'narx':8000,
#         'km':78000,
#         'korobka':'mexanika'
#         }

# car2 = {'model':'gentra',
#         'rangi':'qizil',
#         'yil':2019,
#         'narx':14000,
#         'km':22000,
#         'korobka':'mexanika'
#         }

# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rangi']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")

# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['rangi']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")

# car = car2
# print(f"{car['model'].title()}, "
#       f"{car['rangi']} rang, "
#       f"{car['yil']}-yil, {car['narx']}$")


# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#         f"{car['rangi']} rang, "
#         f"{car['yil']}-yil, {car['narx']}$")

# print(cars[0])
# print(cars[0]['model'])  #ro'yxat ichidagi kalit so'z bo'yicha chiqarish

# malibus = []
# for n in range(10):
#     new_car = {'model':'malibu',
#         'rangi':None, #rangi noaniq
#         'yil':2020,
#         'narx':None,
#         'km':0,
#         'korobka':'avtomat'
#         }
#     malibus.append(new_car)
# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus[:3]:
#     malibu['rangi'] = 'qizil'

# for malibu in malibus[3:6]:
#     malibu['rangi'] = 'qora'

# for malibu in malibus[6:]:
#     malibu['rangi'] = 'oq'
#     malibu['korobka'] = 'mexanika'
# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus:
#     if malibu['korobka']=='avtomat':
#         malibu['narx'] = 40000
#     else:
#         malibu['narx'] = 35000

# for malibu in malibus:
#     print(malibu)

# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#'],
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper(), end=' ')


hamkasblar = {'ali':{'familiya':'valiyev','tyil':1995,'malumot':'oliy','tillar':['python','c++']},

    'vali':{'familiya':'aliyev','tyil':2001,'malumot':"o'rta-maxsus",'tillar':['html','css','js']},

    'hasan':{'familiya':'husanov','tyil':1999,'malumot':'maxsus','tillar':['python','php']}
    }
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
           "Quyidagi dasturlash tillarini biladi:"
           )
    for til in info['tillar']:
        print(til.upper())













