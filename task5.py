import random
import math
import numpy

""" ----------------------------------- TASK 5 -----------------------------------------
Repeat task 3 by assuming that the step size and the orientation are continuous random variables
between 0 − 1 and 0 − 2π. Again, you may find it easier to model the PDF as a uniform random
variable. Feel free to try other distributions


Task3: Create a two-dimensional random walk model using simulation-based approach within boundaries
of a circular disc. Simulation will be discrete with respect to step-size {0, 0.5, 1} and
direction [0 ~ 360].
"""

def Round_Simulation(Radius):
    Time = 500
    Bots = 500
    
    Curr_Pos = list()
    myBot = list()
    for _ in range(Bots):
        Curr_Pos.append( (0,0) )                                #Initial position of bots
        myBot.append( list() )

    for Step in range(Time):
        
        for bot in range(Bots):
            dr = numpy.random.uniform(0.0, 1.0)                 #Randomly selects the step size
            dt = 2 * math.pi * numpy.random.uniform(0.0, 1.0)   #Randomly selects the direction

            x, y = Curr_Pos[bot]
            dx, dy = dr * math.cos(dt), dr * math.sin(dt)       #Converts movement into cartesian coordinates

            Curr_Pos[bot] = (x + dx, y + dy)

            if (x + dx)**2 + (y + dy)**2 > Radius**2:           #Formula mentioned in the write-up
                Curr_Pos[bot] = ( (x+dx) / (math.sqrt((x+dx)**2 + (y+dy)**2)), (y+dy) / (math.sqrt((x+dx)**2 + (y+dy)**2)))

            myBot[bot].append(Curr_Pos[bot])

    return Curr_Pos

print("Bots are standing at points:", Round_Simulation(100))
