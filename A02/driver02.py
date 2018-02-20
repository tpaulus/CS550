"""
Driver for graph search problem
Created on Feb 12, 2018

@author: Tom Paulus
"""

import logging
import re
import time
from statistics import (mean, stdev)

from basicsearch_lib02.utilsdontneed import print_table
from npuzzle import NPuzzle
from problemsearch import graph_search
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)

TRIAL_SIZE = 31
TRIAL_BOARD_SIZE = 8
SOLUTION_METHODS = [BreadthFirst, DepthFirst, Manhattan]


def tic():
    """Return current time representation"""
    return time.time()


def tock(t):
    """Return time elapsed in sec since t where t is the output of tic()"""
    return time.time() - t


def driver():
    length_of_plan = dict()
    number_of_nodes = dict()
    elapsed_time = dict()

    for method in SOLUTION_METHODS:
        length_of_plan[method] = list()
        number_of_nodes[method] = list()
        elapsed_time[method] = list()

    for i in range(TRIAL_SIZE):
        logging.info('Starting Trial #%d', i)

        for method in SOLUTION_METHODS:
            logging.info('Solving puzzle via %s', method.__name__)
            puzzle = NPuzzle(TRIAL_BOARD_SIZE, g=method.g, h=method.h)

            start_time = tic()
            path, nodes_explored = graph_search(puzzle, debug=True, verbose=True)
            duration = tock(start_time)

            assert path is not None

            length_of_plan[method].append(len(path))
            number_of_nodes[method].append(nodes_explored)
            elapsed_time[method].append(duration)

            logging.info('Solved puzzle via %s in %d seconds', method.__name__, duration)

        logging.info('Finished Trial #%d', i)

    header = ["Method / Result   ",
              "Length of Plan (Mean/STDEV)",
              "Number of Nodes (Mean/STDEV)",
              "Elapsed Time (Mean/STDEV)"]
    rows = list()

    # Header Separator
    rows.append(['-' * (len(header[i]) + 1) for i in range(len(header))])

    # Table Values
    for method in SOLUTION_METHODS:
        rows.append([' '.join(re.sub('(?!^)([A-Z][a-z]+)', r' \1', method.__name__).split()),
                     '{:.3f} / {:.3f}'.format(mean(length_of_plan[method]), stdev(length_of_plan[method])),
                     '{:.3f} / {:.3f}'.format(mean(number_of_nodes[method]), stdev(number_of_nodes[method])),
                     '{:.3f} / {:.3f}'.format(mean(elapsed_time[method]), stdev(elapsed_time[method]))])

    print_table(rows, header=header, sep="\t| ")


if __name__ == '__main__':
    driver()
