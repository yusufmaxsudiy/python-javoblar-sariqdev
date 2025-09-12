foydalanuvchilar = ['admin','direktor','xodim','ishchi','haydovchi']
login = input("Yangi login kiriting:\n>>>")
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {login.title()}")
