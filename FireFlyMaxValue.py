# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 13:16:32 2022

@author: ARMAN
"""

import random
import math

# function to optimize: y = -x^2 + 10x - 24
def target_function(x):
    return -x**2 + 10*x - 24

# firefly algorithm
def firefly_algorithm(popsize, iter, gama):
    # initialize variables
    pop = [0.0 for _ in range(popsize)]
    f = [0.0 for _ in range(popsize)]    
    maxfx = -1000000.0 # It will be increase then i choose minus number    
    xmax = 0.0 

    # generate random initial population
    for i in range(popsize):
        pop[i] = random.uniform(0, 10)  # random d within range [0,10] x values
        
        f[i] = target_function(pop[i])  # calculate target function f(x) values

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
                pop[b] = pop[b] - (beta * pop[b]) + (beta * pop[a]) + alpha * (s- 0.5) 
            else:
                # a-th firefly is drawn towards the b-th firefly.
                s = random.uniform(0, 1) # [0,1] range random number
                # Xi = Xi - Beta(r) * Xi + Beta(r) * Xj + (alpha*(random - 0.5))  
                pop[a] = (1 - beta) * pop[a] + beta * pop[b] + alpha * (s - 0.5)
                
        # update target functions
        for i in range(popsize):
            f[i] = target_function(pop[i])

        # find maximum target function
        for i in range(popsize):
            if f[i] > maxfx:
                maxfx = f[i]
                xmax = pop[i]
                print(xmax)
    

    # write results to file
    with open("ates_bocegi_sonuclar.txt", "w") as fp:
        fp.write("Optimum x=%4.4f \n" % xmax)
        fp.write("Maximum target function=%4.4f \n" % maxfx)
    print("Firefly algorithm completed")
    
    return print(xmax, maxfx)

# test firefly algorithm
firefly_algorithm(popsize=10, iter=10, gama=0.9)

