import pandas as pd
"""
s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples= s1 , oranges= s2)
#Sözlük yapısına çevrilerek apples ve oranges kolon ismi olarak kayıt edilir
#Diğer sayılar value olarak indislere atanır
print(data)
df = pd.DataFrame(data)
#pd.DataFrame komutu ile tablo yapısı oluşturulur
print(df)
"""

list = [['İphone 7',2017,5000],['İphone 8',2018,6000],['İphone 9',2019,7000]]
#Data frame içerisine ilk parametreye eklenen her tuple,liste,dizi dataya 1 satır ekler
#Data içerisindeki dizi elemanları ise dataya birer sütun ekler
df = pd.DataFrame(list, columns=['Sütun-1','Sütun-2','Sütun-3'],index=['m1','m2','m3'])
print(df)
#ALTERNATİVE 2 şekilde gösterebilriiz 1- Normal liste içinde 2-Sözlük şeklinde yazarak

dict = {'Phone Name':['İphone 7','İphone 8','İphone 9'],'Release Year':[2017,2018,2019],'Price':[5000,6000,7000]}

dict_df = pd.DataFrame(dict,index=[1,2,3])
print(dict_df)
"""
dict_list = [
                {SATIR 1}#Key Value değerleri vardır. Her key(value) bir sütuna denk gelir
                {SATIR 2}
                {SATIR 3}
                {SATIR 4}
                {SATIR 5}
                ]
"""