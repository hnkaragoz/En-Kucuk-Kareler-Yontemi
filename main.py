
# Gerekli Kütüphaneleri Ekle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)

#Veriyi Oku
data = pd.read_csv('./datasets/covid-data2.csv')
print(data.shape)
data.head()

#X ve Y değerlerini toplama
X = data['Sira Sayisi'].values
Y = data['Hasta Sayisi'].values

# Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

#Toplam Değer Sayısı
n = len(X)

# m ve c'yi hesaplamak için formül
numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
    m = numer / denom
    c = mean_y - (m * mean_x)

#Katsayıları yazdır
print(m, c)
#Çizim Değerleri ve Regresyon Çizgisi
max_x = np.max(X) + 100
min_x = np.min(X) - 100

# x ve y değerleini hesapla
x = np.linspace(min_x, max_x, 1000)
y = c + m * x

#Regrasyon Çizgisi
plt.plot(x, y, color='#52b920', label='Regresyon Çizgisi')
#Dağılım Noktaları
plt.scatter(X, Y, c='#ef4423', label='Dağılım Noktaları')

plt.xlabel('Sira Sayisi')
plt.ylabel('Hasta Sayisi')
plt.legend()
plt.show()