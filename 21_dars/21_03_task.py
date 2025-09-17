# def bahola(ismlar):
#     baholar = {}
#     i = 0
#     while i < len(ismlar):
#         ism = ismlar[i]
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting:")
#         baholar[ism.title()] = int(baho)
#         i += 1
#     return baholar
# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)
talabalar = ['ali', 'vali', 'hasan', 'husan']

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
        
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
