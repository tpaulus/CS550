"""
ai - search & strategy module

implement a concrete Strategy class and AlphaBetaSearch
"""
import abstractstrategy
from checkerboard import *


class Strategy(abstractstrategy.Strategy):

    def play(self, board) -> (CheckerBoard, tuple):
        pass

    def utility(self, board: CheckerBoard) -> int:
        __king_weight = 5
        kings = board.get_kingsN()
        pawns = board.get_pawnsN()

        red = __king_weight * kings[0] + pawns[0]
        black = __king_weight * kings[1] + pawns[1]
        if board.playeridx(self.maxplayer) is 0:
            return red - black
        else:
            return black - red

class AlphaBetaSearch:
    """AlphaBetaSearch
    Conduct alpha beta searches from a given state.

    Example usage:
    # Given an instance of a class derived from AbstractStrategy, set up class
    # to determine next move, maximizing utility with respect to red player
    # and minimiizing with respect to black player. Search 3 plies.
    search = AlphaBetaSearch(strategy, 'r', 'b', 3)

    # To find the move, run the alphabeta method
    best_move = search.alphabeta(some_checker_board)
    """

    def __init__(self, strategy, maxplayer, minplayer, maxplies=3,
                 verbose=False):
        """"AlphaBetaSearch - Initialize a class capable of alphabeta search
        strategy - implementation of AbstractStrategy class
        maxplayer - name of player that will maximize the utility function
        minplayer - name of player that will minimize the utility function
        maxplies- Maximum ply depth to search
        verbose - Output debugging information
        """

    def alphabeta(self, state):
        """alphbeta(state) - Run an alphabeta search from the current
       state. Returns best action.
       """
    # define other helper methods as needed
