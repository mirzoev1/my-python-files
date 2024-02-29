# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 18:17:27 2024

@author: Shukurullo
"""
# #1
# python_keys ={
#    'keys()':'kalit so\'z',
#    'values()':'qiymat',
#    'title()':'matnni Katta Harfda chop etish',
#    "for":'biror amalni qayta-qayta takrorlash',
#    'if ':'biror shartni bajarish',
#    'typle':"O'zgarmas Ruyxat",
#    'integer':'butun sonlar 5',
#    'float':'o\'nlik sonlar',
#    'boolean':'mantiqiy qiymatlar',
#    'while':'nomalum qiymatni tekshirish'
   
#   }
# for k,q in sorted(python_keys.items()):
#     print(f"bu kalit  {k}")
#     print(f"bu qiytmat {q}\n")
    
#2
# countries ={
#     'tajikistan':"dushanbe",
#     'kazakhstan':'astana',
#     'turkey':'ankara',
#     'uzbekistan':'tashkent',
#     'rossiya':'moskva',
#     'china':'pekin',
#     'aqsh':'vashington',
#     'saudia':'er riyod',
#     'turkmenistan':'ashqabat',
#     'angliya':'london',
#     'braziliya':'brazilia'
   
#     }
# for state, capital in sorted(countries.items()):
#       print("Davlatlar nomi")
#       print(f"{state.title()}\n")  
#       print("davlat poytaxti")
#       print(f"{capital.title()}")
     
     
# #3

# davlat = input("istalgan davlat nomi>>> ").lower()
# state = countries.get(davlat)
# if state == None:
#     print('bunday davlat mavjud emas')
# else:
#     print(state)

    

menu ={
        'osh':20,
        'mantu':30,
        'lagman':15,
        'sambusa':7,
        'shashlik':20,
        'shurvo':15,
        'lavash':30,
        'pizza':25,
        'dimlama':10,
        'chuchvara':25}

print("istalgan 3 ta ovqat nomi")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1} ovqat   ".lower()))
for buyurtma in buyurtmalar:    
 if buyurtma in menu:
     print(f"{buyurtma.title()}   {menu[buyurtma]} sum")
 else:
        print(f"bunday {buyurtma} yuq ")

