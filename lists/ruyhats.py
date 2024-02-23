mevalar =['olma','anjir',"o'rik" ,'shaftoli','tarvuz' ,'qovun']
print(mevalar)
raqamlar =[1200,8900,1200,-7210,4200]
print(raqamlar)
ismlar = []

print(ismlar)
print("Birinchi meva " ,mevalar[0])
print("Birinchi meva " ,mevalar[-6].lower())

print("Ikkinchi meva ", mevalar[1].title())
print("Oxirgi meva ",mevalar[5].capitalize())
print("Oxirgi meva ",mevalar[-1].upper())
print(raqamlar[2] + raqamlar[0])
print(raqamlar[-3])
raqamlar[2] =  13000
print(type(raqamlar[0]))
raqamlar[3] = 3500
raqamlar[-1] = raqamlar[-1] - 200
print(raqamlar)

#.uppend() ruyhatlarga malumot qushamiz 
mevalar.append('Gilos')
print(mevalar)
ismlar.append('Shukurullo')
print(ismlar)
ismlar.append('Mahmud')
ismlar.append('Soxib')
ismlar.append('Behruz')
print(ismlar)
ismlar[-2] = 'Sohibjon'
print(ismlar)

#.insert() ruyhatlarga malumot qushamiz xoxlagan joyimizga
ismlar.insert(1,'Shahriyor')
print(ismlar)
ismlar.insert(1,'Sheroz')
ismlar.insert(3,'Sheroz')

ismlar.insert(0,'Sheroz')
print(ismlar)

#del yordamida ruyhatdan indexi buyicha malumot  uchiramiz
del mevalar[-2]
print(mevalar)
del mevalar[2]
print(mevalar)

#.remove() orqali esam uchirmoqchi bulgan malumotni yozamiz
mevalar.remove('Gilos')
print(mevalar)
mevalar.remove('anjir')
print(mevalar)
ismlar.remove('Sheroz')
print(ismlar)
ismlar.remove('Sheroz')
print(ismlar)

#.pop() funksiyasi ruyhatdan malumot sugurib olish ucgun ishlatiladi
bozorlik = ['moy','guruch','sabzi','un','piyoz','kartoshka']
maxsulot = bozorlik.pop(2)

print("Men bozordan  " + maxsulot + " sotib oldim ")
print("Olinmagan maxsulotlar",bozorlik)
bozorlik.pop()
print(bozorlik)
print(type(bozorlik))
