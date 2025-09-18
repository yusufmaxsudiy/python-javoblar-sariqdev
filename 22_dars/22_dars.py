# def avto_info(kompaniya, model, rang, korobka, yil, narx=None): 
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rang,
#             'korobka':korobka,
#             'yil':yil,
#             'narx':narx}
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000,)
# avtolar = [avto1,avto2]
# print("Bozorda mavjud mashinalar:")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narxi: {narx}")
# yuqoridagi misolda argumentlar cheklangan, bu darsda cheklanmagan argument berishni o'rganamiz

# *arg va **kwargs
# def summa(*sonlar): #shu joyda sonlarning tipi tuple bo'ladi list emas 
#     """Sonlar yig'indisini hisoblaydi"""
#     # yigindi = 0
#     # for son in sonlar:
#     #     yigindi+= son
#     # return yigindi
#     return sum(sonlar)

# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))

# def summa(x,y,*sonlar):
#     """Sonlar yig'indisini hisoblaydi"""
#     return x+y+sum(sonlar)

# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))


def avto_info(kompaniya, model, **malumotlar):
    """avto ma'lumotlar lug'at shaklda"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto1 = avto_info('gm','malibu', rang='qora', yil=2018)
avto2 = avto_info('kia','k5',rang='qizil',narx=35000, yil=2020)
print(avto2)








