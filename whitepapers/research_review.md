Author: Ilton Garcia dos Santos Silveira
<br>
Date: December, 06, 2017        


# AlphaGo Research Review

It paper's goals was to show how DeepMind defeated the best AlphaGo player introducing a new technique approach, 
minimizing the enormous search space of Go created by traditional AI methods, which create a search tree for each 
possible position. Using Deep Learning principles, the DeepMind implemented two deep convolution neural networks 
(CONVNET). One CONVNET, called "value network", predicts how likely a move can lead to win after optimal moves.
The other, called "policy network", helps to reduce the breadth of the searching move to play & using Monte Carlo Tree
Search (MCTS), that effectively selects actions by look-ahead search it could "prune" even more the search tree.

This paper introduced many AI training perspectives:
1. Supervised Learning using human skills to train the CONVNET;
1. Reinforcement Learning, the system played against different versions of itself, learning from its mistakes;
1. Finally the evaluation function was created using Reinforcement Learning using self-play data set.

As result, it program defeated 99.8% of others Go programs and even defeated the human European Go champion.