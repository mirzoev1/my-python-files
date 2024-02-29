# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:15:52 2024

@author: Shukurullo
"""
# #1

rudakiy ={
    'ism':'Abu Abdullox Rudakiy',
    't_yili':860,
    't_joyi':'Panjakent',
    'v_etgani':941,
    'asarlari':[None]
    }

loiq_sherai ={
    'ism':'Loiq sherali',
    't_yili':1941,
    't_joyi' : 'Panjakent',
    'v_etgani':2000,
    'asarlari':[None]
    }
jobs ={
    'ism':'Stiv jobs',
    't_yili':1955,
    't_joyi':'america',
    'v_etgani':2011,
      'asarlari':[None]
        
    }

geyts ={
    'ism':'Bill geyts',
    't_yili':1955,
    't_joyi':'america',
    'v_etgani':None,
    'asarlari':[None]
}
vazifalar=[rudakiy,loiq_sherai,jobs,geyts]

for vazifa in vazifalar:
    print(f"\n{vazifa['ism']} {vazifa['t_yili']} yilda "
          f" {vazifa['t_joyi']} da tugilgan "
          f"{vazifa['v_etgani']} yilda vafot etgan")
#2


shaxslar=[rudakiy,loiq_sherai,jobs,geyts]
for shaxs in shaxslar:
    ism= shaxs['ism']
    asarlari =shaxs['asarlari']
    print(f"\n{ism} ning mashxur asarlari")
    for asar in asarlari:
        print(asar)



#3
friend ={
    'name':'Shaxriyor',
    'love_kino':['jumong','qasoskorlar','oila uchun']
    }
print(f"Mening do'stim {friend['name']}:\n"
      f"unig sevimli kinolari {friend['love_kino']}")


#4
davlatlar = {
    'tojikiston':{
        'nomi':'tojikiston',
        'poytaxti':'dushanbe',
        'axolisi':'10 mln',
        'puli':'somoni'},
    'uzbekistan':{
        'nomi':'uzbekistan',
        'poytaxti':'tashkent',
        'axolisi':'30 mln',
        'puli':'so\'m'},
    'rossiya':{
        'nomi':'rossiya',
        'poytaxti':'moscva',
        'axolisi':'140 mln',
        'puli':'rubl'
        }
        
    }
for davlat,info in davlatlar.items():
    poytaxti = info['poytaxti']
    axolisi = info['axolisi']
    puli = info['puli']
    print(f"\n{davlat} ning poytaxti {poytaxti}\n",
          f"axolisi: {axolisi}\n"
          f"pul birligi {puli}\n")
    
#5
davlatlar1 ={
      'tojikiston':{
          'nomi':'tojikiston',
          'poytaxti':'dushanbe',
          'axolisi':'10 mln',
          'puli':'somoni'},
      'uzbekistan':{
          'nomi':'uzbekistan',
          'poytaxti':'tashkent',
          'axolisi':'30 mln',
          'puli':'so\'m'},
      'rossiya':{
          'nomi':'rossiya',
          'poytaxti':'moscva',
          'axolisi':'140 mln',
          'puli':'rubl'
          }
            }

my_davlat = input('davlat nomi?').lower()
if my_davlat in davlatlar:
    print(my_davlat)
    for malumotlar in davlatlar1:
        malumotlar = davlatlar1[my_davlat]
    for malumot,info in davlatlar1.items():
            print(f"{malumot}:{info[my_davlat]}")
else:
            print('bizda bunday davlat malumoti mavjud emas ')



davlatlar = {
    "AQSh": {
        "poytaxt": "Washington, D.C.",
        "maydon": "9.8 million kvadrat kilometr",
        "aholi": "ko'rib chiqilgan, 2021: 331.5 million",
        "pul birligi": "Dollar (USD)"
    },
    "Rossiya": {
        "poytaxt": "Moskva",
        "maydon": "17.1 million kvadrat kilometr",
        "aholi": "ko'rib chiqilgan, 2021: 146.4 million",
        "pul birligi": "Rubl (RUB)"
    },
    "Xitoy": {
        "poytaxt": "Pekin",
        "maydon": "9.6 million kvadrat kilometr",
        "aholi": "ko'rib chiqilgan, 2021: 1.41 milliard",
        "pul birligi": "Yuan (CNY)"
    },
    "Germaniya": {
        "poytaxt": "Berlin",
        "maydon": "357,386 kvadrat kilometr",
        "aholi": "ko'rib chiqilgan, 2021: 83.2 million",
        "pul birligi": "Yevro (EUR)"
    },
    "Fransiya": {
        "poytaxt": "Paris",
        "maydon": "551,695 kvadrat kilometr",
        "aholi": "ko'rib chiqilgan, 2021: 65.4 million",
        "pul birligi": "Yevro (EUR)"
    }
}

# Foydalanuvchi so'ragan davlatni kiritish
soralgan_davlat = input("Istalgan davlat nomini kiriting: ").lower()

# Davlat ma'lumotlarini tekshirish va konsolga chiqarish
if soralgan_davlat in davlatlar:
    print(f"{soralgan_davlat}:")
    malumotlar = davlatlar[soralgan_davlat]
    for malumot, qiymat in malumotlar.items():
        print(f"\t{malumot}: {qiymat}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")









