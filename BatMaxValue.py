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
  #%% initialize variables
  # Max 100 popsize
  # 0 values for these variables in every iterations
  
  pop = [0.0 for i in range(pop_size)] # x values
  fitness = [0.0 for i in range(pop_size)] # fitness values
  pulse_rate = [0.0 for i in range(pop_size)] # pulse rates
  loudness = [0.0 for i in range(pop_size)] # loudness values
  velocity = [0.0 for i in range(pop_size)] # velocity values
  

  # initialize other variables
  # Frekans of bats. (We can choose what we want)
  
  fmin = 0.0      # Fi=[Fmin, Fmax] 
  fmax = 0.001    # It can be Fmin=0.0 ve Fmax=1.0 
  
  best_solution = -1000000.0    # global best value
  random.seed()
  counter = 1

  #%% calculate average loudness
  avg_loudness = 0.0            # Avarage Loudness of Bats
  sum_all_loudness = 0.0
  
  for i in range(pop_size):
    loudness[i] = random.uniform(0, 1) # Random [0,1] For Loudness
    sum_all_loudness = sum_all_loudness + loudness[i]        # sum all loudness for all bats
  avg_loudness = sum_all_loudness / pop_size   # average loudness value           

  #%% initialize pulse rates
  for i in range(pop_size):
    pulse_rate[i] = random.uniform(0.5, 1) # Random [0.5,1] For Pulse Rates

  #%% main loop
  while counter <= iterations:
    # generate random population
    for i in range(pop_size):
      pop[i] = random.uniform(0, 10) # random x in range [0, 10]
      fitness[i] = optimize(pop[i]) # calculate fitness
      if best_solution < fitness[i]: # update best solution
        best_solution = fitness[i]   # Global best function value
        best_solution_x = pop[i]     # Global best x value

    # loop through population
    # Two type search --> Local and random search
    for i in range(pop_size):
      d = random.uniform(0, 1)
      
      if d < pulse_rate[i]:
        # local search for i-th bat
        
        # position of bat --> Xit = Xit-1                
        pop[i] = best_solution_x  
        
        # position of bat --> Xi(t) = Xi(t-1) + ???k . Aavg(t-1)
        pop[i] = pop[i] + (random.uniform(-1.0, 1.0) * avg_loudness) # ???k --> [-1, 1] range
        
      else:
        # random search for i-th bat
        beta = random.uniform(0, 1)
        
        # Fi(t) = Fmin + (Fmax - Fmin).ui 
        fitness[i] = fmin + (fmax - fmin)*beta 
        
        # Vi(t) = Vi(t-1) + (Xi(t-1) - Xg).Fi(t) 
        velocity[i] = velocity[i] + (best_solution_x - pop[i]) * fitness[i]
        
        # Xi(t) = Xi(t-1) + Vi(t) 
        
        pop[i] = pop[i]  + velocity[i]
        
    counter += 1
    
    for i in range(pop_size):
        
      # Ai(t+1) = alpha . Ai(t) 
      loudness[i] = alpha * loudness[i]
      
      # Ri(t+1) = Rmaxt  . [1- 0.5. gama ^ iterasyon no]
      pulse_rate[i] = 1.0 - 0.5 * gama**counter
# write results to file
    with open("yarasa_sonuclar.txt", "w") as fp:
        fp.write("Optimum x=%4.4f \n" % best_solution_x )
        fp.write("Maximum target function=%4.4f \n" % best_solution)
    print("Bat algorithm completed")
    
    return best_solution, best_solution_x     

  # return best solution
  return best_solution, best_solution_x

# test the yarasa function
result = yarasa(20, 20, 0.95, 0.95)
print("Best solution:", result)
