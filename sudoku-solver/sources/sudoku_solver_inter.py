# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:17:57 2018

@author: cetoussa

Explanations (French) :
    Ce projet est un solveur de sudoku.
    Il consiste à construire une grille de cases avec des ensembles de 
    possibilités pour chaque case. Différents algorithmes sont ensuite exécutés
    afin de réduire le nombre de possibilités jusqu'à qu'il n'en reste plus
    qu'une par case, qui sera donc par défaut la solution pour cette case.
    Au début, on commence donc par créer la grille et par la remplir avec des
    valeurs de départ. On exécute ensuite le solveur.
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

class Case(set):
    """
    The basic element in a sudoku. A Case is a set of all possibilities for
    case. If the Case have only one element left in it, it should be considered
    as the solution for this case.
    
    A Case has two more attributes : _completed and _position (accessed with
    completed() and position())
    _completed is set when the case has only one element
    _position is a tuple with the line and row position of the case in the grid
    """
    
    def __init__(self, n, m):
        """
        Create an empty Case wich is not completed and at the position n, m
        """
        super().__init__()
        self._completed = False
        self._position = (n, m)
        
    
    def add(self, elem):
        """
        (Overwritten)
        Add an element in the set, but check if the Case is not completed first.
        This function should only be used when we populate a Case with his 
        default value.
        """
        pass
            
            
    def __repr__(self):
        """
        (Overwritten)
        Return different representation of the set, depending on the number of
        values in it
        """
        pass
        
        
    def __copy__(self):
        """
        (Overwritten)
        Allows a copy of a Case with the attribute
        """
        pass
    
    
    def __deepcopy__(self, memo):
        """
        (Overwritten)
        No deepcopy needed, we use the copy instead
        """
        return self.__copy__()
    
    
    def update(self, values):
        """
        (Overwritten)
        Same as add, but with a set of values
        """
        pass
        
        
    def set_as_default(self):
        """
        Set the case as completed, no turning back
        """
        self._completed = True
        
        
    def set_as_completed(self):
        """
        Set the case as completed, verifyif there is only one value left in the
        csae possibilities
        """
        if len(self) is 1 :
            self._completed = True
        
        
    def completed(self):
        """
        Return the state "completed" of the case
        """
        return self._completed
    
    
    def position(self) :
        """
        Return the position of the case in the grid as a tuple (line, row)
        """
        return self._position

        
class Line(list):
    """
    A Line is a list of Cases. It has two accessible attributes :
    completed_values : A set of completed values for this subset of cases
    position : The number of the line (or row, or block)
    """
    
    def __init__(self, cases, position):
        """
        Create a Line with a line number ans a list of cases
        """
        super().__init__()
        self.extend(cases)
        self.completed_values = set()
        self._position = position
        
        
    def __copy__(self):
        """
        When we copy a line, we must also copy the attributes
        """
        pass
        
        
    def __repr__(self):
        """
        A pretty representation of a line
        TODO : Change the representation when the line is a mini-line in a block
        """
        pass
    
    
    def completed_list(self):
        """
        Returns the completed values as a list
        """
        return [case for case in self if case.completed()]        

        
    def position(self):
        """
        Returns the number of the current line
        """
        return self._position


class Row(Line):
    """
    A row is typically a line in another direction. Only defined for convenience.
    """
    pass


class Block(Line):
    """
    Same as Row, a Block is a Line with a particular subset of Cases. Only
    defined for convenience.
    """
    pass


    
def block_index(n, m):
    """
    Compute a block index from a line and a row number
    """
    return (n//3)*3 + m//3
    

class Grid() :
    """
    A grid contains a list of Cases which can be indexed by their number or by
    the lines, rows, or blocks.
    """
    
    def __init__(self):
        """
        Creates the grid of empty cases. Then creates the lines, rows and blocks
        which reference the cases by different means
        """
        self.cases = [Case(i//9, i%9) for i in range(9*9)]
        self.lines = [Line([self.cases[i] for i in range(9*j, 9*j+9)], j) for j in range(9)]
        self.rows =  [Row([self.cases[i] for i in range(j, j+73, 9)], j) for j in range(9)]
        self.blocks = []
        
        # For the blocks, we use a matrix of the value 0,1,2 for defining the
        # "line and the row" of the block -> 00, 01, 02, 10, 11, 12, 20, 21, 22
        for i, j in itertools.product(range(3), repeat = 2) :
            sub_array = []
            for k in range(0, 19, 9):
                # Tricky index jumping to choose the good cases
                # Could be more efficient with "pandas"
                tmp = [i*27 + j*3 + k + l for l in range(3)]
                sub_array.extend(tmp)
                
            blocks = Block([self.cases[i] for i in sub_array], 3*i+j)
            self.blocks.append(blocks)
        
        
    def __repr__(self):
        """
        A pretty representation of the grid
        """
        pass
        
    
    def populate(self, array):
        """
        Fill the gris with the default values. The array must be a list of lists
        of value, like a 2D array. See the exemples at the beginning of the file.
        """
        pass
            
        
    def _put_at(self, value, n, m, default = False):
        """
        Write a value at the given position and set it as default. We must add
        te value to the completed values of the corresponding line, row and block
        TODO : The "default" parameter should be useless, all values set with 
        this function must be default values
        """
        pass
        
    
    def _remove_at(self, values, n, m, explanation = ""):
        """
        The most usefull function of this algorithm. Remove a set a values of a
        case given by its position. The parameter "explanation" can be given to
        display an indication for debug.
        """
        pass
    
    
    def is_valid(self):
        """
        This function checks if the grid is valid by checking if a value is 
        present more than once, this function is called after populate and
        is not very necessary after.
        """               
        return True
    
    
    def is_completed(self):
        """
        Check if all the cases are completed
        """
        return False
    
    
    def _complete_with_possibilities(self):
        """
        Fills the cases with all possibilities before solving the grid.
        The completed case are not affected by the update (overloaded in Case).
        """
        pass
        
        
    def solve(self):
        """
        Execute the solver
        """
        pass
        

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
        If this is true, so the other case in the subset can't have those values.
        
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
        results = [self._check_identical_cases(subset) for subset in 
                   self.lines + self.rows + self.blocks]
        
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
        we can act differently (TODO : event if dealing with the three cases 
        seems possible)
        """
        empty_operation = True
        
        return empty_operation

        
if __name__ == "__main__" :
    # Execute the solver on the two given examples
    grid = Grid()
    grid.populate(good_array)
    pprint.pprint(grid)
    grid.solve()
    
    grid2 = Grid()
    grid2.populate(good_array_2)
    pprint.pprint(grid2)
    grid2.solve()