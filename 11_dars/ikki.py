yosh = int(input("Yoshingiz nechada?:"))
if yosh <=4:
    narx = 0
elif yosh <18:
    narx = 10000
elif yosh < 60:
    narx = 20000
else:
    narx = 0
print(f"Kirish siz uchun {narx} so'm")