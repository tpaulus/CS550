"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles of an odd length
    with solutions that contain the blank in the middle and numbers going
    from left to right in each row, e.g.:
        123
        4 5
        678
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

# For each of the following classes, create classmethods g and h
# with the following signatures
#       @classmethod
#       def g(cls, parentnode, action, childnode):
#               return appropriate g value
#       @classmethod
#        def h(cls, state):
#               return appropriate h value
from basicsearch_lib02.searchrep import Node
from basicsearch_lib02.tileboard import TileBoard


class BreadthFirst:
    """BredthFirst - breadthfirst search"""

    k = 0

    @classmethod
    def g(cls, parentnode: Node, action, childnode: Node):
        # Return Depth
        return len(childnode.path())

    @classmethod
    def h(cls, state):
        # Return Constant K (eg 0)
        return cls.k


class DepthFirst:
    """"DepthFirst - depth first search"""

    @classmethod
    def g(cls, parentnode: Node, action, childnode: Node):
        # Return Cost thus far
        raise len(childnode.path())

    @classmethod
    def h(cls, state: TileBoard):
        # Return Depth * -1
        raise NotImplemented


class Manhattan:
    """"Manhattan Block Distance heuristic"""

    @classmethod
    def g(cls, parentnode, action, childnode):
        return (len(childnode.path) + 1) * 2

    @classmethod
    def h(cls, state: TileBoard):
        distance = 0
        # for i in range(state):
        #     index = node.index(i + 1)
        #     row_diff = abs((i / MAT_SIZE) - (index / MAT_SIZE))
        #     col_diff = abs((i % MAT_SIZE) - (index % MAT_SIZE))
        #     count += (row_diff + col_diff)
        # index = node.index(-1)
        # row_diff = abs((PUZZLE_TYPE / MAT_SIZE) - (index / MAT_SIZE))
        # col_diff = abs((PUZZLE_TYPE % MAT_SIZE) - (index % MAT_SIZE))
        # count += (row_diff + col_diff)
        # return count
        return distance