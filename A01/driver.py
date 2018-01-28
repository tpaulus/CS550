"""
Create function driver in driver.py that is invoked when driver.py is called from the
command line: python driver.py. It should print a board and allow you to play an 8
puzzle. If you want, you can have it ask you for the size of the board instead of
hardcoding it.
"""

from boardtypes import TileBoard


class Puzzle(object):
    def __init__(self, size=8, force_state=None):
        self.num_tiles = size
        self.board = TileBoard(self.num_tiles, force_state)

    def play(self):
        print("Hello! Let's play the %d tile game!" % self.num_tiles)
        while not self.board.solved():
            print(self.board)

            # Show Move Options
            options = self.board.get_actions()
            chosen_option = None
            prompt = "How would you like to move [row_delta,col_delta]? "

            print()
            print("\t".join(["%s. %s" % (letter, move) for (letter, move) in
                             zip([chr(l) for l in range(ord('a'), ord('a') + len(options))], options)]))

            while chosen_option not in options:
                letter_choice = input(prompt)

                # noinspection PyBroadException
                try:
                    chosen_option = options[ord(letter_choice) - ord('a')]
                except:
                    pass

                prompt = "Invalid Choice. Please try again: "

            # Perform Move
            self.board = self.board.move(chosen_option)

        # Puzzle has been solved!
        print("Nice Job! You Solved the Puzzle")


if __name__ == '__main__':
    size = 8
    Puzzle(size).play()
