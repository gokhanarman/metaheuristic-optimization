# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 14:31:56 2023

@author: ARMAN
"""

'''
f(x)=sin(√x) - x  fonksiyonunun kök değerini ATEŞ BÖCEĞİ algoritmasını kullanarak bulunuz. 
Kök değerini [0.5, 3] aralığında araştırınız. 
Popülasyon sayısı=15 ve iterasyon sayısı=40 olarak belirleyiniz.
'''
import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return math.sin(math.sqrt(x)) - x
f2 = np.vectorize(f)
x = np.arange(0, 3, 0.001)
plt.plot(x, f2(x))
plt.grid(True)
plt.show()

import random

# function to optimize: y = sin(√x) - x
def target_function(x):
    return math.sin(x**(1/2)) - x

# firefly algorithm
def firefly_algorithm(popsize, iter, gama):
    # initialize variables
    pop = [0 for _ in range(100)]
    f = [0 for _ in range(100)]
    
    best_solution = 1000000 # It will be increase then i choose minus number
    
    

    # generate random initial population
    for i in range(popsize):
        pop[i] = random.uniform(0.5, 3)  # random d within range [0.5, 3] x values
        f[i] = target_function(pop[i])  # calculate target function f(x) values
        print("x :{} and f(x): {}".format(pop[i], f[i]))

    # mating
    eslesme = popsize * (popsize - 1) / 2.0     # n(n-1)/2 
    
    for _ in range(iter):
        for _ in range(int(eslesme)):
            a = random.randint(0, popsize - 1)
            b = random.randint(0, popsize - 1)
            d = abs(pop[a] - pop[b]) # distance for each fireflies
            alpha = random.uniform(0, 1) # [0,1] range
            # beta hızlı veya yavaş yakınsama için kullanılır.
            # 0.9 alınırsa hızlı yakınsar 0.99 alınırsa yavaş yakınsar
            beta = (0.9) * math.exp((-1.0) * gama * d * d) # Cekicilik Beta(r) = Beta(0)*(e^(-gama*r^2))
            
            # Fitness functionda büyük yanan firefly küçük yananı kendisine doğru çeker.
            if f[a] > f[b]:
                # b-th firefly is drawn towards the a-th firefly.
                s = random.uniform(0, 1) # [0,1] range random number
                
                # Xi = Xi + (Beta(0)*(e^-gama*r^2)*(Xj - Xi)) + (alpha*(random - 0.5))
                # Xi = Xi + (Beta(r) * (Xj - Xi)) + (alpha*(random - 0.5))
                # Xi = Xi - Beta(r) * Xi + Beta(r) * Xj + (alpha*(random - 0.5))              
                pop[b] = pop[b] - (beta * pop[b]) + (beta * pop[a]) + alpha * (s - 0.5) 
                # print("pop[b]",pop[b])
            else:
                # a-th firefly is drawn towards the b-th firefly.
                s = random.uniform(0, 1) # [0,1] range random number
                # Xi = Xi - Beta(r) * Xi + Beta(r) * Xj + (alpha*(random - 0.5))  
                pop[a] = (1 - beta) * pop[a] + beta * pop[b] + alpha * (s - 0.5)
                # print("pop[a]",pop[a])

        # update target functions
        for i in range(popsize):
            f[i] = target_function(pop[i])

        # find maximum target function
        for i in range(popsize):
            if f[i] < best_solution:
                best_solution = f[i]
                best_solution_x = pop[i]
                
    # print(f"Optimum x = {xmax:.4f}")
    # print(f"Minimum hedef fonksiyonu = {maxfx:.4f}")

    # write results to file
    with open("ates_bocegi_sonuclar.txt", "w") as fp:
        fp.write("Optimum x=%4.4f \n" % best_solution_x)
        fp.write("Maximum target function=%4.4f \n" % best_solution)
    print("Firefly algorithm completed")
    
    return print(best_solution_x, best_solution)

# test firefly algorithm
firefly_algorithm(popsize= 5, iter= 5, gama = 0.9)


