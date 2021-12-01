# link: https://adventofcode.com/2021/day/1

# As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

# For example, suppose you had the following report:

# 199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263

# This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

# The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

# To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

from typing import List

sample = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input_file = open("./input.txt", 'r')
depth_measurements = [int(i) for i in input_file.readlines()]

def count_increases(depth_measurements: List[int]) -> int:
    increases = 0

    for i in range(1, len(depth_measurements)):
        if depth_measurements[i] > depth_measurements[i-1]:
            increases += 1

    return increases

assert count_increases(sample) == 7
print(count_increases(depth_measurements))