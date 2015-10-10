from __future__ import division
import numpy as np
from random import randint

class State():
    def __init__(self,nstates=6):
        self.nstates = nstates
        self.Vec     = np.eye(self.nstates,1)
        self.TRoll   = (1.0/self.nstates)*np.ones((self.nstates,self.nstates))
        self.THold   = np.eye(self.nstates,self.nstates)
        ScoreMatrix  = np.zeros((self.nstates,self.nstates))
        for i in xrange(nstates):
            ScoreMatrix[:,i] = (i+1)*np.ones((self.nstates))
        self.ScoreMat = ScoreMatrix
        self.score = np.dot(self.Vec.T,np.dot(self.ScoreMat,self.Vec))
        self.curRoll = 0

    def evalScore(self,action='Hold'):
        if action == 'Hold':
            transMat = self.THold
        elif action == 'Roll':
            transMat = self.TRoll
        newState = np.dot(transMat,self.Vec)
        return np.dot(newState.T,np.dot(self.ScoreMat,newState))
 
    def roll(self):
        k = randint(0,self.nstates-1)
        self.Vec     = np.eye(self.nstates,1,-k)
        self.score = np.dot(self.Vec.T,np.dot(self.ScoreMat,self.Vec))

    def play(self):
        if self.curRoll == 0:
            self.roll()
        scoreHold = self.evalScore('Hold')
        scoreRoll = self.evalScore('Roll')
        if self.score >= scoreRoll:
           print self.score
           print scoreRoll
           action = 'Hold'
        elif self.score < scoreRoll:
           print self.score
           print scoreRoll
           action = 'Roll'
        print action          



state = State()

state.play()



