# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:17:57 2018

@author: cetoussa

Explanations (French) :
    Ce projet est un solver de sudoku.
"""

import pprint
import copy
import itertools

# Here are two grid you can use to test your algorithm
# The first one can be easier to solve

good_array = [[None,None,None,2   ,None,None,None,None,None],
              [None,None,None,None,None,None,None,9   ,1   ],
              [None,None,7   ,9   ,None,None,8   ,4   ,None],
              [None,None,None,5   ,6   ,None,7   ,None,None],
              [None,None,8   ,None,4   ,None,None,None,None],
              [None,1   ,None,None,None,3   ,None,None,6   ],
              [3   ,5   ,None,None,None,None,9   ,None,None],
              [None,2   ,None,None,None,5   ,None,None,None],
              [None,4   ,None,7   ,None,None,3   ,None,None]]


good_array_2 = [[1   ,None,7   ,None,None,None,None,None,9   ],
                [None,None,None,2   ,None,None,None,None,6   ],
                [None,None,None,None,4   ,None,8   ,3   ,None],
                [None,None,None,None,None,5   ,None,None,None],
                [4   ,None,None,None,7   ,3   ,2   ,None,None],
                [6   ,None,None,None,2   ,None,9   ,None,8   ],
                [7   ,3   ,None,None,None,None,None,None,1   ],
                [None,None,None,7   ,3   ,None,None,None,None],
                [None,None,9   ,5   ,None,None,None,2   ,None]]

class Grid() :
    
    def __init__(self):
        pass
        
        
    def solve(self):
        """
        Execute the solver
        """
        
    def _clean_cases(self):
        """
        Main mean of solving the grid. We look for each cases and build a set 
        of already completed values, extracted from the line, the row and the 
        block the case is in.
        [X, , |X,X,X|X, ,X]
        [X, , | ,X,X|X, ,X]
        [X,X, |X, ,X| ,X,X]
        -------------------
        [X, ,X|X,X,X|X,X,X]}
        [X, ,X| , , |X,A,X] <- completed_values of the line
        [X,X, |X,X,X|X, ,X]} <- completed_ values of the block
        -------------------
        [X,X, | ,X, |X, ,X]
        [X, ,X| , ,X| ,X,X]
        [ , ,X|X, ,X|X, ,X]
                       ^
                       completed_values of the row
        A = A - (completed_values of line, row and block)
        """
        empty_operation = True
                    
        return empty_operation
    
    
    def _check_identical_cases(self, subset) :
        """
        For this one, we check if two cases in a subset have the two same values.
        If this is true, so the other cases in the subset can't have those values.
        
        [{1,2}, , |X,{1,2},X|X, ,X]
        The cases 1 and 5 have the same set of possibilities, so the other cases
        of the line can't have those possibilities. So we eliminate them from
        their set.
        
        TODO : could be extend to check if three case have the same set of three
        values or four case, the same set of four values and so far, but this
        seems difficult to implement. In most case, only checking pairs is enough.
        """
        empty_operation = True
                    
        return empty_operation
    
    
    def _check_identical_pair(self):
        """
        Function called to check pairs of cases in all the subsets
        """
        # results is a list of boolean values holding the "empty loop" result
        results = [True]
        
        # Call the previous function on a list of subsets
        
        # Return True if all results are empty
        return all(results)
        
    
    def _square_algo(self):
        """
        This part of the algorithm is easier to understand
        
        [X, , |X,X,X|X, ,X]
        [X, , | ,X,X|X, ,X]
        [X,X, |X, ,X| ,X,X]
        -------------------
        [X, ,X|X,X,X|X,X,X]
        [X, ,X| , , |X,X,X]
        [X,X, |X,X,X|X, ,1] <- Take this value for example
        -------------------
        [C,C, | ,C, |A,A,B] <- The value "1" can't be in cases B, so it must
        [X, ,X| , ,X|X,X,B]    be in one of the cases A, so all the rest of line
        [ , ,X|X, ,X|X,X,B]    can't contain this value. Remove the value "1"
                               from the cases C
        """
        empty_operation = True
        
        return empty_operation
        
    
    def _check_blocks_with_line_or_row_completed(self):
        """
        This one is more difficult. If a block is partially completed with one
        of its inner line or row completed; and the two remaining lines (or rows)
        contain exclusive values (with an extended set of values from the other 
        line (or row)), we can directly solve the value only present one.
        
        [1, , | ,     ,     |3, ,9]
        [X, , |X,  X  ,  X  |X, ,X]
        [X,X, |X,{1,6},{6,7}| ,X,X]
        In the middle block, the first line can't contain {1, 3 or 9}, so it can
        only be in the third line. We compute the occurences of each values of
        possibilities {1,6,7}. If one of them only appears one and is in the 
        "extended" set of value to exclude, it is the solution for this case.
        -> case {1,6} becomes 1
        """
        empty_operation = True
        
        return empty_operation
    
    
    def _crossed_third_block(self):
        """
        We now work on a subset of three blocks in line or in row.
        If two of the three blocks have some completed values in common (and 
        that the third has not)
        
        [X, , | , , |3, ,9] <- The value 3 appears in line 1 and 3 but not in 
        [X, , |X,A,B|X, ,X]    line 2
        [3,6, |X, ,X| ,X,X]
        
        We check the cases A and B, if the value 3 appears only in case A, so
        this is the solution for A. If it appears in A and B, we can't make
        any conclusion.
        
        Depending on the number of free non-completed cases in the middle block
        We can act differently (TODO : event if dealing with the three cases 
        seems possible)
        """
        empty_operation = True
        
        return empty_operation

        
if __name__ == "__main__" :
    # Execute the solver on the two given examples
    grid = Grid()
    #grid.populate(good_array)
    #pprint.pprint(grid)
    grid.solve()
    
    grid2 = Grid()
    #grid2.populate(good_array_2)
    #pprint.pprint(grid2)
    grid2.solve()