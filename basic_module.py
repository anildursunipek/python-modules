#Projeler modüller halinde parça parça oluşturulur.
#Modüller arasında bir ilişki olmaktadır. Başka bir modülün elemanı kullanılabilir.(Örn:sınıflar,fonksiyonlar...)
#Modülleri kendimiz oluşturabiliriz yada hazır modül kullanabiliriz.
"""YÖNTEM 1"""
#import math #math modülünü dahil ettik
#import math as mat ---> olarak yazsaydık math modülünü mat kısaltması ile çağırabilirdik.
"""
value = dir(math)
value2 = help(math.factorial)
"""
#fakt = math.factorial(5)
#print(fakt)

"""YÖNTEM 2"""
from math import factorial,sqrt # Bu şekilde yazılırsa fonksiyonlar direkt olarak çağırılabilir
#Kısaca math kütüphanesinden factorial ve sqrt fonksiyonlarını kütüphanemize ekledik


value = sqrt(5)
faktor = factorial(3)
print(value)
print(faktor)