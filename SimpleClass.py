from __future__ import division
import numpy as np
from numpy.random import randint

"""
    This is a class that sets up the following game:

       Say you have a die with a certain number of faces, and a 
       finite number of rolls. You receive the score of the die.
       You may continue rolling, or you may take your score as is. 
       This class finds the optimal roll strategy (either roll or
       hold) for the finite numer of rolls for the given die. 

       You may change the number of rolls or the number of faces
       on the die.

       In __main__ you can hard code the number of games following 
       this strategy. In the limit of large number of games, you 
       should get the optimal expected value. Some optimal strategy
       expected values are:

       num_faces = 6 & num_rolls = 1 : expected score = 3.5
       num_faces = 6 & num_rolls = 2 : expected score = 4.25
       num_faces = 6 & num_rolls = 3 : expected score = 4.66

"""


class Dice:


    def __init__(self,num_faces=6,num_turns=3):
        self.num_faces          = num_faces
        # reward vector is just the number on each face, but of course
        # it needn't be!
        # Can I make init of reward vector more elegant?
        self.reward_vector      = np.empty((self.num_faces,1))
        self.reward_vector[:,0] = np.arange(1,self.num_faces+1)
        # probability to roll another face
        self.trans_roll         = np.ones((self.num_faces,self.num_faces)) \
                                    * (1.0/self.num_faces)
        # probability to stay the same -- identity matrix!
        self.trans_hold         = np.eye(self.num_faces)
        # state_vector not in use at the moment, I'm keeping it
        # for when I generalize this routine
        self.state_vector       = np.zeros((self.num_faces,1))
        self.num_turns          = num_turns
        self.num_turns_left     = num_turns

    def expectedValues(self): 
        # NVec updates reward vector based on number of rolls
        # if we only rolled once, NVec would remain reward vector
        NVec = np.copy(self.reward_vector)
        for turn in xrange(self.num_turns_left):
            expected_value_Roll = np.dot(self.trans_roll,NVec)
            expected_value_Hold = np.dot(self.trans_hold,NVec)
            for i in xrange(self.num_faces):
                NVec[i] = max(expected_value_Hold[i],\
                              expected_value_Roll[i])
        return np.mean(NVec) 

    def play_game(self):
        for roll in xrange(self.num_turns):
            # since num_turns_left = num_turns, decrement by 1
            # at the top because this is our first roll
            self.num_turns_left -= 1
            if roll == 0:
            # no action on first roll...just roll!
                current_score = randint(1,self.num_faces+1)
            else:
                exp_roll = self.expectedValues()
                if exp_roll > current_score:
                    current_score = randint(1,self.num_faces+1)
        # reset num_turns_left
        self.num_turns_left = self.num_turns
        return current_score
         
               
if __name__ == '__main__':
    num_games = 1000000
    score = 0.0
    num_dice = 1
    num_faces = 6
    num_rolls = 2
    Hand = []
    # Dice(num_faces,num_rolls)
    for dice in xrange(num_dice):
        Hand.append(Dice(num_faces,num_rolls))
    for game in xrange(num_games):
        for dice in enumerate(Hand):
            score += dice[1].play_game()

        if (game != 0 and game % 10000 == 0):
            avg_score = score/(game+1) 
            print game, avg_score
            
    avg_score = score/num_games    
    
    print num_games, avg_score
    
    
    



