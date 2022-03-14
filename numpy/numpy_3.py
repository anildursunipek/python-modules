import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers
"""
print(result[5])#Dizi içerisindeki 5. indisi çıktı olarak verir
print(result[0:3])
print(result[::2])
print(result[3:])
print(result[::-1])#Listeyi ters çeviririz
"""

numbers2 = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(numbers2[1][1])
print(numbers2[1,1])#İkiside çıktı olarak aynı sonucu vermektedir

print(numbers2[:,0])#Tüm satırlardaki 0.indisi çıktı olarak verir
print(numbers2[:,1])
print(numbers2[:,0:2])



arr1 = np.arange(0,10)
"""
arr2 = arr1
arr2[0] = 10000
print(arr1)
print(arr2)#Referans objesi olduğu için 2 dizide de değişiklik olacaktır
print(type(arr1))"""
"""
--> Referans değil de farklı adresler olması istendiğinde .copy metodu kullanılmaldır
"""
arr2 = arr1.copy()
arr2[0] = 10000
print(arr1)
print(arr2)#Referans objesi olduğu için 2 dizide de değişiklik olacaktır
print(type(arr1))

