country = ['tojikiston','uzbekiston','angliya','rossiya','malayziya','saudia','falastin','qatar']
print(country)
print(len(country))
print(sorted(country))
print(sorted(country,reverse=True,))
print(country,"\n")
country.reverse()
print(country,"\n")
country.sort()
print(country,"\n")
country.sort(reverse=True)
print(country,"\n")

juft_sonlar = list(range(120,1200,2))
print(juft_sonlar,"\n")
print(sum(juft_sonlar))
print(max(juft_sonlar) - min(juft_sonlar))
print(len(juft_sonlar))
print(juft_sonlar[0:20])
print(juft_sonlar[270:290])
print(juft_sonlar[290:310])
taomlar = ['palov','somsa','mantu','shahlik','shurbo','qurutob']
nonushta = taomlar[:]
nonushta.remove('palov')
del(nonushta[0:3])
nonushta.append('qaymoq')
nonushta.append('kofe')
nonushta.append('sut')
print(taomlar ,"\n")
print(nonushta)
nonushta= tuple(nonushta)
print(type(nonushta))


