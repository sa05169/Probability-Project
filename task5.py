import random
import math

""" ----------------------------------- TASK 5 -----------------------------------------
Repeat task 3 by assuming that the step size and the orientation are continuous random variables
between 0 − 1 and 0 − 2π. Again, you may find it easier to model the PDF as a uniform random
variable. Feel free to try other distributions


Task3: Create a two-dimensional random walk model using simulation-based approach within boundaries
of a circular disc. Simulation will be discrete with respect to step-size {0, 0.5, 1} and
direction [0 ~ 360].
"""

def Round_Simulation(Radius):
    Time = 10
    Bots = 10
    
    Curr_Pos = list()
    myBot = list()
    for _ in range(Bots):
        Curr_Pos.append( (0,0) )
        myBot.append( list() )

    for Step in range(Time):
        
        for bot in range(Bots):
            dr = random.randint(0, 1000) / 1000
            dt = 2 * math.pi * random.randint(0, 1000) / 1000

            x, y = Curr_Pos[bot]
            dx, dy = dr * math.cos(dt), dr * math.sin(dt)

            if (x + dx)**2 + (y + dy)**2 > Radius**2:
                Curr_Pos[bot] = (x - dx, y - dy)
            else:
                Curr_Pos[bot] = (x + dx, y + dy)

            myBot[bot].append(Curr_Pos)

    return Curr_Pos

print(Round_Simulation(100))
