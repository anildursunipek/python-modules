import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1,numbers2)

result = numbers1 + numbers2#İki dizi arasındaki indisi aynı olan elemanları toplar
result = numbers1 + 10#Dizinin tüm indislerine 10 ekler

result = np.sin(numbers1)#Dizi içerisindeki tüm elemanların sinüsünü alır
result = np.sqrt(numbers1)#Dizideki tüm elemanların karakökünü alır
result = np.log(numbers1)

multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)
print(multi_numbers1)
print(multi_numbers2)


result = np.vstack((multi_numbers1,multi_numbers2))#2 Diziyi dikey bir şekilde birleştirir
result2 = np.hstack((multi_numbers1,multi_numbers2))#2 Diziyi yatay bir şekilde birleştirir

print(result)
print(result2)
"""
---> Vertical
[[54 35 90]     --->Denklem sayısı artar
 [52 18 92]
 [20 85 75]
 [58 59 86]]
---> Horizonal
[[54 35 90 20 85 75] --->Bilinmeyen sayısı artar
 [52 18 92 58 59 86]]
"""

test = np.arange(10,100,6)

yazdir = numbers1 >= 5#Sayıları kontrol eder 5'e göre bool türünde değer döndürür ---> Bu işlem % // gibi işlemler ile de yapılabilir
print(yazdir[1])
print(yazdir)