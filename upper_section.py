from __future__ import division
import numpy as np
import itertools
from numpy.random import randint

"""
    Currently, attempts to tell you whether you should
      hold or roll your dice in an attempt to maximize
      the expected value of a strategy-based reward

    Unfortunately, the algorithm is greedy and only looks
      to maximize *immediate* gains, not looking to what
      stategy maximizes overall score

"""


class State:

    def __init__(self,num_faces=6,num_dice=5):
        self.num_faces    = num_faces
        self.num_dice     = num_dice
        self.state_matrix = np.zeros((self.num_faces,self.num_dice))
        self.permutations = list(itertools.product('HR',repeat=self.num_dice))
        self.possible_states = []
        self.available_strategies = range(0,self.num_faces)
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

    def reward_vec(self,number):
        return number*np.eye(1,self.num_faces,number)

    def choose_strategy(self):
        best_outcome = 0.0
        best_strategy = 0
        for strategy in self.available_strategies:
            for idx, state in enumerate(self.possible_states):
                reward = np.sum(np.dot(self.reward_vec(strategy),state))
                if reward > best_outcome:
                    best_outcome = reward
                    best_strategy = strategy + 1
                    best_action = self.permutations[idx]
        print best_outcome, best_strategy, best_action
            
                


if __name__ == '__main__':

   my_hand = State()
   my_hand.roll_all()
   my_hand.enumerate_states()
   print my_hand.state_matrix
   my_hand.choose_strategy()
   

