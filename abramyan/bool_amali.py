# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 21:59:54 2024

@author: Admin
"""

'''son = int(input("Juft son kiriting   "))
if son % 2 == 0:
    print("RAXMAT")
else:
    print("Bu juft son emas")
'''

'''yosh = int(input("Yoshingiz nechida   ")) 
if yosh <= 4 or yosh >= 60 :
    print("Siz uchun Muzeyga kirish bepul")
elif yosh < 18:
    print("Siz uchun muzeyga kirish 10 sum")
elif yosh >18:
    print("Siz uchun muzeyga kirish 20 sum")
    '''
'''
son1 = int(input("Birinchi sonni kiriting   "))
son2 = int(input("ikkinchi sonni kiriting   "))
if son1 == son2:
    print("Sonlar teng")
elif son1 > son2:
    print(f"{son1}  {son2}  dan katta ")
else:
     print(f"{son2}  {son1}  dan katta")
     '''
maxsulotlar =["gurunch",'moy','cola','banan','gusht','sabzi','olma','tuxum','non','piyoz','makaron']  
savat =[]
print("savatga 5 ta maxsulot kiriting")
for n in  range(5):
 savat.append(input(f"{n +1} maxsulotni kiriting    "))
for nomalum in maxsulotlar:
 if   nomalum in savat:
     print(f"  {nomalum} dukonimizda  bor ")
 else: 
     print(f"{nomalum} dukonimizda yuq")
    