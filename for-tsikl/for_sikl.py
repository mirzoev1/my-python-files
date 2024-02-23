ismlar = ['ali','vali','hasan','husan','olim']
for ism in ismlar:
    print("assalomu alaykum " ,ism)
    print("sizni shanbe kuni bulib utadigon imtonga taklif qilaman",ism )

cars= ['bmw','mers','audi','tayotta']
for moshin in cars:
    print(moshin.upper())
print('Kurmagansan hayotda'.title())

raqamlar= list(range(1,11))
for raqam_kvadrati in raqamlar:
    print(f"{raqam_kvadrati} ning kvadrati {raqam_kvadrati **2 } ga teng\n ")

sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar ,'\n>>>')
print(sonlar_kvadrati)


dustlarim = []
print('5 ta eng yaqin dustingiz nomi nima?')
for dustim in range(6):
 dustlarim.append(input(f"{dustim+1}- ismini kiriting:\n>>>"))
 print(dustlarim)
