avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())
        
javob = float(input("9*8 nechiga teng >>>"))
if javob !=40:
    print("Javob hato")
    
yosh=int(input("Yoshingiz nechida>>>" ))
if yosh >= 18:
    print('Xush kelibsiz')
else:
        print("Sizga kirish taqiqlanadi")

yil = int(input("Tugilgan yilingizni kiriting"))
if 2024 - yil >18:
    print(f"Yoshingiz {2024 - yil} da ekan ")
    print("Sizga kirish mumkin emas")
else:
    print("Hush Kelibsiz")
login =str(input("Yangi login kiriting"))
if len(login)<=5:
    print("Login 5 harfdan ko'proq bo'lishi shart")
else:
    print("Siz muvaffaqli ravishda ruyhatdan utdingiz")
    