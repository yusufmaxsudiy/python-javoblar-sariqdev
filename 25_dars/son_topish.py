import random as r

def son_top(x=10):
    # ishora = True
    ehtimol = r.randint(1,x)
    print("Keling o'ylagan sonni topish o'ynaymiz\n")
    son = input(f"1 dan {x} gacha son o'yladim. Topa olasizmi?")
    son = int(son)
    marta = 0
    
    while True:
        marta +=1
        if son == ehtimol:
            print(f"TOPDINGIZ! bu son {son} edi. {marta} ta taxmin bilan topdingiz.")
            return marta
        elif son>ehtimol:
            son = int(input("Xato men o'ylagan son bundan kichikroq. Yana harakat qilib ko'ring:"))

        elif son<ehtimol:
            son = int(input("Xato men o'ylagan son bundan kattaroq. Yana harakat qilib ko'ring:"))
    return marta


def son_top_pc(x=10):
    
    input(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman.\n"
                    f"Son o'ylagan bo'lsangiz istalhan tugmani bosing")
    tahmin_soni = 0
    min = 1
    max = x
    
    while True:
        son = r.randint(min,max)
        raqam = input(f"Siz {son} sonini o'yladingiz: To'g'ri bo'lsa (T), men o'ylagan son bundan kattaroq bo'lsa (+), yoki kichikroq bo'lsa(-)??").lower()
        tahmin_soni +=1
        if raqam == 't':
            print(f"Soningizni {tahmin_soni} taxmin bilan topdim!")
            return tahmin_soni
            
        elif raqam == '+':
            min = son+1
        elif raqam =='-':
            max = son-1
    


def ishla():
    yana = True
    while yana:
        a = son_top()
        b = son_top_pc()
        if a == b:
            print(f"\nDurrang, hisob {a}:{b}")
        elif a < b:
            print(f"\nSiz yutdingiz, hisob {a}:{b}")
        else:
            print(f"\nMen yutdim, hisob {a}:{b}")
        yana = int(input("Yana o'ynashni istaysizmi? Ha(1)/Yo'q(0)"))
ishla()

        
