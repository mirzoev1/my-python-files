cars = ['mers','tesla','lasetti','bugatti','audi','opel','bmw','hyunday']
print(cars)


cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)
\
\
kompyuter=['dell','hp','lenovo','sony','acer','acus','fujitsu','apple','ibm','toshiba']
print(kompyuter)
print(sorted(kompyuter))
print(sorted(kompyuter,reverse=True))
print(kompyuter)

sonlar=[92,123.5,3,65,4,65,2,87,7,85,5,53,6]
print(sonlar)

print(sorted(sonlar))
print(sorted(sonlar,reverse=True))
print(sonlar)

\
sonlar.sort()
print(sonlar)

sonlar.sort(reverse=True)
print(sonlar)

print(kompyuter)

kompyuter.reverse()
print(kompyuter)

print("kompyuterlar soni" ,len(kompyuter))

print("raqamlar son",len(sonlar))

uzunlik = len(sonlar)
print(uzunlik)


#range()
raqamlar = list(range(1,100))
print(raqamlar)
toq_raqamlar = list(range(1,21,2))
print(toq_raqamlar, "\n")
jufr_raqamlar = list(range(0,21,2))
print(jufr_raqamlar)

print(max(raqamlar))
print(min(raqamlar))
print(sum(raqamlar))
raqamlar.sort()
print(raqamlar)

arzon = min(sonlar)
qimmat = max(sonlar)
jami = sum(sonlar)
print("Eng arzon narh ",arzon,".Eng qimmati",qimmat,".jami:",jami)


print(cars[2:6])
print(raqamlar[0])
print(sonlar[3:])
print(kompyuter[:4])


my_cars = cars

print(cars,"\n")
print(my_cars ,"\n")

my_cars.remove('opel')
del(my_cars[2])
my_cars.insert(1,'damas')
my_cars.append('kia')


print(my_cars,"\n")
print(cars)
#xato usuli nusha olinmadi

noutbuklar= kompyuter[:]
noutbuklar.remove('fujitsu')
del(noutbuklar[0:3])
noutbuklar.append('samsung')
noutbuklar.insert(2,'apple')
print(kompyuter,"\n")
print(noutbuklar)
#tugri kopiya qilish uchun [:] foydalanamiz


#uzgarmas listlar tuples()
toys = ('moshincha','dendi','ayiqcha','qugirchok','quyoncha')
print(toys)
print(toys[-1])
print(toys[1:3])
print(toys)
toys = list(toys)
print(type(toys))
toys.append('traktor')
toys = tuple(toys)
print(type(toys))
print(toys)





