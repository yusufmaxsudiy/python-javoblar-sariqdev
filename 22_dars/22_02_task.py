def talabalar(ism, familiya, **malumotlar): #malumotlar lug'at shaklda bo'ladi
    """avto ma'lumotlar lug'at shaklda"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba1 = talabalar('Ali','Hasanov', t_yil=2002)
talaba2 = talabalar('Karim','Jalolov', t_yil=2001, viloyat='Fargona')
print(talaba2)
