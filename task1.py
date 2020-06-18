import random
import math

""" ----------------------------------- TASK 1 -----------------------------------------
Create a one-dimensional random walk mathematical and simulation-based model to predict the
ex-pected  distance  from  the  starting  point.   You  should  test  your  models  for
range  of  scenarios  e.g.starting position, (un)equal probabilities of moving left, right,
and not moving at all.
"""

def Expected_Position(P_left, P_right, Time, Init_Pos = 0):
    
    P_stay = 1 - P_left - P_right           # Probability of not moving
    
    Simulation_Bots = list()
    for _ in range(1000):                   # Creating 1000 bots for simulations
        
        Simulation_Bots.append( Init_Pos )  # Simulation_Bots[i] is current position of
                                            # i_th bot performing the random walk

    for Step in range(Time):                # Stepwise Simulation
        
        for bot in range(1000):             # move all bots by one step
            
            Vector = random.randint(0, 1000) / 1000         # choose uniformly within continuous [0, 1]
            
            if Vector < P_left:                             # Vector coming in range of left
                Simulation_Bots[bot] -= 1
                
            elif Vector < P_left + P_right:                 # Vector coming in range of Right
                Simulation_Bots[bot] += 1

    return sum(Simulation_Bots) / len(Simulation_Bots)      # return Average of all Final positions

