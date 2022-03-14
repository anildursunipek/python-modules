import numpy as np
"""
---> Büyük veriler ile çalışırken çok daha az yer kapladığı için numpy ile çalışılıyor.

"""
#Numpy array

np_array = np.array([1,2,3,4,5,6,7,8,9])#tek boyutlu bir dizi oluşturuldu
print(type(np_array))
print(np_array)

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)#Çok boyutlu bir dizi oluşturmamızı sağlar. reshape metodu ile 3'e 3'lük bir dizi oluşturduk
print(np_multi)
print(np_array.ndim)
print(np_multi.ndim)#Kaç boyutlu olduğu çıktı olarak verildi

print(np_array.shape)
print(np_multi.shape)#Kaça kaçlık bir dizi olduğunu çıktı olarak verdi