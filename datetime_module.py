"""
from datetime import datetime
from datetime import time
from datetime imprt date
"""
from datetime import *
#print(dir(datetime))

result = datetime.now()#Today ile aynı işev >>> datetime().today
#result = 2022-02-15 13:33:37.394386 // Sonuç olarak yıl ay gün saat dakika saniye şeklinde çıktı verir
result = datetime.now().year
print(result)
result = datetime.now().month
print(result)
result = datetime.now().day
print(result)
result = datetime.now().hour
print(result)
result = datetime.now().minute
print(result)
result = datetime.now().second
print(result)
result = datetime.now()
print(datetime.now().date())
print(datetime.ctime(datetime.now()))#Daha detaylı bir şekilde tarihi yazdırır
print(datetime.strftime(datetime.now(),'%Y'))
print(datetime.strftime(datetime.now(),'%X'))

t = '11 August 1999 10:12:30'
dt = datetime.strptime(t, '%d %B %Y %H:%M:%S')#Yazdığımız string ifadedeki tarihi kendi çözümledi
print(dt)
print(dt.year)
birthday = datetime(1999,8,11,10,30,10)
print(birthday)
new = result + timedelta(days=10)
print(new)