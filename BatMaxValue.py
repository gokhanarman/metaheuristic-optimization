# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:45:24 2022

@author: ARMAN
"""

import random
import math

# function to optimize: y = -x^2 + 10x - 24
def optimize(x):
  return -x**2 + 10*x - 24

# function to run the Yarasa algorithm
def yarasa(pop_size, iterations, alpha, gama):
  # initialize variables
  pop = [0.0 for i in range(100)] # x values
  fitness = [0.0 for i in range(100)] # fitness values
  pulse_rate = [0.0 for i in range(100)] # pulse rates
  loudness = [0.0 for i in range(100)] # loudness values
  velocity = [0.0 for i in range(100)] # velocity values

  # initialize other variables
  fmin = 0.0
  fmax = 0.001
  best_solution = -1000000.0
  random.seed()
  counter = 1

  # calculate average loudness
  avg_loudness = 0.0
  for i in range(pop_size):
    loudness[i] = 0.001*(random.randint(0, 1000))
    avg_loudness += loudness[i]
  avg_loudness /= pop_size

  # initialize pulse rates
  for i in range(pop_size):
    pulse_rate[i] = 1 - 0.5*0.001*(random.randint(0, 1000))

  # main loop
  while counter <= iterations:
    # generate random population
    for i in range(pop_size):
      pop[i] = 0.001*(random.randint(0, 10000)) # random x in range [0, 10]
      fitness[i] = optimize(pop[i]) # calculate fitness
      if best_solution < fitness[i]: # update best solution
        best_solution = fitness[i]
        best_solution_x = pop[i]

    # loop through population
    for i in range(pop_size):
      d = 0.001*(random.randint(0, 1000))
      if d < pulse_rate[i]:
        # local search for i-th bat
        pop[i] = best_solution_x
        pop[i] += (random.uniform(-1.0, 1.0)*avg_loudness)
      else:
        # random search for i-th bat
        beta = random.uniform(0, 1)
        fitness[i] = fmin + (fmax - fmin)*beta
        velocity[i] = (velocity[i]*alpha) + (best_solution_x - pop[i])*(loudness[i]*beta) + (gama*pulse_rate[i]*(best_solution_x - pop[i]))
        pop[i] += velocity[i]
    counter += 1

  # return best solution
  return best_solution

# test the yarasa function
result = yarasa(100, 1000, 0.9, 0.9)
print("Best solution:", result)
