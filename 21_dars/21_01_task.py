def katta_harf(nomlar):
    n = len(nomlar)
    for ism in range(n):
        nomlar[ism] = nomlar[ism].title()
        
ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)
