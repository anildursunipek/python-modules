import matplotlib.pyplot as plt
import numpy as np

np_array = np.array([1,2,3,4,5,6,7])
np_array2 = np.array([1,4,9,16,25,36,49])

plt.plot(np_array,np_array2,color='yellow',linewidth='2')#Basit bir grafik çizme metodudur
#Verilen ilk parametre x eksenine , 2.parametre y eksenine yazdırılarak grafik çizilir
#https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.plot.html
#Hazır plot style üstteki linkten erişilebilir
plt.axis([0,10,0,100])#Oluşturulan grafiğin x ve y eksenlerindeki sınırlarını belirlememizi sağlar
#İlk 2 değer x başlangıç bitiş , son 2 değer y başlangıç bitiş

plt.title("GRAFİK BASLIGI",color='red')
plt.xlabel("X LABEL")
plt.ylabel("Y LABEL")

plt.show()