

python={'for':'uchun',
        'if':'agar',
        'else':'aks holda',
        'elif':'aks holda agar',
        'dictionary':'lugat',
        'input':'kiritish',
        'and':'va',
        'or':'yoki',
        'title()':'Matn Uchun',
        'float':'10.50 shunaqa sonlar uchun',
        'list':'ruyhat'
}
print(python)


kalit = input('dasturlashga oid suz yozing').lower()
print(python.get(kalit,'bunday kalit mavjud emas'))



kalit = input("Kalit so'z kiriting:").lower()
tarjima = python.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

