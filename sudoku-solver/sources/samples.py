"""
define a few sample grids, and a main function 
5ithat solves (some of) them from the command line
"""

sample1 = [
    [None,None,None,  2   ,None,None,  None,None,None],
    [None,None,None,  None,None,None,  None,9   ,1   ],
    [None,None,7   ,  9   ,None,None,  8   ,4   ,None],
    
    [None,None,None,  5   ,6   ,None,  7   ,None,None],
    [None,None,8   ,  None,4   ,None,  None,None,None],
    [None,1   ,None,  None,None,3   ,  None,None,6   ],
    
    [3   ,5   ,None,  None,None,None,  9   ,None,None],
    [None,2   ,None,  None,None,5   ,  None,None,None],
    [None,4   ,None,  7   ,None,None,  3   ,None,None],
]


sample2 = [
    [1   ,None,7   ,  None,None,None,  None,None,9   ],
    [None,None,None,  2   ,None,None,  None,None,6   ],
    [None,None,None,  None,4   ,None,  8   ,3   ,None],

    [None,None,None,  None,None,5   ,  None,None,None],
    [4   ,None,None,  None,7   ,3   ,  2   ,None,None],
    [6   ,None,None,  None,2   ,None,  9   ,None,8   ],

    [7   ,3   ,None,  None,None,None,  None,None,1   ],
    [None,None,None,  7   ,3   ,None,  None,None,None],
    [None,None,9   ,  5   ,None,None,  None,2   ,None],
]

import pprint


def main(grid_class):
    import argparse
    parser = argparse.ArgumentParser()
    # quick and dirty
    parser.add_argument("-1", dest='sample1', action='store_true',
                        help="run 1st sample")
    parser.add_argument("-2", dest='sample2', action='store_true',
                        help="run 2nd sample")
    args = parser.parse_args()

    # no option provided : run all
    if not (args.sample1 or args.sample2):
        args.sample1 = args.sample2 = True

    if args.sample1:
        grid = grid_class()
        grid.populate(sample1)
        pprint.pprint(grid)
        grid.solve()

    if args.sample2:
        grid = grid_class()
        grid.populate(sample2)
        pprint.pprint(grid)
        grid.solve()

        

