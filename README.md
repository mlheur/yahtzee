```
$ python3 yahtzee.py
scorecard: P1
=====================
A | Ones       |    0
B | Twos       |    0
C | Threes     |    0
D | Fours      |    0
E | Fives      |    0
F | Sixes      |    0
--|------------|-----
= | Upper      |    0
+ | Bonus      |    0
--|------------|-----
G | 3-Kind     |    0
H | 4-Kind     |    0
I | FullHouse  |    0
J | Short      |    0
K | Long       |    0
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |    0
--|------------|-----
==| Total      |    0
=====================
P1: 1st roll | .2. .5. .5. .1. .4. > ?
### INSTRUCTIONS ###
> q to quit
> v to view the scorecard
> r to roll free dice    | .#.
> 1..5 to hold that die  | [#]
> A..F score dice in the upper half
> G..M score dice in lower half
P1: 1st roll | .2. .5. .5. .1. .4. > 23
P1: 1st roll | .2. [5] [5] .1. .4. > r
P1: 2nd roll | .1. [5] [5] .4. .6. > r
P1: 3rd roll | .4. .5. .5. .4. .5. > I
scorecard: P1
=====================
A | Ones       |    0
B | Twos       |    0
C | Threes     |    0
D | Fours      |    0
E | Fives      |    0
F | Sixes      |    0
--|------------|-----
= | Upper      |    0
+ | Bonus      |    0
--|------------|-----
G | 3-Kind     |    0
H | 4-Kind     |    0
- | FullHouse  |   25
J | Short      |    0
K | Long       |    0
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |   25
--|------------|-----
==| Total      |   25
=====================
P1: 1st roll | .1. .3. .2. .4. .2. > 35r
P1: 2nd roll | .6. .6. [2] .6. [2] > 12345
P1: 2nd roll | [6] [6] .2. [6] .2. > r
P1: 3rd roll | .6. .6. .4. .6. .5. > G
scorecard: P1
=====================
A | Ones       |    0
B | Twos       |    0
C | Threes     |    0
D | Fours      |    0
E | Fives      |    0
F | Sixes      |    0
--|------------|-----
= | Upper      |    0
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
H | 4-Kind     |    0
- | FullHouse  |   25
J | Short      |    0
K | Long       |    0
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |   52
--|------------|-----
==| Total      |   52
=====================
P1: 1st roll | .2. .1. .5. .4. .3. > K
scorecard: P1
=====================
A | Ones       |    0
B | Twos       |    0
C | Threes     |    0
D | Fours      |    0
E | Fives      |    0
F | Sixes      |    0
--|------------|-----
= | Upper      |    0
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
H | 4-Kind     |    0
- | FullHouse  |   25
J | Short      |    0
- | Long       |   40
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |   92
--|------------|-----
==| Total      |   92
=====================
P1: 1st roll | .5. .4. .5. .1. .6. > 13
P1: 1st roll | [5] .4. [5] .1. .6. > r
P1: 2nd roll | [5] .3. [5] .5. .2. > 4
P1: 2nd roll | [5] .3. [5] [5] .2. > r
P1: 3rd roll | .5. .3. .5. .5. .4. > E
scorecard: P1
=====================
A | Ones       |    0
B | Twos       |    0
C | Threes     |    0
D | Fours      |    0
- | Fives      |   15
F | Sixes      |    0
--|------------|-----
= | Upper      |   15
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
H | 4-Kind     |    0
- | FullHouse  |   25
J | Short      |    0
- | Long       |   40
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |   92
--|------------|-----
==| Total      |  107
=====================
P1: 1st roll | .3. .2. .3. .1. .6. > 13
P1: 1st roll | [3] .2. [3] .1. .6. > r
P1: 2nd roll | [3] .3. [3] .6. .2. > 2
P1: 2nd roll | [3] [3] [3] .6. .2. > r
P1: 3rd roll | .3. .3. .3. .1. .4. > C
scorecard: P1
=====================
A | Ones       |    0
B | Twos       |    0
- | Threes     |    9
D | Fours      |    0
- | Fives      |   15
F | Sixes      |    0
--|------------|-----
= | Upper      |   24
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
H | 4-Kind     |    0
- | FullHouse  |   25
J | Short      |    0
- | Long       |   40
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |   92
--|------------|-----
==| Total      |  116
=====================
P1: 1st roll | .6. .3. .5. .6. .1. > 14
P1: 1st roll | [6] .3. .5. [6] .1. > r
P1: 2nd roll | [6] .2. .4. [6] .6. > 5
P1: 2nd roll | [6] .2. .4. [6] [6] > r
P1: 3rd roll | .6. .6. .2. .6. .6. > F
scorecard: P1
=====================
A | Ones       |    0
B | Twos       |    0
- | Threes     |    9
D | Fours      |    0
- | Fives      |   15
- | Sixes      |   24
--|------------|-----
= | Upper      |   48
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
H | 4-Kind     |    0
- | FullHouse  |   25
J | Short      |    0
- | Long       |   40
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |   92
--|------------|-----
==| Total      |  140
=====================
P1: 1st roll | .6. .6. .5. .4. .5. > 12
P1: 1st roll | [6] [6] .5. .4. .5. > r
P1: 2nd roll | [6] [6] .2. .6. .4. > 4
P1: 2nd roll | [6] [6] .2. [6] .4. > r
P1: 3rd roll | .6. .6. .6. .6. .5. > H
scorecard: P1
=====================
A | Ones       |    0
B | Twos       |    0
- | Threes     |    9
D | Fours      |    0
- | Fives      |   15
- | Sixes      |   24
--|------------|-----
= | Upper      |   48
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
- | 4-Kind     |   29
- | FullHouse  |   25
J | Short      |    0
- | Long       |   40
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |  121
--|------------|-----
==| Total      |  169
=====================
P1: 1st roll | .2. .3. .5. .5. .1. > 1
P1: 1st roll | [2] .3. .5. .5. .1. > r
P1: 2nd roll | [2] .5. .3. .2. .3. > 4
P1: 2nd roll | [2] .5. .3. [2] .3. > r
P1: 3rd roll | .2. .4. .5. .2. .4. > B
scorecard: P1
=====================
A | Ones       |    0
- | Twos       |    4
- | Threes     |    9
D | Fours      |    0
- | Fives      |   15
- | Sixes      |   24
--|------------|-----
= | Upper      |   52
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
- | 4-Kind     |   29
- | FullHouse  |   25
J | Short      |    0
- | Long       |   40
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |  121
--|------------|-----
==| Total      |  173
=====================
P1: 1st roll | .3. .6. .2. .5. .4. > 5
P1: 1st roll | .3. .6. .2. .5. [4] > J
scorecard: P1
=====================
A | Ones       |    0
- | Twos       |    4
- | Threes     |    9
D | Fours      |    0
- | Fives      |   15
- | Sixes      |   24
--|------------|-----
= | Upper      |   52
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
- | 4-Kind     |   29
- | FullHouse  |   25
- | Short      |   30
- | Long       |   40
L | Yahtzee    |    0
M | Chance     |    0
--|------------|-----
= | Lower      |  151
--|------------|-----
==| Total      |  203
=====================
P1: 1st roll | .2. .2. .4. .2. .4. > 35
P1: 1st roll | .2. .2. [4] .2. [4] > r
P1: 2nd roll | .6. .1. [4] .2. [4] > r
P1: 3rd roll | .6. .6. .4. .5. .4. > M
scorecard: P1
=====================
A | Ones       |    0
- | Twos       |    4
- | Threes     |    9
D | Fours      |    0
- | Fives      |   15
- | Sixes      |   24
--|------------|-----
= | Upper      |   52
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
- | 4-Kind     |   29
- | FullHouse  |   25
- | Short      |   30
- | Long       |   40
L | Yahtzee    |    0
- | Chance     |   25
--|------------|-----
= | Lower      |  176
--|------------|-----
==| Total      |  228
=====================
P1: 1st roll | .1. .2. .3. .2. .6. > 1
P1: 1st roll | [1] .2. .3. .2. .6. > r
P1: 2nd roll | [1] .2. .4. .6. .3. > r
P1: 3rd roll | .1. .2. .4. .1. .6. > A
scorecard: P1
=====================
- | Ones       |    2
- | Twos       |    4
- | Threes     |    9
D | Fours      |    0
- | Fives      |   15
- | Sixes      |   24
--|------------|-----
= | Upper      |   54
+ | Bonus      |    0
--|------------|-----
- | 3-Kind     |   27
- | 4-Kind     |   29
- | FullHouse  |   25
- | Short      |   30
- | Long       |   40
L | Yahtzee    |    0
- | Chance     |   25
--|------------|-----
= | Lower      |  176
--|------------|-----
==| Total      |  230
=====================
P1: 1st roll | .2. .4. .5. .5. .3. > 2
P1: 1st roll | .2. [4] .5. .5. .3. > r
P1: 2nd roll | .3. [4] .5. .5. .1. > r
P1: 3rd roll | .5. .4. .4. .2. .4. > D
scorecard: P1
=====================
- | Ones       |    2
- | Twos       |    4
- | Threes     |    9
- | Fours      |   12
- | Fives      |   15
- | Sixes      |   24
--|------------|-----
= | Upper      |   66
+ | Bonus      |   35
--|------------|-----
- | 3-Kind     |   27
- | 4-Kind     |   29
- | FullHouse  |   25
- | Short      |   30
- | Long       |   40
L | Yahtzee    |    0
- | Chance     |   25
--|------------|-----
= | Lower      |  176
--|------------|-----
==| Total      |  277
=====================
P1: 1st roll | .1. .5. .3. .4. .4. > 45
P1: 1st roll | .1. .5. .3. [4] [4] > r
P1: 2nd roll | .1. .1. .1. [4] [4] > 12345
P1: 2nd roll | [1] [1] [1] .4. .4. > r
P1: 3rd roll | .1. .1. .1. .1. .3. > L
scorecard: P1
=====================
- | Ones       |    2
- | Twos       |    4
- | Threes     |    9
- | Fours      |   12
- | Fives      |   15
- | Sixes      |   24
--|------------|-----
= | Upper      |   66
+ | Bonus      |   35
--|------------|-----
- | 3-Kind     |   27
- | 4-Kind     |   29
- | FullHouse  |   25
- | Short      |   30
- | Long       |   40
- | Yahtzee    |   -0
- | Chance     |   25
--|------------|-----
= | Lower      |  176
--|------------|-----
==| Total      |  277
=====================
```
