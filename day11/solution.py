with open("input.txt", "r") as f:
    seeds = [l.strip("\n") for l in f.readlines()]

octopus_grid = {}
for i, y in enumerate(seeds):
    row = []
    for j, x in enumerate(y):
        octopus_grid[(j, i)] = int(x)


def get_neighbors(coordinates):
    max_x = 9
    max_y = 9
    x, y = coordinates
    n = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
    ]
    neighbors = n.copy()

    for i in n:
        if i[0] > max_x or i[0] < 0 or i[1] > max_y or i[1] < 0:
            neighbors.remove(i)

    return [{k: octopus_grid[k] for k in octopus_grid if k in neighbors}]


flashes = 0
# incompatible with part 1 - set the number of steps to run to get that answer
for i in range(1000):
    print(f"Step {i + 1}")
    step_flashes = []
    # increase all energy by 1
    for o in octopus_grid:
        octopus_grid[o] += 1
    # loop
    while True:
        ## check for flashes (energy > 9) and track what flashed
        ## if flash, increase energy of neighbors by 1
        ## check for new flashes
        # repeat until no new flashes
        step_flash_count_curr_pass = 0
        for o in octopus_grid:
            if o not in step_flashes:
                if octopus_grid[o] > 9:
                    step_flashes.append(o)
                    flashes += 1
                    step_flash_count_curr_pass += 1
                    neighbors = get_neighbors(o)
                    for n in neighbors[0].keys():
                        octopus_grid[n] += 1
        if step_flash_count_curr_pass == 0:
            break
    # part 2 - did they all flash simultaneously? may need to bump up the number of steps
    if len(step_flashes) == len(octopus_grid):
        print("Everyone Flashes!")
    # for each octopus that flashed, reset to 0
    for o in octopus_grid:
        if octopus_grid[o] > 9:
            octopus_grid[o] = 0

print(flashes)

"""
this is a little janky. i got lazy and didn't fix the return type of get_neighbors, just subscripted around it.
do..until loops dont exist in python - so i had to use a while loop and break it. guessing there's a better way.
dealing with the grid as a dict of (x,y) -> energy worked really nicely.
"""
