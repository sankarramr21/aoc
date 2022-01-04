## Day 1 Puzzle - Sonar Sweep ##
## https://adventofcode.com/2021/day/1 ##
from aocd.models import Puzzle
from aocd import submit

puzzle = Puzzle(year=2021, day=1)

## Part 1 response
answer = 0
input_list = puzzle.input_data.split()
for index, i in  enumerate(input_list[1:]):
    if int(i) > int(input_list[index]):
        answer += 1

# submit(part1answer, day =1, year=2021)

## Part 2 response
new_input_list = []
input_list = puzzle.input_data.split()
for index, i in  enumerate(input_list):
    if index >= 2:
        new_input_list.append(int(input_list[index])+int(input_list[index-1])+int(input_list[index-2]))
print(new_input_list)
answer = 0
for index, i in  enumerate(new_input_list[1:]):
    if i >  new_input_list[index]:
        answer += 1

# submit(answer, day =1, year=2021)

