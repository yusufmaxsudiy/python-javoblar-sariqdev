python_lugat = {"boolean":"Mantiqiy qiymat",
                "float":"O'nlik son",
                "for":"Biror amalni qayta-qayta bajarish sikli",
                "if":"Shartlarni tekshirish operatori",
                "integer":"Butun son",
                "string":"Matnli qiymat",
                "round":"Butun qiymatini oladi",
                "list":"ro'yxat",
                "dictionary":"Lug'at ma'lumot turi",
                }

for k,q in sorted(python_lugat.items()):
    print(f"{k.title()} - {q}")
