#!/usr/bin/python

# TO EXECUTE THIS PROGRAM IN REPL.IT CLICK ON THE RUN BUTTON ABOVE

import sys
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--stones_per_player',
                    help='Number of random stones per player, default = 10', type=int, default=10)
parser.add_argument(
    '-b', '--board_size', help='Board size, for the standard sizes (9, 13, 19), the star points are shown, default = 19', type=int, default=19)
parser.add_argument('-border', '--place_border_stones',
                    help="By default, no stones will be placed on the border. Setting this option allows it.", action='store_true')
args = parser.parse_args()

stones_per_player = args.stones_per_player
board_size = args.board_size
place_border_stones = args.place_border_stones

# UNCOMMENT THIS TO CREATE YOUR OWN CONFIGURATION WITHOUT PASSING ARGUMENTS
# stones_per_player = 5
# board_size = 13
# place_border_stones = True

# The board is technically two spaces smaller if the boarder is not used
if args.place_border_stones:
    board_size_no_border = board_size
else:
    board_size_no_border = board_size - 2

# Sanity check if all stones fit on the board
if stones_per_player > board_size_no_border * board_size_no_border:
    raise Exception("The stones don't fit on the field")

# Draw random stones from the board
random_stones = np.random.choice(
    board_size_no_border * board_size_no_border, stones_per_player * 2, replace=False)

# Split the chosen stones between black and white
randomsB = random_stones[:stones_per_player]
randomsW = random_stones[stones_per_player:]

# Star positions for standard board sizes
stars = {9: [[2, 2], [2, 7], [4, 4], [7, 2], [7, 7]],
         13: [[3, 3], [3, 9], [6, 6], [9, 3], [9, 9]],
         19: [[3, 3], [3, 9], [3, 15], [9, 3], [9, 9], [9, 15], [15, 3], [15, 9], [15, 15]]}

# Iterate over the whole field
for i in range(board_size):
    for j in range(board_size):
        # Check if position is on border
        on_border = (i == 0 or j == 0 or i == board_size - 1 or j ==
                     board_size - 1) and not args.place_border_stones
        # Get an index from row and column
        if args.place_border_stones:
            index = i * board_size + j
        else:
            # Move the indices one up to center the board
            index = (i - 1) * board_size_no_border + (j - 1)

        # Check if the index is in the selected fields
        if index in randomsB and not on_border:
            sys.stdout.write('B ')
        elif index in randomsW and not on_border:
            sys.stdout.write('W ')
        else:
            # Check if the field is a star
            if board_size in stars and [i, j] in stars[board_size]:
                sys.stdout.write('* ')
            else:
                sys.stdout.write('. ')
    # New line
    sys.stdout.write('\n')
