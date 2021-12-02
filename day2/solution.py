from typing import List, Tuple

with open("input.txt", "r") as f:
    moves = [line.strip("\n") for line in f.readlines()]

sample = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

# part 1
def calculate_position(moves: List[str]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0

    for move in moves:
        move = move.split(" ")
        direction = move[0]
        distance = int(move[1])

        if direction == "up":
            depth -= distance
        elif direction == "down":
            depth += distance
        elif direction == "forward":
            horizontal += distance

    return horizontal, depth

#part 2 - adding aim
def calculate_position_with_aim(moves: List[str]) -> Tuple[int, int]:
    horizontal = 0
    depth = 0
    aim = 0

    for move in moves:
        move = move.split(" ")
        direction = move[0]
        distance = int(move[1])

        if direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance
        elif direction == "forward":
            horizontal += distance
            depth += aim * distance

    return horizontal, depth

horizontal, depth = calculate_position(moves)
print(horizontal * depth)

horizontal, depth = calculate_position_with_aim(moves)
print(horizontal * depth)