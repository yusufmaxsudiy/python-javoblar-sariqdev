# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# height = float(height)
# print(ism.title(), yosh, height)

# son = 1
# while son <= 5:
#     print(son)
#     son += 1  # shu "son = son + 1" ga teng
# print("dastur tugadi")

# print("Sonning kvadratini chiqaruvchi dastur.")
# savol = "Son kiriting "
# savol+= "(dasturni to'xtatish uchun 'exit deb yozing): "
# qiymat = ' '
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi")

#ishora
# print("Sonning kvadratini chiqaruvchi dastur.")
# savol = "Son kiriting "
# savol+= "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi")

#break
# print("Sonning kvadratini chiqaruvchi dastur.")
# savol = "Son kiriting "
# savol+= "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi")

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 6:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 6:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son <10:
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)

#infinite loop
# son = 0
# while son <10:
    
#     if son%2 != 0:
#         continue
#     else:
#         print(son)

# son = 0
# while son <10:
    
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
#     son += 1


son = 1
while son >0:
    son +=1
    if son%2 != 0:
        continue
    else:
        print(son)










