import random

#help(random)

randomNumber = random.random() #0 ile 1 arasında bir sayı üretilir
randomNumber = random.uniform(1,100) # 1 ile 100 arasında bir sayı üretir,ondalıklıdır
randomNumber = random.randint(1,100) # 1 ile 100 arasında tam bir sayı üretir
print(randomNumber)

names = ['Dursun','Gamze','Hatice','Şaban','Efe','Ahmet']

result = names[random.randint(0,len(names)-1)]
result2 = names[random.randint(0,len(names)-1)]
result3 = names[random.randint(0,len(names)-1)]
secme = random.choice(names)#Bu metod dizi üzerinden rastgele bir seçim yapar
print(result,result2,result3)
print(secme)
random.shuffle(names)#Bu metod liste içindeki elemanların yerlerini rastgele bir şekilde değiştirir
print(names)

ornek = random.sample(names,2)#Bu metod rastgele istenen sayıda örnek seçer
print(ornek)