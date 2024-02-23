# UPPER() funksiyasi mayda harflarni KATTA harflarga ugirish 
ism='Anvar'
familiya='Narzullaev'
ism_sharif=f'{ism} {familiya}'
ism_sharif = ism_sharif.upper()
print(ism_sharif.upper())


#lover() KATTA harfni kichik harfga o'giradi
print(ism_sharif.lower())

#title() Har Bir Suzning Bosh Harfini Katta Qiladi
ttile = 'har bir suzning bosh harfini katta qiladi'
print(ttile.title())

#capitalize() matndagi Bosh hafrni katta qiladi
bharf_katta='bosh hafrni katta qiladi'
print(bharf_katta.capitalize())

#uzgaruvhcisiz ham qullab buladi
print('hello wordl!'.upper())

meva="      OLMA     "
print (meva)
print(" Men  " + meva.lstrip() + "yaxshi ko'raman")
print(" Men " + meva.rstrip() + '  '  "yaxshi ko'raman")
print(" Men " ' '+ meva.strip() + ' ' "yaxshi ko'raman")
meva=meva.strip()
print(meva)
 
 
