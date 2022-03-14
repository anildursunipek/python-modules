import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,2,100)


fig,axs = plt.subplots(3)
#subplots(kaç adet grafik birleştirilecek) metodu grafiklerin aynı çerçeve içerisinde görüntülenmesini sağlar
#subplots ile sadece alt alta grafik oluşturmayız. aynı zamanda eksenler şeklinde 4 bir yana da grafik oluşturabiliriz
#örneğin plt.subplots(2,2) şeklinde girersek kodu 2 alt üst 2 sağ sol olacak şekilde grafikler yerleşir
#fig.suptitle('GRAFİK BAĞLIĞI') ile de ana grafiğin başlığını belirleyebiliriz
axs[0].plot(x,x,color='red')
axs[0].set_title('Linear')#Belirlenen axs grafiğine başlık ekler

axs[1].plot(x,x**2,color='yellow')
axs[1].set_title('quadratic')
axs[2].plot(x,x**3,color='green')
axs[2].set_title('cubic')

plt.tight_layout()#Grafik görünümünü değiştirir
plt.show()

