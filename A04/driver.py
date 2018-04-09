from copy import deepcopy

from backtrack import backtracking_search
from constraint_prop import AC3
from csp_lib.sudoku import (Sudoku, easy1, harder1)


def is_solved(sudoku: Sudoku):
    for var in sudoku.curr_domains:
        if len(sudoku.curr_domains[var]) is not 1:
            return False
    return True


if __name__ == "__main__":
    # for puzzle in [easy1, harder1]:
    for puzzle in [easy1]:
        s = Sudoku(puzzle)  # construct a Sudoku problem
        print(s.display(s.infer_assignment()))

        ac3_s = deepcopy(s)
        AC3(ac3_s)
        if is_solved(ac3_s):
            print("Solved via AC3")
            print(ac3_s.display(ac3_s.infer_assignment()))
        else:
            print("Could not solve via AC3")
            print(ac3_s.display(ac3_s.infer_assignment()))
            print("Trying to solve via Back Track")
            # backtracking_search(s) # Non Implemented
            if is_solved(s):
                print("Solved via Back Track")
                print(s.display(s.infer_assignment()))
            else:
                print("Puzzle could not be solved")
