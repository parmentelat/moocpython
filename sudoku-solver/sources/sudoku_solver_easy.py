#!/usr/bin/env python3
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

from samples import good_array, good_array_2


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
        new_case = type(self)(*self._position)
        new_case.update(self)
        new_case._completed = self._completed
        return new_case

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
        if len(self) is 1:
            self._completed = True

    def completed(self):
        """
        Return the state "completed" of the case
        """
        return self._completed

    def position(self):
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
        new_line = type(self)(self, self._position)
        new_line.completed_values = copy.copy(self.completed_values)
        return new_line

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
        pass

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
    return (n // 3) * 3 + m // 3


class Grid():
    """
    A grid contains a list of Cases which can be indexed by their number or by
    the lines, rows, or blocks.
    """

    def __init__(self):
        """
        Creates the grid of empty cases. Then creates the lines, rows and blocks
        which reference the cases by different means
        """
        self.cases = [Case(i // 9, i % 9) for i in range(9 * 9)]
        self.lines = [Line([self.cases[i] for i in range(
            9 * j, 9 * j + 9)], j) for j in range(9)]
        self.rows = [Row([self.cases[i] for i in range(j, j + 73, 9)], j)
                     for j in range(9)]
        self.blocks = []

        # For the blocks, we use a matrix of the value 0,1,2 for defining the
        # "line and the row" of the block -> 00, 01, 02, 10, 11, 12, 20, 21, 22
        for i, j in itertools.product(range(3), repeat=2):
            sub_array = []
            for k in range(0, 19, 9):
                # Tricky index jumping to choose the good cases
                # Could be more efficient with "pandas"
                tmp = [i * 27 + j * 3 + k + l for l in range(3)]
                sub_array.extend(tmp)

            blocks = Block([self.cases[i] for i in sub_array], 3 * i + j)
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

    def _put_at(self, value, n, m, default=False):
        """
        Write a value at the given position and set it as default. We must add
        te value to the completed values of the corresponding line, row and block
        TODO : The "default" parameter should be useless, all values set with 
        this function must be default values
        """
        pass

    def _remove_at(self, values, n, m, explanation=""):
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
        # Initialize some data
        empty_loop = False

        # Defines a maximal number of loop to solve the grid to avoid infinite loop
        counter = 0

        # Fills the non-completed cases with all possibilities
        self._complete_with_possibilities()

        # We loop until the grid is completed, or nothing was done in the
        # loop, or we reach the maximum number of loops
        # TODO : "_clean_case" should return an "empty_loop" too
        while ((not self.is_completed()) and
               (empty_loop is False) and
               (counter < 10)):

            # First reset the empty_loop variable
            empty_loop = True

            # We must call _clean_cases between each other functions to avoid
            # false resolution in the algorithm

            # Refer to each function for more details
            while not self._clean_cases():
                pass

            empty_loop &= self._check_identical_pair()

            while not self._clean_cases():
                pass

            empty_loop &= self._check_blocks_with_line_or_row_completed()

            while not self._clean_cases():
                pass

            empty_loop &= self._crossed_third_block()

            while not self._clean_cases():
                pass

            empty_loop &= self._square_algo()

            # Show to the user the number of loops executed and if something was
            # done in this loop (False if somethinf was done)
            print(counter, empty_loop)
            counter += 1

        if counter is 10:
            print("The solver is maybe stuck in a loop")

        elif not self.is_completed():
            print("The algorithm can't solve the grid")

        else:
            print("Solution found !")

        pprint.pprint(self)

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

    def _check_identical_cases(self, subset):
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

        # Loop over all the blocks
        for block in self.blocks:

            # Work on a copy of the blocks
            copy_block = copy.deepcopy(block)

            # First we build mini-lines and rows of the current block
            lines = []
            rows = []
            for index in range(3):
                lines.append(Line([copy_block[3 * index + i]
                                   for i in range(3)], index))
                rows.append(Row([copy_block[3 * i + index]
                                 for i in range(3)], index))

            # Defines a subfunction to execute repeatedely on lines and rows
            def _check_subset(subset, direction):

                # Copy the subset because we will modify them
                copy_subset = copy.copy(subset)

                #print(f"Copied subset {copy_subset}")

                # For each in the mini-line (or row)
                for cases in copy_subset:

                    # Check if the current line is completed
                    if all(case.completed() for case in cases):
                        subset.remove(cases)
                        #print(f"Subset remove {cases}")

                #print(f"Remaining subset {subset}")
                # If there is not two remaining lines, no need to go further,
                # the algorithm can't be applied
                if len(subset) == 2:
                    # Identify the two remaining lines
                    first_line, second_line = subset

                    # Defines a new subfunction to compute the occurences with
                    # a given line and a given set of completed values
                    def _compute_occurences(line, completed_values):

                        # The number of occurences is contained in a dict
                        nb_occurences = dict()

                        for case in line:
                            for value in case:
                                # Get the previous number of occurences and
                                # theirs location. If the key doesn't exist,
                                # create an empty tuple
                                cpt, places = nb_occurences.get(
                                    value, (0, list()))

                                # Add the case to the locations
                                places.append(case)

                                # Update the dict with one more location
                                nb_occurences[value] = (cpt + 1, places)

                        #print(f"Resolved occurences {nb_occurences}")

                        # Now we will check for each completed values if the
                        # value only appears one in the dict.
                        for completed_value in completed_values:

                            # Extract the number of occurences and the
                            # corresponding cases, empty if the value doesn't
                            # appear
                            occurence, places = nb_occurences.get(
                                completed_value, (0, []))

                            if occurence is 1:
                                empty_operation = False

                                # Extract the only case from the list of cases
                                case = places.pop()

                                # Should not be necessary, but keep it just in case
                                if not case.completed():

                                    # Here, we must remvove all but the good value
                                    values_to_remove = case - \
                                        set([completed_value])

                                    #print(f"BLOCK : Sets before removing {case} {case.position()} / {values_to_remove}")

                                    self._remove_at(
                                        values_to_remove, *case.position(), explanation="Block with completed line or row")

                                    #n, m = case.position()
                                    #print(f"BLOCK : Sets after removing {self.cases[n*9 + m]}")

                    # End of the subsubfunction

                    # First compute occurences on the first line with the
                    # completed values of the second

                    # We must seperate line and rows because we don't extract the
                    # completed values the same way
                    if direction == "line":
                        index, _ = second_line[0].position()
                        completed_values = self.lines[index].completed_values
                    else:
                        _, index = second_line[0].position()
                        completed_values = self.rows[index].completed_values

                    _compute_occurences(first_line, completed_values)

                    # Then compute occurences on the second line with the
                    # completed values of the first

                    if direction == "line":
                        index, _ = first_line[0].position()
                        completed_values = self.lines[index].completed_values
                    else:
                        _, index = first_line[0].position()
                        completed_values = self.rows[index].completed_values

                    _compute_occurences(second_line, completed_values)

            # End of the first subfunction, execute it on the lines, then on the
            # rows
            _check_subset(lines, "line")
            _check_subset(rows, "row")

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

        block_lines = [[self.blocks[i * 3 + j]
                        for j in range(3)] for i in range(3)]
        block_rows = [[self.blocks[j * 3 + i]
                       for j in range(3)] for i in range(3)]

        # First subfunction which will work on each subset defined just before
        def _check_subset(subset):
            for block_line in subset:

                # Even if there are redundant permutations of the three blocks
                # this is the only way I found to cover all cases easily
                for block1, block2, block3 in itertools.permutations(block_line, 3):

                    # Compute the completed values in common in the two blocks
                    intersection = block1.completed_values & block2.completed_values

                    if not intersection:
                        continue

                    #print(f"Intersection found : {intersection} with blocks @ position {block1.position()} and {block2.position()}")

                    for value in intersection:

                        # If the value is in the completed values of the third
                        # block, no need to continue
                        # TODO : can be improve by removing them in the first
                        # intersection ?
                        if value in block3.completed_values:
                            continue

                        # Second subfunction
                        # Look for the position of the values in block1 and
                        # block2
                        def _search_position(block):
                            for case in block:
                                # If the case is not completed, this is not the
                                # case we are looking for
                                if not case.completed():
                                    continue

                                # Else, check the value and store the position
                                if value in case:
                                    if subset is block_lines:
                                        position, _ = case.position()
                                    else:
                                        _, position = case.position()
                                    return position

                        # End of the subsubfunction

                        # Compute the position of the value in the two blocks
                        position1 = _search_position(block1)
                        position2 = _search_position(block2)

                        # Since the position returned is a abolute position in
                        # the grid, we must compute position3 depending on it
                        if position1 in {0, 1, 2}:
                            position3 = (
                                {0, 1, 2} - {position1, position2}).pop()
                        elif position1 in {3, 4, 5}:
                            position3 = (
                                {3, 4, 5} - {position1, position2}).pop()
                        elif position1 in {6, 7, 8}:
                            position3 = (
                                {6, 7, 8} - {position1, position2}).pop()

                        #print(f"CROSS : Position of value {value} in block1, block2, block3 : {position1}, {position2}, {position3}")

                        # Now select the cases we will check in the third block
                        selected_cases = list()
                        for case in block3:
                            # If the case is completed, exclude it
                            if case.completed():
                                continue

                            # We must a difference between lines and rows
                            if subset is block_lines:
                                position_line, _ = case.position()

                                if position_line != position3:
                                    continue

                            else:
                                _, position_row = case.position()

                                if position_row != position3:
                                    continue

                            # The cases which are not at the good position have
                            # been "escaped"
                            selected_cases.append(case)

                        # No need to go further if the selection is empty (the
                        # mini-line is already completed
                        # TODO : I think this line is useless?
                        if not selected_cases:
                            continue

                        #print(f"CROSS : Selected cases to scan : {[selected_case.position() for selected_case in selected_cases]}")

                        # Then we must separate each case, depending on the
                        # number of non-completed cases in the mini-line
                        # For each case, we should remove the solutions found
                        # from others case but we will let the "_clean_case"
                        # function do its work
                        # TODO : Only the third case should always work

                        # If there is only one case available for the current
                        # value, so this is the only solution for this case
                        if len(selected_cases) is 1:
                            selected_case = selected_cases.pop()

                            # Remove all others values
                            values_to_remove = selected_case - intersection
                            empty_operation = False
                            self._remove_at(
                                values_to_remove, *selected_case.position(), explanation="Crossing blocks")

                        # If there are two cases non completed
                        elif len(selected_cases) is 2:
                            case1 = selected_cases.pop()
                            case2 = selected_cases.pop()

                            #print(f"CROSS : Two cases to scan {case1} and {case2}, with value {value}")

                            # If the current value is not in the first case,
                            # keep it only in the second one
                            if value not in case2:
                                values_to_remove = case1 - {value}
                                self._remove_at(
                                    values_to_remove, *case1.position(), explanation="Crossing blocks")
                                #print(f"CROSS : Removing values {values_to_remove} from case at {case1.position()}")
                            elif value not in case1:
                                values_to_remove = case2 - {value}
                                self._remove_at(
                                    values_to_remove, *case2.position(), explanation="Crossing blocks")
                                #print(f"CROSS : Removing values {values_to_remove} from case at {case2.position()}")

                            empty_operation = False

                        # At least, if the three cases are not completed
                        elif len(selected_cases) is 3:
                            case1 = selected_cases.pop()
                            case2 = selected_cases.pop()
                            case3 = selected_cases.pop()

                            #print(f"CROSS : Concerned cases : {case1}, {case2}, {case3}")

                            # If the value only appears in one case, keep it as
                            # the solution for this case
                            if (value not in case2) and (value not in case3):
                                values_to_remove = case1 - {value}
                                self._remove_at(
                                    values_to_remove, *case1.position(), explanation="Crossing blocks")
                            elif (value not in case1) and (value not in case3):
                                values_to_remove = case2 - {value}
                                self._remove_at(
                                    values_to_remove, *case2.position(), explanation="Crossing blocks")
                            elif (value not in case1) and (value not in case2):
                                values_to_remove = case3 - {value}
                                self._remove_at(
                                    values_to_remove, *case3.position(), explanation="Crossing blocks")

                            empty_operation = False

        # End of the subfunction

        # Now apply it on each subset
        _check_subset(block_lines)
        _check_subset(block_rows)

        return empty_operation


if __name__ == "__main__":
    # Execute the solver on the two given examples
    grid = Grid()
    grid.populate(good_array)
    pprint.pprint(grid)
    grid.solve()

    grid2 = Grid()
    grid2.populate(good_array_2)
    pprint.pprint(grid2)
    grid2.solve()
