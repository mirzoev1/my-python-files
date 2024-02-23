# car = {'model':'Tico','rang':'Qizil'}
# print(car)
# print(car['model'])
# print(car['rang'])


# INT STRING QIYMATLAR
# talaba = {'ism': 'Shukurullo', 'yosh': 19, 't_yil': 2004}
# print(f"{talaba['ism'].title()}, "
#       f"{talaba['t_yil']} - yilda tugilgan, "
#       f"{talaba['yosh']} - yoshda")
# LUGATGA KALIT QO'SHISH
# talaba['kurs'] = 2
# talaba['Fakultet'] = 'telecom'
# print(talaba)

# LUGATNI TAGMA TAG YOZISH

# car ={
#    'make':'tayota',
#    'model':'cambry',
#    'color':'White',
#    'year':2020,
#    'price':45000
#  }
# print(car['color'],car['price'],car['model'])
# narx = car.get('narx')
# print(narx)

# QIYMATINI O'ZGARTIRISH
# car['price'] = 4000
# year['year'] = 2018


# BO'SH LUGAT
# phone ={}
# phone['model'] = 'samsungS9'
# phone['color'] = 'black'
# phone['price'] = 150
# print(f" {phone['model']} {phone['color']} {phone['price']}$")

# LUGATDAN KALITLARNI O'CHIRISH
# language ={'uz':'salom','eng':'Hello','ru':'Привет',}
# print(language)
# DEL funksiyasi
# del language['ru']
# print(language)

phone = {
    "brand": "Samsung",
    "model": "Galaxy S21",
    "year": 2021,
    "color": "Phantom Black",
    "storage": "256GB",
    "price": 999.99
}

print("Brand:", phone["brand"])
print("Model:", phone["model"])
print("Year:", phone["year"])
print("Color:", phone["color"])
print("Storage:", phone["storage"])
print("Price:", phone["price"])
