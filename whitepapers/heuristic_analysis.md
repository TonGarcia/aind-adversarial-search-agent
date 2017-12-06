Author: Ilton Garcia dos Santos Silveira
<br>
Date: December, 06, 2017        


# Choosing a Heuristic to an Isolation Game-Playing Agent

That analysis should expose the comparison of the the different heuristics & my reasoning for choosing the the heuristic I ultimately use in mine submitted agent.



## The Strategies

1. __MiniMax Algorithm__: performs a complete depth-first exploration of the game tree and its time cost in real games can be impractical;
1. __Alpha-Beta Pruning__: the second one, alpha-beta pruning, ignores a portion of the search tree that makes no difference to the final choice. According to Russell (Artificial Intelligence: A Modern Approach), when this technique is applied to standard minimax tree, it returns the same move as minimax would.



### Heuristic Evaluation Functions

All my three evaluation functions was based on Udacity evaluation functions: _```improved_score```_ & _```open_move_score```_ :

1. __custom_score_2__: weighted linear function, where opponent’s moves are two times more relevant than the agent’s moves. The motivation of this approach is to influence the agent to prioritize moves that minimize the moves from the opponent before maximize its moves.
1. __custom_score_3__: rewards the agent based on the amount of legal moves that still available, as the Udacity open move score function does, and it also gives an additional reward to the agent if it is in the center of the board. The idea is to motivate the agent to dominate the center when it is possible.
1. __custom_score__: it is a mix of the both previous approaches, using weights giving more relevance to opponent's moves, but also giving additional reward when the agent moves to the center of the board. This way it dominates the center paynig attention on opponent's moves.

As a Result I got:

| Opponent    | AB_Improved | AB_Custom | AB_Custom_2 | AB_Custom_3 |
|-------------|-------------|-----------|-------------|-------------|
| Random      |    9 / 1    | 10 / 0    |    10 / 0   |    8 / 2    |
| MM_Open     |    8 / 2    |   8 / 2   |    8 / 2    |    6 / 4    |
| MM_Center   |   10 / 0    |   9 / 1   |    5 / 5    |    7 / 3    |
| MM_Improved |    6 / 4    |   7 / 3   |    7 / 3    |    10 / 0   |
| AB_Open     |    5 / 5    |   4 / 6   |    6 / 4    |    6 / 4    |
| AB_Center   |    7 / 3    |   4 / 6   |    6 / 4    |    6 / 4    |
| AB_Improved |    6 / 4    |   5 / 5   |    8 / 2    |    4 / 6    |
| WIN RATE    |    72.0%    |   67.0%   |    74.0%    |    67.0%    |

So, by this result I choose my AB_Custom_2 as the winner strategy because it won 74.0%, the best WIN RATE.
As the __custom_score__ a mix of strategy 2 & strategy 3 I expected that it would be the better answer. But it proved that using this approach is better only against a Random & MM Agents, against AB Agents it mix become vulnerable. Another conclusion is that the mix between 2 and 3 performed exactly the same as the strategy 3 on WIN RATE perspective, which means that the mix brought no "globally" improvements for AB3 & down the AB2 perform.

According to the video "16 Solving 5x5 Isolation", Malcolm Haines explained how he got better results moving by the edges instead of using the center (my strategy for score_3), and considering the edges he could explore the advantage that the edges looks & work as mirrors each other, reducing the search effort. But the most important is that moving away from the center & paying attention on opponent's moves, reflecting it, the better way is to take a decision based on the situation (opponents reactions), not following a fixed strategy, which can be reflected.   