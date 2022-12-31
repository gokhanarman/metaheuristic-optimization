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
    pop = [0.0 for _ in range(100)]
    f = [0.0 for _ in range(100)]
    maxfx = -1000000.0
    xmax = 0.0

    # generate random initial population
    for i in range(popsize):
        pop[i] = 0.001 * random.randint(0, 10000)  # random d within range
        f[i] = target_function(pop[i])  # calculate target function

    # mating
    eslesme = popsize * (popsize - 1) / 2.0
    for _ in range(iter):
        for _ in range(int(eslesme)):
            a = random.randint(0, popsize - 1)
            b = random.randint(0, popsize - 1)
            d = abs(pop[a] - pop[b])
            alpha = 0.001 * random.randint(0, 1001)
            beta = (0.9) * math.exp((-1.0) * gama * d * d)

            if f[a] > f[b]:
                s = 0.001 * random.randint(0, 1000)
                pop[b] = (1 - beta) * pop[b] + beta * pop[a] + alpha * (s - 0.5)
            else:
                s = 0.001 * random.randint(0, 1000)
                pop[a] = (1 - beta) * pop[a] + beta * pop[b] + alpha * (s - 0.5)

        # update target functions
        for i in range(popsize):
            f[i] = target_function(pop[i])

        # find maximum target function
        for i in range(popsize):
            if f[i] > maxfx:
                maxfx = f[i]
                xmax = pop[i]
    

    # write results to file
    with open("ates_bocegi_sonuclar.txt", "w") as fp:
        fp.write("Optimum x=%4.4f \n" % xmax)
        fp.write("Maximum target function=%4.4f \n" % maxfx)
    print("Firefly algorithm completed")
    
    return print(xmax, maxfx)

# test firefly algorithm
firefly_algorithm(popsize=10, iter=100, gama=0.5)

