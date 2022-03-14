import requests
import json
"""
--->Bir internet sitesini ziyaret ettiğimizde kaynak kodlara ulaşmamızı sağlayan kütüphanedir.
"""

result = requests.get("https://jsonplaceholder.typicode.com/todos")
#print(result)#Result içerisine site bir cevap göndericek
#cevap : <Response [200]>
#Başarılı olduğu anlamına gelmektedir.
result = json.loads(result.text)#json modülü ile string bilgiyi liste ifadesine çevirdik
for i in result:
    print(i)
print(type(result))
#print(result[0]['userId'])
