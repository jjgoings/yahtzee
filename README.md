README

This is a set of code and algorithms for solving the optimal strategy problem in the dice game Yahtzee.

Late one night, playing Yahtzee with my wife, I realized that I didn't know the optimal strategy for the dice game Yahtzee.

For example, say I rolled 1,1,1,2,3:
	* do I go for my ones?
	* do I go for Full House?
	* should I just reroll?

I had no idea, but figured a computer should be able to help me out.

Currently my strategy is based on finite horizon Markov Decision Process. We'll see where it goes in the future.

SimpleClass solves a very simple dice game, where you have a certain number of rolls to get the highest value face you can (which is your score).

I'm working to generalize this to several dice and eventually the whole game of Yahtzee, but I'm in no rush.


