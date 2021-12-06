from typing import List


class Point(object):
    def __init__(self, coords: List):
        self.x = int(coords[0])
        self.y = int(coords[1])

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return "Line({}, {})".format(self.start, self.end)

    def __hash__(self):
        return hash((self.start, self.end))

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_horizontal(self):
        return self.start.y == self.end.y

    @property
    def points_occupied(self):
        if self.is_vertical():
            if self.start.y > self.end.y:
                inc = -1
            else:
                inc = 1
            return [
                Point((self.start.x, y))
                for y in range(self.start.y, self.end.y + inc, inc)
            ]
        elif self.is_horizontal():
            if self.start.x > self.end.x:
                inc = -1
            else:
                inc = 1
            return [
                Point((x, self.start.y))
                for x in range(self.start.x, self.end.x + inc, inc)
            ]
        else:
            # part 2 -- handle 45 degree diagonals
            # this is so bad. I'm using sets to eliminate duplicates instead of actually fixing my code.
            points = []
            slope = (self.end.y - self.start.y) // (self.end.x - self.start.x)
            if self.start.x > self.end.x:
                start_x, end_x = self.end.x, self.start.x
                start_y, end_y = self.end.y, self.start.y
            else:
                start_x, end_x = self.start.x, self.end.x
                start_y, end_y = self.start.y, self.end.y
            for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
                points.append(Point((i, j)))
                points.append(self.start)
                points.append(self.end)
            return list(set(points))


with open("input.txt", "r") as f:
    contents = f.readlines()

strsegs = [c.strip("\n").split(" -> ") for c in contents]
points = []
seg = []
lines = []

for s in strsegs:
    for i, p in enumerate(s):
        seg.append(Point(p.split(",")))
        if (i + 1) % 2 == 0:
            points.append(seg)
            seg = []

for l in points:
    lines.append(Line(l[0], l[1]))

# up to this point, modeling as points and lines
# i'm sure there's an algorithm to calculate intersection, but i'm not sure how to do it
# since points are discrete and integers here, instead we'll enumerate the points occupied by
# each horizontal or vertical line, and iterate progressively through the list of lines
# to find intersections based on one line containing the same points as another -
# we'll skip double-counting by only checking each line once and shortening the loop


# part 1 ---

# between the sample and actual input, there's a difference in that the real input provides an
# opportunity to double-count intersecting points. the right answer is unique intersections,
# so use a set to fix that
def count_intersections(lines: List[Line]) -> int:
    intersections = set()
    for i, l1 in enumerate(lines):
        for l2 in lines[i + 1 :]:
            intersecting_points = list(
                set(l1.points_occupied) & set(l2.points_occupied)
            )
            if intersecting_points:
                intersections.update(intersecting_points)

    return len(intersections)


no_diagonals = [l for l in lines if l.is_vertical() or l.is_horizontal()]

print(count_intersections(no_diagonals))

# part 2 ---

# now we include diagonals (which can only be 45 degrees, thankfully), and somehow we got lucky
# in how we approached the abstraction of lines. this should be just extending our Line class
# to enumerate occupied points on a diagonal line then re-using the count_intersections function

print(count_intersections(lines))

# this whole thing is embarrassingly slow. i'm pretty sure that the `points_occupied` method is
# being recalculated every time we loop through the lines. i'm also using sets as a serious crutch.
# it calculates correctly, but i'd fix these in a real setting.
