from __future__ import division
import numpy as np
from numpy.random import randint

n = 6

# try this way of creating rvec for now
RVec = np.empty((n,1))
RVec[:,0] = np.arange(1,n+1)

PRoll = np.ones((n,n))*(1.0/n)
PHold = np.eye(n)
SVec = np.zeros((n,1))
I = np.eye(n)


def expectedValues(num_turns_left, num_states, PRoll, PHold, RVec): 
    NVec = np.empty((n,1))
    for turn in range(num_turns_left):
        ERoll = np.dot(PRoll,RVec)
        EHold = np.dot(PHold,RVec)
        for i in range(num_states):
            # probably there is a better way to determine max
            if ERoll[i] >= EHold[i]:
                NVec[i] = ERoll[i] 
            else:
                NVec[i] = EHold[i]
            # compare expected value for roll or hold for each state.
#    print RVec
    return np.mean(NVec) 
       
num_games = 1000000
num_rolls = 3 
score = 0.0
for game in range(num_games):
    for roll in range(num_rolls):
        if roll == 0:
            expRoll = expectedValues(num_rolls - roll, n, PRoll, PHold, RVec) 
            current_score = randint(1,n+1)
        else:
            expRoll = expectedValues(num_rolls - roll, n, PRoll, PHold, RVec) 
            if expRoll > current_score:
                current_score = randint(1,n+1)
        #print current_score, expRoll
    score += current_score

avg_score = score/num_games    

print avg_score




