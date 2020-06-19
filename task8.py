import random
import math
import numpy
""" ----------------------------------- TASK 8 -----------------------------------------
Building on task 5, each team will capture the trajectory of two nodes whose initial locations are
chosen randomly and uniformly over a circular region. Every team will be asked to explain how did
they model the initial position of the two nodes.
"""

def Distance(P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    

def Pick_from_Circ(Radius):
    dt = 2 * math.pi * numpy.random.uniform(0.0, 1.0)
    dr = math.sqrt( Radius**2  * numpy.random.uniform(0.0, 1.0))
    return (math.cos(dt) * dr, math.sin(dt) * dr)

def Expected_Time(Radius):
    Bots = 500
    Time = 500
    
    mybots = list()                     # bots list
    for i in range(Bots):
        mybots.append( Pick_from_Circ(Radius) )
        
    Lost = list()                       # stores pairs of bots (A,B) which are have not yet met.
                                        # This list will update on every step
    for a in range(len(mybots) - 1):
        for b in range(a+1, len(mybots)):
            Lost.append( (a,b) )

    def Take_A_Step(my_Bots):           # simulates all given bots by one step
        for bot in range(len(my_Bots)):
            x,y = my_Bots[bot]
            
            dr = numpy.random.uniform(0.0, 1.0)
            dt = 2 * math.pi * numpy.random.uniform(0.0, 1.0)
            
            dx = dr * math.cos(dt)
            dy = dr * math.sin(dt)

            x = x + dx
            y = y + dy
            r = math.sqrt(x**2 + y**2)

            if r > Radius:
                my_Bots[bot] = (x / r, y / r)
            else:
                my_Bots[bot] = (x + dx, y + dy)
            
        return my_Bots

    Total_Meets = 1
    Meetings = [ 0 ]                # Meetings[i] stores no. of meetings occured on step i
    for Step in range(Time):
        Meetings.append( 0 )
        
        mybots = Take_A_Step(mybots)

        Restore = list()            # A bot pair (a,b) that has recorded meet will not meet again
        for a, b in Lost:
            if Distance(mybots[a], mybots[b]) < 1:
                Meetings[Step] += 1
                Total_Meets += 1
            else:
                Restore.append( (a,b) )
        Lost = Restore
        
    return sum([Step * Meetings[Step] for Step in range(Time)]) / Total_Meets

print(Expected_Time(8))