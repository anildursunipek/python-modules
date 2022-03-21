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
import numpy as np
numbers = [20,30,40,50]

#pandas_series = pd.Series(numbers)
#type olarak series çıktısı verir
#Tek boyutlu liste tanımlaması yapılır
pandas_series = pd.Series(numbers, [1,2,3,4])

#2.parametre olarak dizi uzunluğu olarak indis bilgisi girebiliriz.
#Örneğin 4 dizi elemanına 4 adet sayı atandı ve çıktı olarak verildi
dict = {'a':10,'b':20,'c':30,'d':40}
pandas_dict = pd.Series(dict)
print(pandas_dict)
#Bu şekilde sözlük olarak seri oluşturursak key value bilgilerine göre seriyi oluşturur
result = pandas_dict['a':'c']
result = pandas_dict.ndim#Kaç boyutlu ?
result = pandas_dict.shape#Kaça kaçlık bir dizi
result = pandas_dict.max()
result = pandas_dict.sum()
result = pandas_dict %2 == 0

#print(pandas_series)
#print(pandas_dict)
#print(result)

"""
df = pd.DataFrame(np.random.randn(5,5), index=["a","b","c","d","e"], columns=["Column1","Column2","Column3","Column4","Column5"])

result = df["Column1"]#Selected first column
# Add new column
df['Column6'] = pd.Series(np.random.randn(5),index=["a","b","c","d","e"])
result = df
df["Column7"] = df['Column1'] + df['Column2']
print(result)
"""

# Data Filter
data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])
"""
print(df)
print(df.columns)#Kolon isimlerini çıktı olarak aktarır
print(df.head(5))#İlk 5 satırı çıktı verir
print(df.tail(5))#Son 5 satırı çıktı verir
print(df["Column1"].head(6))#Secilen kolondan ilk 6 kayıt
print(df[["Column1","Column2"]])#Birden fazla kolon seçimi
print(df[5:15]["Column4"].head(3))
"""
result = df>50#True False geri döndürür
result = df[df>50]#Büyük olanlar gösterilir, olmayanalar nan gösterir
result = df[(df["Column2"]>30) & (df["Column3"]>50)]
result = df.query("Column2 > 30 & Column3 > 50")#Koşul ile sorgu yapma işlemleri query ile yapılır

# Dataframe Grupby

result = df['Column1'].sum()#Secilen kolonu toplar
result = df.groupby(['Column1']).groups#Gruplandırma
result = df.groupby(['Column2']).mean()
result = df.groupby('Column2').max()


print(result)
