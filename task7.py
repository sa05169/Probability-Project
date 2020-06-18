import random
import math
import numpy

""" ----------------------------------- TASK 7 -----------------------------------------
Repeat task 3 by assuming that the step size is a discrete random variable and the orientation is a
continuous random variables between 0 − 2π.

Task3: Create a two-dimensional random walk model using simulation-based approach within boundaries
of a circular disc. Simulation will be discrete with respect to step-size {0, 0.5, 1} and
direction [0 ~ 360].
"""

def Round_Simulation(Radius):
    Time = 100
    Bots = 100
    
    Step_Size = [0, 0.5, 1]                                     # discrete steps
    
    Curr_Pos = list()
    myBot = list()
    for _ in range(Bots):
        Curr_Pos.append( (0,0) )
        myBot.append( list() )

    for Step in range(Time):
        
        for bot in range(Bots):
            dr = Step_Size[ random.randint(0,2) ]
            dt = 2 * math.pi * numpy.random.uniform(0.0, 1.0)

            x, y = Curr_Pos[bot]
            dx, dy = dr * math.cos(dt), dr * math.sin(dt)

            if (x + dx)**2 + (y + dy)**2 > Radius**2:
                Curr_Pos[bot] = (x - dx, y - dy)
            else:
                Curr_Pos[bot] = (x + dx, y + dy)

            myBot[bot].append(Curr_Pos[bot])

    return Curr_Pos

print("Bots are standing at point:", Round_Simulation(100))
