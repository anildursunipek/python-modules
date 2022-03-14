import os
import datetime
#Os Modülü Nedir?
"""
---İşletim sistemleri hakkında bilgiler, klasör işlemleri, dosya işlemleri os modülü ile yapılabilir
---
"""


result = os.name#Hangi işletim sistemi kullandığımızı çıktı olarak veriri
result = os.getcwd()#Dosya hakkında bilgi verir.Bulunduğu konumu çıktı olarak yazdırır -- Etkin dizini gösterme
#os.mkdir("yenidosya")#Aynı dizin altında yeni dosya oluşturur
#os.chdir()#Change the current working directory to the specified path. --Dizin değiştirme
result = os.listdir()
result = os.listdir('C:\\')
result = os.stat("basic_module.py")#Parametreye girilen dosya hakkında bilgileri verir --Boyut --Değiştirme tarihi -- Açma tarihi...
print(datetime.datetime.fromtimestamp(result.st_atime))#Son erişim tarihi
print(datetime.datetime.fromtimestamp(result.st_ctime))#Oluşturma tarihi
print(datetime.datetime.fromtimestamp(result.st_mtime))#Değiştirme tarihi
"""
Klasor Adı değiştirme
os.rename("klasör adı","yeni isim")
"""
"""
os.rmdir()
os.rmdirs()
--Belirtilen dosya içeriklerini veya dosyaları siler
"""
yol = os.path.abspath("basic_module.py")#Dosyanın tam konumunu çıktı olarak verir
yol = os.path.dirname('C:/Users/fb-du\Desktop\python\module/basic_module.py')#Dosya yolu girilen dosyanın dizin ismini verir
result = os.path.dirname(os.path.abspath('basic_module.py'))
result = os.path.exists('C:/Users/fb-du\Desktop\python\module/basic_module.py')#Dosya var mı yok mu ?
result = os.path.isdir('C:/Users/fb-du\Desktop\python\module/basic_module.py')#Dosya mı?
result = os.path.isfile('C:/Users/fb-du\Desktop\python\module/basic_module.py')


print(yol)
print(result)