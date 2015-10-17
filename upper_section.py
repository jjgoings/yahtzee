from __future__ import division
import numpy as np
import itertools
from numpy.random import randint
from scipy.special import binom
from math import factorial

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
        self.rolls_left  = 3
        self.expected_outcome = []
        self.available_strategies = range(0,self.num_faces)
        self.populate_expected_outcome()

    def roll(self,dice):
        I = randint(0,self.num_faces)
        self.state_matrix[:,dice] = 0.0 # Clear state
        self.state_matrix[I,dice] = 1.0 

    def roll_all(self):
        for dice in xrange(self.num_dice):
            self.roll(dice)
        self.rolls_left -= 1

    def probability(self):
        prob_not = 1.0 - 1.0/self.num_faces
        return 1.0 - np.power(prob_not,self.rolls_left)

    def enumerate_states(self):
        current_state = np.copy(self.state_matrix)
        self.possible_states = []
        for permutation in self.permutations:
            for idx, action in enumerate(permutation):
                if action == 'R':
                   probability = self.probability()
                   current_state[:,idx] = probability
                # no else, cause we do nothing for hold!
            self.possible_states.append(current_state)
            current_state = np.copy(self.state_matrix)

    def reward_vec(self,number):
        return number*np.eye(1,self.num_faces,number)

    def count_vec(self,number):
        return np.eye(1,self.num_faces,number)

    def populate_expected_outcome(self):
        for face in xrange(self.num_faces): 
            outcome = self.num_dice*self.probability()
            self.expected_outcome.append(outcome)

    def choose_strategy(self):
        max_rarity = 0.0
        best_strategy = 0
        best_outcome = 0.0
#        for strategy in self.available_strategies:
#            for idx, state in enumerate(self.possible_states):
#                reward = np.sum(np.dot(self.reward_vec(strategy),state))
#                if reward > best_outcome:
#                    best_outcome = reward
#                    best_strategy = strategy + 1
#                    best_action = self.permutations[idx]
        for strategy in self.available_strategies:
            for idx, state in enumerate(self.possible_states):
                number = np.sum(np.dot(self.count_vec(strategy),state))
                reward = np.sum(np.dot(self.reward_vec(strategy),state))
                if number > self.expected_outcome[strategy]:
                    rarity = number - self.expected_outcome[strategy]
                    if rarity >= max_rarity:
                        max_rarity = rarity
                        if reward > best_outcome:
                            best_outcome = reward
                            best_strategy = strategy + 1
                            best_action = self.permutations[idx]
        print "You could expect a score of: ", best_outcome
        print "If you go for your: ", best_strategy
        print "So hold/roll these: ", best_action
            
                


if __name__ == '__main__':

   my_hand = State()
   my_hand.roll_all()
   my_hand.enumerate_states()
   print my_hand.state_matrix
   print "You have %s rolls left" % my_hand.rolls_left
   my_hand.choose_strategy()
   

