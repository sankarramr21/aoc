## Day 3 Puzzle - Sonar Sweep ##
## https://adventofcode.com/2021/day/3 ##
from aocd.models import Puzzle
from aocd import submit

puzzle = Puzzle(year=2021, day=3)

def bitsresearch(incominglist, type, bit_position, bit_length):
    bit_construct = []
    if bit_position < bit_length:
        for i in incominglist:
            bit_construct.append(i[bit_position])

        count_1 = bit_construct.count('1')
        count_0 = bit_construct.count('0')
        """Logic to compare the bits by their position and 
        construct the ratings - most_common, least_common, Oxygen and CO2
        most_common <--> Oxygen and least_common <--> CO2 logics are same."""
        if count_1 >= count_0:
            most_common = str(1)
            least_common = str(0)
        else:
            most_common = str(0)
            least_common = str(1)

    if type == 1:
        return most_common
    else:
        return least_common

input_list = puzzle.input_data.splitlines()
# input_list = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
bit_length = len(input_list[0])

bit_position = 0
most_common = ''
least_common = ''
while bit_position < bit_length:
    most_common = most_common + bitsresearch(input_list,1,bit_position,bit_length)
    least_common = least_common + bitsresearch(input_list, 2,bit_position, bit_length)
    bit_position += 1

gamma = int(most_common,2)
epsilon = int(least_common,2)
myanswer = gamma*epsilon # Part 1 answer
# submit(myanswer, day =3, year=2021) #3969000

#Part 2 Solution

oxygen_rating = input_list.copy()
## To find oxygen rating
bit_position = 0
while bit_position < bit_length and len(oxygen_rating) > 1:
    temp_list = oxygen_rating.copy()
    oxygen_rating_level = bitsresearch(temp_list, 1,bit_position, bit_length)
    for i in temp_list:
        if i[bit_position] != oxygen_rating_level and not(len(oxygen_rating) == 1):
            oxygen_rating.remove(i)
    bit_position += 1

oxygen_rating_int = int(oxygen_rating[0], 2)

## To find CO2 rating
CO2_rating = input_list.copy()
bit_position = 0
while bit_position < bit_length and len(CO2_rating) > 1:
    temp_list = CO2_rating.copy()
    CO2_rating_level = bitsresearch(temp_list, 2,bit_position, bit_length)
    for i in temp_list:
        if i[bit_position] != CO2_rating_level and not(len(CO2_rating) == 1):
            CO2_rating.remove(i)
    bit_position += 1

CO2_rating_int = int(CO2_rating[0], 2)

myanswer = oxygen_rating_int * CO2_rating_int
# submit(myanswer, day =3, year=2021) #3977498

