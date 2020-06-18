import random
import math

""" ----------------------------------- TASK 2 -----------------------------------------
Create a one-dimensional random walk mathematical and simulation-based model where two
people start x units away from each other and are traversing the grid with some probabilities.
Predict theexpected time it takes to meet them.  You should test your models for a range of
scenarios.  List anyassumptions you may have made
"""

def Expected_Time(A_left, A_right, B_left, B_right, Distance):
    Bots = 500
    Time = 500
    
    A_bot = list()                  # bots on point A
    for i in range(Bots):
        A_bot.append( 0 )

    B_bot = list()                  # bots on point B
    for i in range(Bots):
        B_bot.append( Distance )

    Lost = list()                   # stores pairs of bots (A,B) which are yet to meet
    for a in range(Bots):
        for b in range(Bots):
            Lost.append( (a,b) )

    def Take_A_Step(my_Bots, P_left, P_right):      # simulates given bots by one step
        for bot in range(len(my_Bots)):
            Vector = random.randint(0, 1000) / 1000
            
            if Vector < P_left:
                my_Bots[bot] -= 1

            elif Vector < P_left + P_right:
                my_Bots[bot] += 1

        return my_Bots

    Total_Meets = 1
    Meetings = [ 0 ]                # Meetings[i] stores no. of meetings on step i
    for Step in range(Time):
        Meetings.append( 0 )
        
        A_bot = Take_A_Step(A_bot, A_left, A_right)
        B_bot = Take_A_Step(B_bot, B_left, B_right)

        Restore = list()            # A bot pair (a,b) that has recorded meet will not meet again
        for a, b in Lost:
            if A_bot[a] == B_bot[b]:
                Meetings[Step] += 1
                Total_Meets += 1
            else:
                Restore.append( (a,b) )
        Lost = Restore
        
    return sum([Step * Meetings[Step] for Step in range(Time)]) / Total_Meets

print(Expected_Time(0.3,0.6,0.6,0.3,5))
