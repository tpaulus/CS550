from copy import deepcopy

from backtrack import backtracking_search
from constraint_prop import AC3
from csp_lib.sudoku import (Sudoku, easy1, harder1)

if __name__ == "__main__":
    # for puzzle in [easy1, harder1]:
    for puzzle in [easy1]:
        s = Sudoku(puzzle)  # construct a Sudoku problem
        print(s.display(s.infer_assignment()))

        if AC3(deepcopy(s)):
            print("Solved via AC3")
            print(s.display(s.infer_assignment()))

        else:
            print("Could not solve via AC3")

            if backtracking_search(s):
                print("Solved via Back Track")
                print(s.display(s.infer_assignment()))
            else:
                print("Could not be solved")
