def katta_harf(nomlar):
    yangi_ismlar = []
    i = 0
    while i < len(nomlar):
        
        yangi_ismlar.append(nomlar[i].title())
        i +=1
    return yangi_ismlar
        
ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)


