def avto_info(kompaniya, model, rang, korobka, yil, narx=None): 
    """ma'lumotlarni lug'at qilib qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rang,
            'korobka':korobka,
            'yil':yil,
            'narx':narx}
    return avto

def avto_kirit():

    avtolar=[]
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting", end='')
        kompaniya = input("\nIshlab chiqaruvchi: ")
        model = input("Model: ")
        rang = input("Rangi: ")
        korobka = input("Korobka: ")
        yil = input("Ishlab chiqarilgan yili: ")
        narx = input("Narxi: ")

        avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narx))

        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
    return avtolar

def info_print(avto_info):
    """Lug'atni konsolga chiqaradi"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, ${avto_info['narx']}")






