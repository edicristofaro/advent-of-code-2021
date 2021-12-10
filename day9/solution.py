from functools import reduce

lines = []

with open("input.txt") as f:
    for line in f:
        lines.append(line.strip("\n"))

#part 1
def get_surrounding_point_values(point, lines):
    x, y = point
    values = []
    if x > 0:
        values.append(lines[x-1][y])
    if x < len(lines)-1:
        values.append(lines[x+1][y])
    if y > 0:
        values.append(lines[x][y-1])
    if y < len(lines[0])-1:
        values.append(lines[x][y+1])
    
    return values

low_points = {}
for y, line in enumerate(lines):
    for x, point in enumerate(line):
        if lines[y][x] < min(get_surrounding_point_values((y,x), lines)):
            low_points[(y,x)] = int(lines[y][x]) + 1

print(sum(low_points.values()))

# part 2
# for each low point, get its surrounding points
# for each surrounding point that isn't a 9
# scan it's surrounding points that arent a 9
# repeat until no more surrounding non-9 points are found

def get_surrounding_basin_points(points, lines):
    points = [p for p in points if p not in visited]
    new_points = []
    for x,y in points:
        visited.append((x, y))
        new_points.append((x,y))
        if x > 0:
            if lines[x-1][y] != "9":
                new_points.append((x-1, y))
        if x < len(lines)-1:
            if lines[x+1][y] != "9":
                new_points.append((x+1, y))
        if y > 0:
            if lines[x][y-1] != "9":
                new_points.append((x, y-1))
        if y < len(lines[0])-1:
            if lines[x][y+1] != "9":
                new_points.append((x, y+1))
        get_surrounding_basin_points(new_points, lines)

    return visited

basin_points = []

for x, y in low_points.keys():
    visited = []
    basin = get_surrounding_basin_points([(x,y)], lines)
    basin_points.append(basin)

basin_sizes = [len(set(b)) for b in basin_points]
basin_sizes = sorted(basin_sizes, reverse=True)

print(reduce(lambda x,y: x*y, basin_sizes[:3]))