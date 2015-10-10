from random import randint

class Dice():

    def __init__(self,num_faces):
        self.num_faces = num_faces
        self.number = randint(1,self.num_faces)

    def roll(self):
        self.number = randint(1,self.num_faces)
        return self.number

    def print_number(self):
        print self.number


class Hand():

    def __init__(self,num_die=5,num_faces=6):
        self.num_die = num_die
        self.this_hand = []
        for die in xrange(self.num_die):
            self.this_hand.append(Dice(num_faces))

    def print_hand(self):
        tot = 0.0
        for die in xrange(self.num_die):
            self.this_hand[die].print_number()
            tot += self.this_hand[die].number
        print "Tot %4d" % tot

class Game():

    def __init__(self):
        self.score = 0.0
        
        
if __name__ == '__main__':
    my_hand = Hand(5)
    my_hand.print_hand()

