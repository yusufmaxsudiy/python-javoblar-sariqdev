savol = "Yoshingizni kiriting:"
savol += "(To'xtatish uchun 'exit' yoki 'quit' kiriting):"

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)

    if float(yosh)<7:
        print("2000 so'm")
    elif 7<=float(yosh)<18:
        print("3000 so'm")
    elif 18<=float(yosh)<65:
        print("10000 so'm")
    elif float(yosh) >= 65:
        print("Bepul")
print("Tugadi")