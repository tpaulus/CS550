'''
Constraint propagation
'''
from csp_lib.csp import CSP


def AC3(csp: CSP, queue=None, removals=None):
    """AC3 constraint propagation
    
    """
    queue = [(i, j) for i in csp.domains for j in csp.neighbors[i]]

    while queue:
        i, j = queue.pop()  # Cell in Puzzle, Set Neighbors of Cell
        if revise(csp, i, j):
            if csp.domains[i] is None:
                return False
            for x in csp.neighbors[i]:
                if x not in csp.neighbors[j]:
                    queue.append((x, i))
        return True

    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    cps.j[x] is the j of variable x


def revise(csp: CSP, i, j):
    revised = False
    for x in csp.domains[i]:
        if not any([csp.constraints(i, x, j, y) for y in csp.domains[j]]):
            if type(csp.domains) is not list:
                csp.domains[i] = list(csp.domains[i])
            csp.domains[i].remove(x)
            revised = True
    return revised
