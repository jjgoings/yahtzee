import numpy as np
import collections
import itertools


three_combos = (list(itertools.product('123456',repeat=3)))

hands = []
for combo in three_combos:
    hand = np.zeros((6,1))
    for i in xrange(len(combo)):
        hand[int(combo[i])-1,0] += 1
    non_zeros = np.nonzero(hand)
#    print hand
#    print non_zeros
    if len(non_zeros[0]) == 1:
       hands.append('3')
    elif len(non_zeros[0]) == 2:
       hands.append('12')
    elif len(non_zeros[0]) == 3:
       hands.append('111')

counter = collections.Counter(hands)

print counter.values()
print counter.keys()

