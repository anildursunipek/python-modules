import json
import requests

result = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=77693259ba14b65f1c0f1779bae15e4e&format=1")
print(result)
#print(result.text)
result = json.loads(result.text)
print(result['rates'])
while True:
    try:
        alınan_doviz = input('Almak istediğiniz para türünü giriniz: ')
        miktar = int(input(f"Ne kadar EUR bozmak istersiniz: "))
        print(f"Güncel {alınan_doviz} kuru: {result['rates'][alınan_doviz]}")
        print(f"{miktar} EUR bozdunuz.")
        print(f"{miktar * result['rates'][alınan_doviz]} {alınan_doviz} aldınız.")
        break
    except:
        print('Yanlış para türü girdiniz.Lütfen para türünü büyük harfler ile giriniz')