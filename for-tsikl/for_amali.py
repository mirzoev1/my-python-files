ismlar =['Sodiq','Ravshan','Behruz','Ulugbek','Bobur']
for ism in ismlar:
    print(f"Assalomu alaykum {ism} siz mening dustim ekaningizdan fahrlanaman".title())
print(f"kod {len(ismlar)} marta takrorlandi  ") 

sonlar = list(range(11,100,2))
for son in sonlar:
    print(f"{son} ning kubi {son **3} ga teng ")

kinolar =[]
print("5 ta sevimli kinongiz nomi")
for k in range(5):
  kinolar.append(input(f" {k+1}   kino  nomi nima:"))
print(kinolar)

n_people = int(input('Bugun nechta inson bilan kurishdingiz'))
k_people =[]
for k in range(n_people):
   k_people.append(input(f"{k+1}-suhbat qilgan odamingiz kim edi: "))
print(k_people)