names=['Shaxboz','Dilmurod','Abubakr','Shaxriyor']
print(names)
print(names[0] ,'Rossiyada')
print(names[1],'Qishloqda')
print(names[2],'Xizmatda')
print(names[3],'Khujandda')

sonlar =[23,-7,5.0,12.128,7]
print(sonlar)
sonlar[1]= 60
sonlar[3]= 50
print( sonlar[2] + sonlar[3])
print( sonlar[0] - sonlar[1])
print( sonlar[3] / sonlar[1])
print( sonlar[1] * sonlar[4])

print(sonlar)



t_shahslar=['Amur Temur','Alisher Navoiy','A. Jomiy']
z_shahslar =['Bill Gates','Ilon Musk','Stiv Jobs']
print(t_shahslar, "\t" ,z_shahslar,"\n")

print("Men tarixiy shahslardan", t_shahslar.pop(0),"bilan, \n Zamonaviy shahslardan",z_shahslar.pop(1) ,"bilan \n suhbat qurishni hohlar edim ")

friends=[]
friends.append('Sherali')
friends.append('Mirzo')
friends.append('Yusuf')
friends.append('Begzod')
friends.append('Begali')
friends.append('Islomjon')
print(friends)

friends.remove('Sherali')
friends.remove('Begali')
print(friends)

friends.insert(0,'Muhammadali')
friends.insert(3,'Sherzod')
friends.insert(2,'Javohir')
friends.insert(7,'Shuhrat')

print(friends)




New_mehmons =[]
print("Hozzircha mehmonga kelganlar",New_mehmons,"\n")
print(friends)
friends.pop(2)
friends.pop(0)
friends.pop(4)
print(friends)


New_mehmons.append('Muhammadali')
New_mehmons.append('Javohir')
New_mehmons.append('Islomjon')

print("Mehmonga Kelgan dustlaringiz", New_mehmons)