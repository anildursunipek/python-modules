import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,2,100)
plt.plot(x,x,color='yellow',label='Linear')#Label lejant üzerindeki isimleri
plt.plot(x,x**2,color='red',label='quadratic')
plt.plot(x,x**3,color='green',label='cubic')
#3 grafik çizimini aynı taplo üzerinden gösteriyoruz

plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel("X'in Karesi")

plt.legend()#Lejantın gösterilmesini sağlar

plt.show()