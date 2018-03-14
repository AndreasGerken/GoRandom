# GoRandom

This python script generates a random initial board position for a variant of the board game [Go](https://en.wikipedia.org/wiki/Go_(game)) (igo, weiqi, baduk), which is comparable with [Chess960](https://de.wikipedia.org/wiki/Chess960).
The variant avoids the standard opening for more interesting and free games.

## Usage
The program can be executed online (https://repl.it/@AndreasGerken/GoRandom, clik on Run) or on your machine. Run it with the  python interpreter.
```
python go_random.py

. . . . . . . . . . . . . . . . . . .
. . . . . . . . . . W . . . . . W . .
. . . . . . . W . . . . . . . . . . .
. . . * . W . B . * . . . B . * . . W
. . . . . W . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . .
. . . . B . W . . . . . . . . . . . B
. . . . . . . . . . . . . . . . . . .
. . . . . . . . . W . . . . . . . . .
. B . * . . . W . * . . . . . * . . .
. . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . B
. . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . W B .
. . B * . . . . . * . . B . . * . . .
B . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . .
```

## Komi
Since the resulting positions are not equally good for both sides, the Komi (extra points for white) has to be negotiated. There are several options.

### Silent bid
Both players think of a Komi (positive or negative) for white and say it at the same time or write it down.
The player who named the lower number plays with white and the named Komi. If there is a tie, normal Nigiri could be used.

### Auction system
The players do an "auction" for the Komi and can outbid each other. When one player does not want to go higher, he accepts and plays with black.

### Pie rule
One player chooses komi, and the other player chooses whether to play black or white.


### Options
There are two options:
```
-s, --stones_per_player : Number of random stones per player, default = 10
-f, --field_size: Field size, for the standard sizes (9, 13, 19), the
                      star points are shown, default = 19
```
Example for 5 stones each on a 13x13 board:
```
python go_random.py -s 5 -f 13

. . . . . . . . . . . . .
. . . W . . . . . . . . .
. . . . . . . . . . . . .
. . B * . . W . . * . . .
. . . W . . . . . . . . .
. . . . . . . . W . . . .
. . . . . . * . . . . . .
. . . . B . . . . . . . B
. . . . . . . . . . . . .
. . . * W . . . . * . . .
. . . . . . B . . . . . .
. . . . . . . . . . . . .
. . . . . . . . . . . . B
```

### Dependencies

```
pip install --user numpy
```

## Credits:
I found the Idea for this variant in a [Reddit Thread](https://www.reddit.com/r/baduk/comments/7mc30y/ke_jies_comment_related_to_the_alphago_teaching/drt8lra/) and the Komi Variants on [Wikipedia](https://en.wikipedia.org/wiki/Komidashi)
