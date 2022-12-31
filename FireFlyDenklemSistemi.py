# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 13:35:01 2022

@author: ARMAN
"""

import random
import math

def firefly_algorithm(popsize, iter, gama):
    # Degiskenleri sıfırlama.....
    pop = [0.0] * 100
    f = [0.0] * 100

    if popsize > 100:
        popsize = 100

    sayac = 0
    minfx = 1000000.0
    random.seed()

    # Rasgele populasyon üretme...
    for x in range(popsize):
        pop[x] = 0.001 * (random.randint(0, 1572))  # Aralık içinde rasgele d üretimi...
        f[x] = abs(3 * math.cos(pop[x]) - pop[x]**2 - 1)  # Hedef fonksiyonlarının hesaplanması....

    # Eşleşme.......
    eslesme = popsize * (popsize - 1) / 2.0

    while sayac < iter:
        for x in range(int(eslesme)):
            a = random.randint(0, popsize - 1)
            b = random.randint(0, popsize - 1)
            d = abs(pop[a] - pop[b])
            alpha = 0.001 * (random.randint(0, 1001))
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
    print(f"Maximum hedef fonksiyonu = {minfx:.4f}")


    # Sonuçların dosyaya yazılması.....
    with open("ates_bocegi_sonuclar.txt", "w") as g:
        g.write(f"Optimum x = {xmin:.4f}\n")
        g.write(f"Maximum hedef fonksiyonu = {minfx:.4f}\n")
    print("Firefly algorithm completed")

firefly_algorithm(10, 100, 0.9)

