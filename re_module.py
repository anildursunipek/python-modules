import re
"""
Re Modülü Nedir?
--Regular Expression
"""
#Re Module
str = "Python Kursu: Python Programlama Rehberinzi | 40 saat saa"
str2 = "Python Kursu: Python Programlama Rehberinzi | 40 saat saat saaat saaaat saaaaaaaat bbb bbbbbbb"
#re.findall() metodu

result = re.findall("Python",str)# Yazılan kelimeyi belirtilen string ifade içerisinden arar ve dizi şeklinde yazdırır
print(len(result))

#re.split
result = re.split(" ",str)# Belirtilen ilk parametreye göre string ifadeyi böler ve dizi içerisine aktarır

#re.sub
result = re.sub(" ","-",str)#Bu metodda ilk parametre ile 2. parametre arasında değiştirme işlemi yapılır
#Örnekte boşluk yerine '-' koyularak tekrardan yazdırma işlemi yapıldı. Yer değiştirme metodudur

#re.search()
result = re.search('Python',str)#Yazılan parametreyi bulur ve onun ile ilgili bilgi aktarır
print(result.pos)
print(result.end())
print(result.start())
# REGULAR EXPRESSİON ÇALIŞMALARI

result = re.findall("[a-e]",str)#Köşeli parantez içerisine girilen karakterler hakkında arama yapar.
# Eğer köşeli parantez içerisine [harf-harf],[sayi-sayi] ifadeleri koyulursa o 2 ifade arasında arama yapar

result = re.findall("[^abc]",str)# ^ işareti koyulrusa oondan sonraki gelenler dışındaki bütün ifadeleri dizi içerisinde çıktı verir

result = re.findall(".....",str)# Nokta sayısı kadar dizi içerisine her bir elemanı aktarır.
result = re.findall("Py..on",str)# Bu örnekte y ile o arasında 2 harf var ise dizi içerisine alır
#Örnek Çıktı: ['Pytho', 'n Kur', 'su: P', 'ython', ' Prog', 'ramla', 'ma Re', 'hberi', 'nzi |', ' 40 s']

result = re.findall("^P",str)#Bu şekilde arama yaparsak ^ ifadesinden sonra gelen string ifade başlayan bir string var mı ?

result = re.findall("saat$",str)# Dolar işaretinden önce gelen string ifade ile biten bir string var mı?

result = re.findall("sa*t",str2)# Bir karakterin sıfır yada daha fazla olmasını kontrol eder

result = re.findall("sa+t",str2)# Bir karakterin bir veya daha fazla olmasını kontrol eder

result = re.findall("sa?t",str2)# Bir karakterin sıfır yada bir olmasını kontrol eder

result = re.findall("a{5}",str2)#a karakterinin 5 defa tekrarlananlarını çıktı olarak diziye aktarır
result = re.findall("a{2,5}",str2)#a karakterinin 2 veya 5 defa tekrarlananlarını çıktı olarak diziye aktarır
result = re.findall("[a-b]{2,5}",str2)#a ve c arasındaki karakterinin 2 veya 5 defa tekrarlananlarını çıktı olarak diziye aktarır

result = re.findall("a|b",str)#String içerisinde bulunan a yada b'leri dizi içerisine aktarır


result = re.findall("(a|b|c)er",str)#a veya b veya c karakterlerinden sonra er string ifadesi bulunanları diziye aktarır
# Bu aramada gruplandırma için paranter kullanılmıştır. Sayılarda çarpma yaparken kullandığımız gibi



print(result)