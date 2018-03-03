"""
ai - search & strategy module

implement a concrete Strategy class and AlphaBetaSearch
"""
import abstractstrategy
from checkerboard import *
import sys


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

    def __init__(self, strategy: Strategy, maxplayer, minplayer, maxplies=3,
                 verbose=False):
        """"AlphaBetaSearch - Initialize a class capable of alphabeta search
        strategy - implementation of AbstractStrategy class
        maxplayer - name of player that will maximize the utility function
        minplayer - name of player that will minimize the utility function
        maxplies- Maximum ply depth to search
        verbose - Output debugging information
        """
        self.__strategy = strategy
        self.__maxplayer = maxplayer
        self.__minplayer = minplayer
        self.__maxplies = maxplies
        self.__verbose = verbose

    def alphabeta(self, state:CheckerBoard):
        """alphbeta(state) - Run an alphabeta search from the current
       state. Returns best action.
       """
        value = self.max_value(state, -1 * sys.maxsize, sys.maxsize)
        for action in state.get_actions(self.__maxplayer):
            if self.__strategy.utility(state.move(action)) is value:
                return action
        raise Exception("No Action Made")

    def max_value(self, state: CheckerBoard, alpha: int, beta: int):
        # Negative Infinity
        value = -1 * sys.maxsize
        if state.is_terminal():
            value = self.__strategy.utility(state)
        else:
            for action in state.get_actions(self.__maxplayer):
                value = max(value, self.min_value(state.move(action), alpha, beta))
                if value >= beta:
                    break
                else:
                    alpha = max(alpha, value)
        return value

    def min_value(self, state: CheckerBoard, alpha: int, beta: int):
        # Infinity
        value = sys.maxsize
        if state.is_terminal():
            value = self.__strategy.utility(state)
        else:
            for action in state.get_actions(self.__minplayer):
                value = min(value, self.max_value(state.move(action), alpha, beta))
                if value <= alpha:
                    break
                else:
                    beta = min(beta, value)
        return value
