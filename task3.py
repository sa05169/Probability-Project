import random
import math

""" ----------------------------------- TASK 3 -----------------------------------------
Create a two-dimensional random walk model using simulation-based approach within boundaries
of a circular disc. Simulation will be discrete with respect to step-size {0, 0.5, 1} and
direction [0 ~ 360].
"""

def Round_Simulation(Radius):
    Time = 10
    Bots = 10
    
    Step_Size = [0, 0.5, 1]                                     # discrete steps
    Orientation = [0, math.pi / 2, math.pi, 3 * math.pi / 2]    # discrete orientation
    
    Curr_Pos = list()
    myBot = list()
    for _ in range(Bots):
        Curr_Pos.append( (0,0) )
        myBot.append( list() )

    for Step in range(Time):
        
        for bot in range(Bots):
            dr = Step_Size[ random.randint(0,2) ]
            dt = Orientation[ random.randint(0, 3) ]

            x, y = Curr_Pos[bot]
            dx, dy = dr * math.cos(dt), dr * math.sin(dt)

            if (x + dx)**2 + (y + dy)**2 > Radius**2:
                Curr_Pos[bot] = (x - dx, y - dy)
            else:
                Curr_Pos[bot] = (x + dx, y + dy)

            myBot[bot].append(Curr_Pos)

    return Curr_Pos

print(Round_Simulation(100))