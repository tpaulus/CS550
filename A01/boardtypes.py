import copy
import math
import random

from basicsearch_lib.board import Board


class TileBoard(Board):
    def __init__(self, n, force_state=None):
        """
        Create a new Tile Board

        :param n: Number of Numbered Tiles in the Board
        :param force_state: list that will be used to populate the board instead of producing a random board.
        """
        board_dimension = math.floor(math.sqrt(n + 1))
        super(TileBoard, self).__init__(board_dimension, board_dimension)

        if force_state is not None:
            # Use Predefined Tile Order
            self.fill_board_from_list(self.board, force_state)
        else:
            self.generate_random_board(self.board)

    # noinspection PyUnresolvedReferences
    def __eq__(self, o: object) -> bool:
        """
        Compare two boards to see if they are equal. This is done by comparing their state_tuples.

        :param o: Comparison Object
        :return: Equality Boolean
        """
        return self.state_tuple() == o.state_tuple()

    def state_tuple(self) -> tuple:
        """
        Flatten the list of list representation of the board and cast it to a
        tuple. e.g. [[1,2,3],[4,None,5],[6,7,8]] becomes (1,2,3,4,None,5,6,7,8)

        :return:
        """
        tiles = list()
        for row in range(self.get_rows()):
            tiles.extend(self.board[row])
        return tuple(tiles)

    def get_actions(self) -> tuple:
        """
        Return list of possible moves. It is easier to
        think of the blank space as being moved rather than
        specifying which numbered tiles can be moved. We will
        return this as a list of lists where each sublist is an
        [row_delta,col_delta] list specifying the offset of the space
        from its current position relative to the current row and
        column. Values of the deltas can be -1, 0, or 1 indicating
        that the space should be moved: left, no move, or right and
        up, no move, or down

        :return:
        """

        actions = list()
        none_row, none_col = self.find_none(self.board)

        if none_col - 1 >= 0:
            # Left
            actions.append([0, -1])

        if none_col + 1 < self.get_cols():
            # Right
            actions.append([0, 1])

        if none_row - 1 >= 0:
            # Up
            actions.append([-1, 0])

        if none_row + 1 < self.get_rows():
            # Down
            actions.append([1, 0])

        return tuple(actions)

    def move(self, offset):
        """
        Given a valid action of the rom [row_delta, col_delta], return a
        new TileBoard that represents the state after the move.
        Example: [0,-1] would move the space one column to the left, exchanging the
        blank and 8.

        :param offset:
        :return:
        """

        new_board = copy.deepcopy(self)  # Create a deep copy of the object
        # make modifications to new_board

        none_row, none_col = self.find_none(self.board)
        new_board.place(none_row, none_col, new_board.get(none_row + offset[0], none_col + offset[1]))
        new_board.place(none_row + offset[0], none_col + offset[1], None)

        return new_board

    def solved(self) -> bool:
        """
        Return True if the puzzle is in a goal state (the blank must be in the
        center of an odd sized puzzle. You may define it as you wish for even sized
        puzzles).
        :return:
        """
        # Check None Position
        none_row, none_col = self.find_none(self.board)
        num_cols = self.get_cols()
        num_rows = self.get_rows()
        if not (none_row == math.floor(num_rows / 2) and none_col == math.floor(num_cols / 2)):
            # Blank not in correct position
            return False

        # Check Tile Order
        tiles = list(self.state_tuple())
        tiles.remove(None)  # Remove Gap, checked previously
        if not all(tiles[i] <= tiles[i + 1] for i in range(len(tiles) - 1)):
            # Not in the correct order
            return False

        return True

    def is_solvable(self) -> bool:
        state_tuple = self.state_tuple()
        inversion_order = 0
        for i in range(len(state_tuple)):
            tile_value = state_tuple[i]
            if tile_value is None:
                continue
            for j in range(i, len(state_tuple)):
                if state_tuple[j] is not None and tile_value > state_tuple[j]:
                    inversion_order += 1

        if self.get_cols() % 2 == 0:
            # Even Sized Board - Need to account for None (the row it is in)
            row, _ = self.find_none(self.board)
            inversion_order += row

        return inversion_order % 2 == 0

    def generate_random_board(self, board):
        tiles = list()
        tiles.extend(list(range(1, self.get_rows() * self.get_cols())))
        tiles.append(None)  # Empty Tile

        done = False

        while not done:
            random.shuffle(tiles)
            self.fill_board_from_list(board, tiles)
            done = self.is_solvable()

    def fill_board_from_list(self, board, tiles: list):
        num_rows = self.get_rows()

        for row in range(num_rows):
            for col in range(self.get_cols()):
                self.place(row, col, tiles[num_rows * row + col])

        return board

    @staticmethod
    def find_none(board) -> tuple:
        for row in range(len(board)):
            if None in board[row]:
                idx = board[row].index(None)
                return row, idx
        return -1, -1
