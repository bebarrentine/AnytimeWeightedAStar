#Main program for A* search

import argparse
import math
import sys
from OpenList import *
import puzzle


def search(initial_state, goal):  
    
    open_list = PriorityQueue()
    closed_list = {} #closed_list is a dictionary

    moves = (puzzle.move_right, puzzle.move_down,puzzle.move_left, puzzle.move_up)

    open_list.add_state(initial_state)

    while len(open_list) > 0:  # Search until your open_list is empty
        n = open_list.pop_state()
      
        # Add node to closed list or increment count
       
        closed_list[n] = n
  
        
        if n == goal:  # return node and stats if goal
            
            return n

        children = []
        for move in moves:  # generate valid children
            try:
                children.append(move(n))
            except ValueError:
                continue

        for child in children:  # calculate children heuristics
            child.calculate_h()

        for child in children:  # add valid children to open list
            if child in closed_list:
                if closed_list[child].c>child.c:
                    del closed_list[child]
                    open_list.add_state(child)
            else:
                open_list.add_state(child)

#Main driver for program   
def main(width, size, state,heuristic):    
    # Pass parameters to puzzle module
    puzzle.settings_init(width,size,heuristic)
    
    # Define puzzle goal state
    gboard=list(x for x in range(1,size))
    gboard.append(0)
    goal=puzzle.State(gboard,None)
    
    # Define initial state
    iboard=[int(x) for x in state]
    initial_state = puzzle.State(iboard, None)
    
    # Determine your puzzle is solvable or not
    try:
        if initial_state.is_solvable() is False:
            raise ValueError("Initial state:",str(initial_state),"is not solvable") 
    except ValueError as err:
        print (state)
        print  (err)
        sys.exit(1)
    initial_state.calculate_h()
    solution=None

    # Run search.
    while solution is None:
        try:
            solution=search(initial_state, goal)
        except ValueError:

            sys.exit(1)

    # Bulid path from initial state to goal state
    ptr=solution
    path=[]
    while ptr is not None:
        path.append(str(ptr))
        ptr=ptr.parent
    path.reverse()

    print (path)
    
    
#set parameters 

def user_input():
    # Get user input
    parser = argparse.ArgumentParser(
        description="A program to solve sliding tile puzzles",
        epilog="example: python A_star.py -w 3 --heuristic manhattan -s 8 2 1 5 4 0 3 7 6  ")
    parser.add_argument("-w, --width",
                        nargs="?",
                        type=int,
                        default=3,
                        dest="width")
    parser.add_argument("--heuristic",
                        nargs="?",
                        type=str,
                        default="manhattan",
                        dest="heuristic")
    parser.add_argument("-s, --state",
                        nargs="*",
                        help="initial state",
                        type=str,
                        dest="state")
    args = parser.parse_args()

    # call main with user input
    size=args.width*args.width
    main(args.width, size,args.state, args.heuristic)


if __name__ == "__main__":
    user_input()


