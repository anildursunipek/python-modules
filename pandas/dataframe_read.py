import pandas as pd
"""
        Farklı Uzantılardaki Dosyaları DataFrame'ye aktarma
df = pd.read_csv('marvel_clean.csv')

json için pd.read_json('Dosya uzantısı')
excel için pd.read_excel('Dosya Uzantısı')

print(df)
"""
df = pd.read_csv('marvel_clean.csv')

result = df['Title']#Kolon seçimi
result = df[['Title','Worldwide']]#Birden fazla sütun gösterimi
result = df.loc[60]#60. İndexteki tüm kolonları result içine aktarır
"""
loc["row","column"]
loc yerine iloc kullanılırsa index isimleri farklı olsa bile sayı baz alınarak indexleme yapıyormuş gibi davranır ve ilk index 0 olarak alınır
"""

result = df.loc[60,'Title']#60. satır Title sütununu aktarır
result = df.loc[:,'Title']#Tüm satırlardaki title kolonunu aktarır
result = df.loc[60,'Title':'Worldwide']#Kolonlar için de aralık belirtilebilir

#df.drop('Title',axis= 1,inplace=True)
#drop data üzerindeki belirtilen kolonu çıkarmamızı sağlar
#axis 1 dikey olduğunu belirtmekte
#inplace True olursa kalıcı olarak siler False olursa geçici olarak silmiş olur
print(result)
print(df)
