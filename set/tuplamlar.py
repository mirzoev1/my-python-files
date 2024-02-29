# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 09:53:01 2024

@author: shukurullo
"""
shumora ={1,2,3,4,5,6}
print(shumora)

nom = {'ali','vali''gani','karim'}
print(nom)

number =[1, 1, 2, 2, 3, 3,4,5,6,7,8,1,2,3,4,5,6,7,8,9]
print("bu ruyxat tartibsiz")
print(f"{number}\n")


sonlar = set(number)
print("bu ruyxat  set() funksiyasi yordamida  tartiblandi")
print(sonlar)

print("yana ruyxat shakliga qaytarildi\n")
number = list(sonlar)
print(number)

#to'plamga element qushish
mevalar ={'anor'}

mevalar.add('banan')
print(mevalar)
mevalar.update(['olma','uzum','banan','anor','olma','shaftoli'])
print(mevalar)

#to'plamdan elementlarni o'chrish

mevalar.discard('olma')
print(mevalar)

mevalar.remove("uzum")
print(mevalar)

#diskart metodi ruyxatda bulmasa xatolik bermaydi
shumora.discard(7)
print(shumora)
#remove xatolik kelib chiqaradi
#shumora.remove(7)
#print(shumora)

#tuplamdan element sugurip olish pop()
son =shumora.pop()
print(son)
print(shumora, "\n\n")


#tuplamlar ustida amallar bajarish
#ikki tuplamni birlashtirish
A = {1,2,3,4}
B = {3,4,5,6,7}
C = A|B
print(C)
#UNION bilan VA | bir vazifani bajaradi
D = A.union(B)
print(D)

#ikki tuplamning kesishmasini topish
X = {99,98,97,96,95,94}
Y = {93,92,91,90}
Z = Y|X
print(Z)
print(A&B)
print(B.intersection(A))


#ikkala tuplam orasidagi fArqni topish
print(A-B)
print(B.difference(A))

#tuplamlardan symmetrik farqni topish ^
print(A^B)
print(A.symmetric_difference(B))