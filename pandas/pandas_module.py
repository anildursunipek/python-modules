"""Pandas Nedir?"""
"""
-->Veri analizi kütüphanesedir
-->Numpy ile birlikte kullanılabilir
-->Numpy daha çok sayılar, matematiksel işlemler üzerinde kullanılmaktadır
-->Pandas ise datalar üzerine işlemler yapılırken kullanılır
-->Farklı dosya türlerinden gelen bilgileri pandas kullanarak veri olarak kullanabiliyoruz
-->Bozuk verileri belli formatlara sokabiliriz
-->Veriler üzerinde ortalama , max , min , silme , ekleme gibi işlemler de yapılabilir
-->Kısacası datayı istediğimiz gibi şekillendirebiliyoruz
-->Dataframe'ler (df) serilerin birleşmiş halleridir
"""
import pandas as pd
numbers = [20,30,40,50,]

#pandas_series = pd.Series(numbers)
#type olarak series çıktısı verir
#Tek boyutlu liste tanımlaması yapılır
pandas_series = pd.Series(numbers, [1,2,3,4])

#2.parametre olarak dizi uzunluğu olarak indis bilgisi girebiliriz.
#Örneğin 4 dizi elemanına 4 adet sayı atandı ve çıktı olarak verildi
dict = {'a':10,'b':20,'c':30,'d':40}
pandas_dict = pd.Series(dict)
#Bu şekilde sözlük olarak seri oluşturursak key value bilgilerine göre seriyi oluşturur
result = pandas_dict['a':'c']
result = pandas_dict.ndim#Kaç boyutlu ?
result = pandas_dict.shape#Kaça kaçlık bir dizi
result = pandas_dict.max()
result = pandas_dict.sum()
result = pandas_dict %2 == 0



print(pandas_series)
print(pandas_dict)
print(result)