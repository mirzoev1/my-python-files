#integer butun sonlar 
a = 20
b = -30
c=0
d= a + b
print ( d)
kvdrt_tmni = 20
kvdrt_yuzi = kvdrt_tmni ** 2
print(kvdrt_yuzi)

#float o'nlik sonlar 
pi = 3.14159
radius = 10
diametr = 2 * radius
print("aylananing uzunligi ",pi * diametr,' ga teng')


#bir nechta uzgaruvchiga qiymat berish
x,y,z = 12,32,-54
c = x + y+z
print(c) 

yosh ,ism = 36, 'Shukurullo'
print(f"{ism} {yosh} yoshda \n")


#uzgaruvchi turini almashtirish
xabar = ism +' '+str(yosh)  + 'yoshda'
print(xabar) 


#uzgaruvchining tipini tekshiramiz
print (type(yosh))
print (type(ism))

#sonlarda input()funksiyasi
t_yil = int(input("Tugilgan yilingizni kiriting\n>>>"))
yosh = 2024 - t_yil
print(f"siz  {yosh}  yoshda ekansizku")

print(type(t_yil))
