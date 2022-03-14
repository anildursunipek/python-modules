import numpy as np

result = np.arange(1,10)#1 den 10 a kadar bir dizi oluşturduk      arange(başlangıç,bitiş,atlamasayısı)

result = np.zeros(10)#Sıfırlardan oluşan bir dizi
result = np.ones(10)#Birlerden oluşan bir dizi

result = np.linspace(0,100,5)#0 dan 100 e kadar belirlenen aralıklarda böler
result = np.random.randint(0,10,5)#1 ile 10 arasında 5 adet sayı üretilir ve dizi oluşturulur
result = np.random.rand(3)#Random 3 adet float sayı üretir

np_array = np.arange(0,50)
np_array = np_array.reshape(5,10)


print(result)
print(np_array)
print(np_array.sum(axis=0))#Satırların toplamı
print(np_array.sum(axis=1))#Sütunların toplamı
print(np_array.max())
print(np_array.min())
print(np_array.mean())
print(np_array.argmin())#En küçük sayının kaçıncı indiste olduğunu gösterir