#!/usr/bin/python
import sys
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stones_per_player",
                    help="Number of random stones per player, default = 10", type=int, default=10)
parser.add_argument(
    "-f", "--field_size", help="Field size, for the standard sizes (9, 13, 19), the star points are shown, default = 19", type=int, default=19)
args = parser.parse_args()


stones_per_player = args.stones_per_player
field_size = args.field_size


if stones_per_player > field_size * field_size:
    raise Exception("The stones don't fit on the field")

random_stones = np.random.choice(
    field_size * field_size, stones_per_player * 2)
randomsB = random_stones[:stones_per_player]
randomsW = random_stones[stones_per_player:]

stars = {9: [[2, 2], [2, 7], [4, 4], [7, 2], [7, 7]],
         13: [[3, 3], [3, 9], [6, 6], [9, 3], [9, 9]],
         19: [[3, 3], [3, 9], [3, 15], [9, 3], [9, 9], [9, 15], [15, 3], [15, 9], [15, 15]]}

# Iterate over the whole field
for i in range(field_size):
    for j in range(field_size):

        # Get an index from row and column
        index = i * field_size + j

        # Check if the index is in the selected fields
        if index in randomsB:
            sys.stdout.write('B')
        elif index in randomsW:
            sys.stdout.write('W')
        else:
            # Check if the field is a star
            if field_size in stars and [i, j] in stars[field_size]:
                sys.stdout.write('*')
            else:
                sys.stdout.write('.')
    # New line
    sys.stdout.write('\n')
