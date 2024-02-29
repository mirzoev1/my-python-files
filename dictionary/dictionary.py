
             # ITEMS() metodi
# talaba_0={
#     'ism':'Shukurullo',
#     'familiya':'Mirzoev',
#     'yosh':19,
#     'fakultet':'telecom',
#     'kurs':2
#     }
# #print(talaba_0.items())
# for key, value in talaba_0.items():
#     print(f"key: {key}")
#     print(f"value: {value}\n")    

    

# phones ={
#     'ali':'calaxy s22+',
#     'alisher':'redmi note 12 pro',
#     'jahongir':'iphone 13 pro',
#     'samad':'POCO 20 30',
#     'umar':'realme c10',
#     'sobit':'techno spark 10'
    #}

    
# for k,q in phones.items():
#     print(f"{k.title()} ning telefoni {q}\n")


# keys() metodi

# maxsulotlar ={
#     'olma':10,
#     'anor':25,
#     'uzum':15,
#     'shaftoli':10,
#     'olucha':5,
#     'zardolu':20
#     }

# #print(maxsulotlar.keys())

# print('Do\'konimizdagi maxsulotlar')

# for maxsulot in maxsulotlar.keys(): #keys() ishlatsak xam bo'ladi ishlatmasak xam
#     print(maxsulot.title())
   
 #do'konda nima bor nima yo'qligini tekshiradigan dastur
#list bozorlik
# bozorlik =['olma','anor','uzum','non','sabzi','tuz','anor','uzum']
# for maxsulot in maxsulotlar:
#   if maxsulot in bozorlik:
#       print(f"{maxsulot.title()}  {maxsulotlar[maxsulot]} сомон")     

# for maxsulot  in maxsulotlar:
#  if maxsulot not in bozorlik:
#      print(f"iltimos do'koningizga  {maxsulot} xam olib keling")
  

#values() faqat qiymatlarini chiqarish
  
# cars ={
# 'Hurshed':'malibu',
# 'ali':'tesla',
# 'vali':'tico',
# 'gani':'opel',
# 'salohiddin':'opel',
# 'shuhrat':'tesla',
# 'anvar':'damas',
# 'bobur':'opel',
# 'nozim':'malibu'
#        }
# #print(cars.values())
# print('foydalanuvchilarda quyidagi moshinlar bor')
# for car in cars.values():
#     print(car)



#set() funksiyasi yordamida tartiblash
# cars ={
# 'khurshed':'malibu',
# 'ali':'tesla',
# 'vali':'tico',
# 'gani':'opel',
# 'salohiddin':'opel',
# 'shuhrat':'tesla',
# 'anvar':'damas',
# 'bobur':'opel',
# 'nozim':'malibu'
#         }
# print('foydalanuvchilarda quyidagi moshinalar bor')
# for car in set(cars.values()):
#     print(car)
    

#SET malumot turi xaqida faqat bitta malumotni chiqaradi
toys = {'bear','car','ball','lego','lego','car','bear','ball'}
print(toys)



#sorted() funksiyasi a- z bo'yicha tartiblash
cars ={
'khurshed':'malibu',
'ali':'tesla',
'vali':'tico',
'gani':'opel',
'salohiddin':'opel',
'shuhrat':'tesla',
'anvar':'damas',
'bobur':'opel',
'nozim':'malibu'
        }

print('foydalanuvchilar')
for car in sorted(cars):
    print(car.title())      
       
