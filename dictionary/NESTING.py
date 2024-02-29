# # -*- coding: utf-8 -*-
# """
# Created on Mon Feb 26 12:05:27 2024

# @author: SHUKURULLO
# """

car0 = {'model':'BMW',
        'color':'black',
        'year':2005,
        'km':50000,
        'price':13000,
        'karobka':'avtomat'
        }


car1 = {'model':'MERS',
        'color':'blue',
        'year':2010,
        'km':980000,
        'price':18000,
        'karobka':'mexanika'
        }



car2 = {'model':'Tayotto',
        'color':'white',
        'year':2012,
        'km':21000,
        'price':25000,
        'karobka':'avtomat'
        }

car = car0
print(f"{car['model']}, rang {car['color']},",
      f"{car['year']} -yil, {car['km']}-km",
      f"{car['price']}-$, {car['karobka']}")


car = car1
print(f"{car['model']}, rang {car['color']},",
      f"{car['year']} -yil, {car['km']}-km",
      f"{car['price']}-$, {car['karobka']}")


car = car2
print(f"{car['model']}, rang {car['color']},",
      f"{car['year']} -yil, {car['km']}-km",
      f"{car['price']}-$, {car['karobka']}\n")


#yuqoridagi bilan quyidagi natijalar bir xil 
#lekin yuqorida kod kup yozilgan

cars = [car0,car1,car2]

for car in cars:
    
    print(f"{car['model']}, rang {car['color']},",
      f"{car['year']} -yil, {car['km']}-km",
      f"{car['price']}-$, {car['karobka']}\n")


print(f"{cars[0]['color'].title()}",
      f"{cars[0]['model']}")


print(cars[1]['color'])



#for() tsikli yordamida bo'sh lugatlar yaratamiz
malibus =[]
for n in range(10):
    new_car = {#xar bir avto uchun lugat yaratamiz
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narx':None,
        'km':0,
        "karobka":'avtomat'
        }
    malibus.append(new_car)
#print(malibus)    
#print(new_car)


#avvalgi 3 ta avtoning rangini qizil qildik
for malibu in malibus[:3]:
    malibu['rang']='qizil' 
    
# 3 dan 6 gacha avtoning rangini qora qildik    
for malibu in malibus[3:6]:
    malibu['rang'] ='qora'    

#oxirgi 4 ta  avtoning rangini qora va karobkasini mexanik qildik
for malibu in malibus[6:]:
    malibu['rang']='qora',
    malibu['karobka'] = 'mexanik'
    
#endi avtolarning karobkasiga qarab narx belgilaymiz
for malibu in malibus:
    if malibu['karobka']=='avtomat':
        malibu['narx'] = 60000
    else:
        malibu['narx']=55000
        
for malibu in malibus:
    print(malibu,"\n\n")


programmer = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'muxabbat':['c++','c#']
    }
for ism,tillar in programmer.items():
    print(f"\n{ism.title()}:",end='')
    for til in tillar:
        print(f"{til.upper()} ",end='')


xamkursho = { 
    'samad':{'familiya':'karimov',
              't_yil':2002,
              'malumot':'oliy',
              'tillar':['python', 'c++']},
    
    
    'abror':{'familiya':'malikov',
              't_yil':1999,
              'malumot':'orta maxsus',
              'tillar':['java,js,php']},
        
    
    'asror':{'familiya':'qaxxorov',
              't_yil':2003,
              'malumot':'maxsus',
              'tillar':['html', 'css', 'js']},
        
            }

for ism,info in xamkursho.items():
        print(f"\n{ism.title()} {info['familiya'].title()},"
          f"{info['t_yil']} yilda tugilgan. \n"
          f"malumoti: {info['malumot' ]}.\n"
          "quyidagi dasturlash tillarini biladi:  ")
        for til in info['tillar' ]:
            print(til.upper())







































