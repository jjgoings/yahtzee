from __future__ import division
import numpy as np
import itertools
from numpy.random import randint

"""
    Currently, attempts to tell you whether you should
      hold or roll your dice in an attempt to maximize
      the expected value of a strategy-based reward

"""


class State:

    def __init__(self,num_faces=6,num_dice=5):
        self.num_faces    = num_faces
        self.num_dice     = num_dice
        self.state_matrix = np.zeros((self.num_faces,self.num_dice))
        self.permutations = list(itertools.product('HR',repeat=self.num_dice))
        self.possible_states = []
        self.reward_ones = np.eye(self.num_faces,1)

    def roll(self,dice):
        I = randint(0,self.num_faces)
        self.state_matrix[:,dice] = 0.0 # Clear state
        self.state_matrix[I,dice] = 1.0 

    def roll_all(self):
        for dice in xrange(self.num_dice):
            self.roll(dice)

    def enumerate_states(self):
        current_state = np.copy(self.state_matrix)
        self.possible_states = []
        for permutation in self.permutations:
            for idx, action in enumerate(permutation):
                if action == 'R':
                   probability = 1.0/self.num_faces
                   current_state[:,idx] = probability
                # no else, cause we do nothing for hold!
            self.possible_states.append(current_state)
            current_state = np.copy(self.state_matrix)
                


if __name__ == '__main__':


   my_hand = State()
   my_hand.roll_all()

   my_hand.state_matrix = np.zeros((my_hand.num_faces,my_hand.num_dice))
   my_hand.state_matrix[0,:] = 1.0

   my_hand.enumerate_states()
   rewards = []
   for state in my_hand.possible_states:
       rewards.append(np.sum(np.dot(my_hand.reward_ones.T,state)))
 
   idx = np.argmax(rewards)       
   print my_hand.state_matrix
   print my_hand.permutations[idx]
   print my_hand.possible_states[idx]
   print max(rewards)
   

