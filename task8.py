import random
import math

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
    dt = 2 * math.pi * random.randint(0, 1000) / 1000
    dr = math.sqrt( Radius**2  * random.randint(0,1000) / 1000)
    return (math.cos(dt) * dr, math.sin(dt) * dr)

def Expected_Time(Radius):
    Bots = 200
    Time = 200

    A = Pick_from_Circ(Radius)
    B = Pick_from_Circ(Radius)

    print( 'Distance :', Distance(A, B))
    
    A_bot = list()                  # bots on point A
    for i in range(Bots):
        A_bot.append( A )

    B_bot = list()                  # bots on point B
    for i in range(Bots):
        B_bot.append( B )

    Lost = list()                   # stores pairs of bots (A,B) which are yet to meet
    for a in range(Bots):
        for b in range(Bots):
            Lost.append( (a,b) )

    def Take_A_Step(my_Bots):      # simulates given bots by one step
        for bot in range(len(my_Bots)):
            x,y = my_Bots[bot]
            
            dr = random.randint(0, 1000) / 1000
            dt = 2 * math.pi * random.randint(0, 1000) / 1000
            
            dx = dr * math.cos(dt)
            dy = dr * math.sin(dt)

            if (x + dx)**2 + (y + dy)**2 > Radius**2:
                my_Bots[bot] = (x - dx, y - dy)
            else:
                my_Bots[bot] = (x + dx, y + dy)
            
        return my_Bots

    Total_Meets = 1
    Meetings = [ 0 ]                # Meetings[i] stores no. of meetings on step i
    for Step in range(Time):
        Meetings.append( 0 )
        
        A_bot = Take_A_Step(A_bot)
        B_bot = Take_A_Step(B_bot)

        Restore = list()            # A bot pair (a,b) that has recorded meet will not meet again
        for a, b in Lost:
            if Distance(A_bot[a], B_bot[b]) < 1:
                Meetings[Step] += 1
                Total_Meets += 1
            else:
                Restore.append( (a,b) )
        Lost = Restore
        
    return sum([Step * Meetings[Step] for Step in range(Time)]) / Total_Meets

print(Expected_Time(10))
