"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float('-inf')

    if game.is_winner(player):
        return float('inf')

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    center_score = (Score.center(game, player) == 0) * 10.
    return float(own_moves - 2. * opp_moves + center_score)

def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float('-inf')

    if game.is_winner(player):
        return float('inf')

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - 2*opp_moves)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_loser(player):
        return float('-inf')

    if game.is_winner(player):
        return float('inf')

    center_score = (Score.center(game, player) == 0) * 10.
    my_open_move_options = Score.open_move(game, player)

    return my_open_move_options + center_score


class Score:
    # Outputs a score equal to square of the distance from the center of the board to the position of the player
    # Used only by the autograder for testing
    @staticmethod
    def center(game, player):
        if game.is_loser(player):
            return float('-inf')
        if game.is_winner(player):
            return float('inf')

        w, h = game.width / 2., game.height / 2.
        y, x = game.get_player_location(player)
        return float((h - y) ** 2 + (w - x) ** 2)

    # Evaluation about the score, which is equal to the number of moves open for your computer player on the board
    @staticmethod
    def open_move(game, player):
        if game.is_loser(player):
            return float('-inf')
        if game.is_winner(player):
            return float('inf')

        return float(len(game.get_legal_moves(player)))



class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """

        # Like on the Graphic View it represents the down triangle (min_val)
        def min_val(game, depth):
            # (note 2)
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            # if "root depth" just return it score
            if depth == 0:
                return self.score(game, self)

            # get the legal moves (empty & on range spaces) from isolation.Board
            legal_moves = game.get_legal_moves()
            # positive "infinity" float to start comparing which is the lowest (anything will be less than that)
            main_score = float('inf')

            # for each move, test it game forecast_move & eval it max in 1 depth level
            # (it is recursive, so this call return to it method in next depth)
            for each_move in legal_moves:
                game_subbranch = game.forecast_move(each_move)
                score = max_val(game_subbranch, depth - 1)
                # as min_val, if main is greater than the score, so update vars
                if score < main_score:
                    best_move = each_move
                    main_score = score

            return main_score

        # Like on the Graphic View it represents the up triangle (max_val)
        def max_val(game, depth):
            # (note 2)
            if self.time_left() < self.TIMER_THRESHOLD:
                raise SearchTimeout()

            # if "root depth" just return it score
            if depth == 0:
                return self.score(game, self)

            # get the legal moves (empty & on range spaces) from isolation.Board
            legal_moves = game.get_legal_moves()
            # negative "infinity" float to start comparing which is the highest (anything will be greater than that)
            main_score = float('-inf')

            # for each move, test it game forecast_move & eval it min in 1 depth level
            # (it is recursive, so this call return to it method in next depth)
            for each_move in legal_moves:
                game_subbranch = game.forecast_move(each_move)
                score = min_val(game_subbranch, depth - 1)
                # as max_val, if main is greater than the score, so update vars
                if score > main_score:
                    best_move = each_move
                    main_score = score

            return main_score

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # init variables
        best_move = (-1, -1)
        main_score = float('-inf')
        legal_moves = game.get_legal_moves()

        # if there are legal_moves, so use any random move on it as first best_move
        if legal_moves:
            best_move = legal_moves[random.randint(0, len(legal_moves) - 1)]

        # Eval min-max for each move in legal_moves
        for each_move in legal_moves:
            # it is the same base of max_val, but when min_val is called it starts a recursive loop
            # it is working like a "propagation" for nodes levels above
            game_subbranch = game.forecast_move(each_move)
            score = min_val(game_subbranch, depth - 1)
            if score > main_score:
                best_move = each_move
                main_score = score

        return best_move


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # init variables, if it abort by timeout it returns something
        depth = 1
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()

        # rand initial best_move
        if legal_moves:
            best_move = legal_moves[random.randint(0, len(legal_moves) - 1)]

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire (before forfeit)
            while True:
                best_move = self.alphabeta(game, depth)
                depth += 1 # goes deeper
        except SearchTimeout:
            return best_move
            pass  # Handle any actions required after timeout as needed

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # init variables
        best_move = (-1, -1)
        init_best_move = best_move
        main_score = float('-inf')
        player_legal_moves = game.get_legal_moves(game.active_player)

        try:
            best_move = player_legal_moves[0]
        except IndexError:
            return init_best_move
        for idx, move in enumerate(player_legal_moves):
            v = self.min_alpha_beta(game.forecast_move(move), alpha, beta, depth-1)
            if v > main_score:
                alpha = v
                main_score = v
                best_move = move
        return best_move

    # Calculate the heuristic value of a game state from the point of player (my winner score algorithm)
    def score(self, game, player):
        return custom_score_2(game, player)

    # Return True if the game is over for the active player, false otherwise
    # Also perform the Cutoff-test described in AIMA, ps 173
    def cutoff_test(self, game, depth):
        # check if there is still time left
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # control the depth.
        if depth < 1:
            # Depth one means terminal state
            # print('depth: ', depth)
            return True
        # check if there are still legal moves by Assumption 1
        return not bool(game.get_legal_moves(game.active_player))

    # min alpha beta helper
    # implement the proposed function in AIMA, page 170
    def min_alpha_beta(self, game, alpha, beta, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # init values
        main_score = float('inf')
        legal_moves = game.get_legal_moves(game.active_player)

        # cutoff_test
        if self.cutoff_test(game, depth):
            return self.score(game, self)

        # calculate beta for each move,
        # if main score is less or equals alpha, so it returns that main score
        for each_move in legal_moves:
            game_subbranch = game.forecast_move(each_move)
            score = self.max_alpha_beta(game_subbranch, alpha, beta, depth - 1)
            main_score = min(main_score, score)

            if main_score <= alpha:
                return main_score

            beta = min(beta, main_score)

        return main_score

    # max alpha beta helper
    def max_alpha_beta(self, game, alpha, beta, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # init values
        main_score = float('-inf')
        legal_moves = game.get_legal_moves()

        # if "root depth" it current score is the max
        if self.cutoff_test(game, depth):
            return self.score(game, self)

        # calculate alpha for each move,
        # if main score is greater or equals beta, so it returns that main score
        for each_move in legal_moves:
            game_subbranch = game.forecast_move(each_move)
            score = self.min_alpha_beta(game_subbranch, alpha, beta, depth - 1)
            main_score = max(main_score, score)

            if main_score >= beta:
                return main_score

            alpha = max(alpha, main_score)

        return main_score