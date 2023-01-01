# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 13:35:01 2022

@author: ARMAN
"""
'''
y=x^2+1 ve y=3cos(x) denklem sistemlerinin çözüm kümesini
Ateş Böceği Algoritması kullanarak ile bulunuz
Başlangıç rasgele aralığını [0,pi/2] alınız.
Çözüm: H.F =|3cos(x)-x^2-1| sıfır yapan x değeri araştırılmalı
'''
'''
Bu kod parçacığında, NumPy ve Matplotlib kütüphanelerini kullanarak iki farklı çizgi oluşturulur.
İlk çizgi, $x^2+1$ ifadesiyle oluşturulur ve kırmızı renkte gösterilir. 
İkinci çizgi ise, $3\cos{x}$ ifadesiyle oluşturulur ve mavi renkte gösterilir. 
Bu iki çizgi grafiğin üzerine çizilir ve kılavuz çizgiler gösterilir. Son olarak, grafik gösterilir.
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1.571, 0.001)
y1 = x**2 + 1
plt.plot(x, y1, 'r')
plt.grid(True)
y2 = 3 * np.cos(x)
plt.plot(x, y2, 'b')
plt.show()

import random
import math

def firefly_algorithm(popsize, iter, gama):
    # Degiskenleri sıfırlama.....
    pop = [0.0] * 100
    f = [0.0] * 100

    if popsize > 100:
        popsize = 100

    sayac = 0
    minfx = 1000000.0 # Problemi minimize edeceğimiz için max bir değer atıyorum.
    random.seed()

    # Rasgele populasyon üretme...
    for x in range(popsize):
        pop[x] = random.uniform(0, math.pi/2)  # Aralık içinde rasgele d üretimi... [0,pi/2]
        f[x] = abs(3 * math.cos(pop[x]) - pop[x]**2 - 1)  # Hedef fonksiyonlarının hesaplanması....

    # Eşleşme.......
    eslesme = popsize * (popsize - 1) / 2.0 # n(n-1)/2

    while sayac < iter:
        for x in range(int(eslesme)):
            a = random.randint(0, popsize - 1)
            b = random.randint(0, popsize - 1)
            d = abs(pop[a] - pop[b])
            alpha = random.uniform(0, 1)
            beta = (0.9) * math.exp((-1.0) * gama * d**2)

            if f[a] < f[b]:
                s = 0.001 * (random.randint(0, 1000))
                pop[b] = (1 - beta) * pop[b] + beta * pop[a] + alpha * (s - 0.5)
            else:
                s = 0.001 * (random.randint(0, 1000))
                pop[a] = (1 - beta) * pop[a] + beta * pop[b] + alpha * (s - 0.5)

        # Hedef Fonksiyonlarının Güncellenmesi.....
        for x in range(popsize):
            f[x] = abs(3 * math.cos(pop[x]) - pop[x]**2 - 1)  # Hedef fonksiyonlarının hesaplanması....

        # En büyük hedef fonksiyon hesabı.....
        for x in range(popsize):
            if f[x] < minfx:
                minfx = f[x]
                xmin = pop[x]

        sayac += 1
        
    print(f"Optimum x = {xmin:.4f}")
    print(f"Minimum hedef fonksiyonu = {minfx:.4f}")


    # Sonuçların dosyaya yazılması.....
    with open("ates_bocegi_sonuclar.txt", "w") as g:
        g.write(f"Optimum x = {xmin:.4f}\n")
        g.write(f"Minimum hedef fonksiyonu = {minfx:.4f}\n")
    print("Firefly algorithm completed")

firefly_algorithm(10, 100, 0.9)

