## Day 2 Puzzle - Sonar Sweep ##
## https://adventofcode.com/2021/day/2 ##
from aocd.models import Puzzle
from aocd import submit

puzzle = Puzzle(year=2021, day=2)

## Part 1 ##
height = 0
depth = 0
input_str = puzzle.input_data.splitlines()
for movement in input_str:
    step = movement.split()
    if step[0].lower() == 'forward':
        height += int(step[1])
    elif step[0].lower() == 'down':
        depth += int(step[1])
    else:
        depth -= int(step[1])

myanswer = height*depth

## Part 2
height = 0
depth = 0
aim = 0
input_str = puzzle.input_data.splitlines()
for movement in input_str:
    step = movement.split()
    if step[0].lower() == 'forward':
        height += int(step[1])
        depth = depth+(aim*int(step[1]))
    elif step[0].lower() == 'down':
        aim += int(step[1])
    else:
        aim -= int(step[1])

myanswer = height*depth
# print(height, depth, aim)
# submit(myanswer, day =2, year=2021)