import matplotlib
import sys
matplotlib.use('Agg')
import matplotlib.pyplot as plt


with open("input.txt", "r") as f:
    data = f.readlines()

dots = []
folds = []
for p in data:
    p = p.strip("\n")
    if "fold along" in p:
        p = p.split("fold along")[1].strip().split("=")
        folds.append((str(p[0]), int(p[1])))
    elif p:
        dots.append(tuple(map(int, p.split(","))))

def fold_up(dots, y_intercept):
    folded_dots = []

    # keep everything above the fold in place
    for dot in dots:
        if dot[1] <= y_intercept:
            folded_dots.append(dot)
        else:
            delta = dot[1] - y_intercept
            folded_point = (dot[0], y_intercept - delta)
            if folded_point not in folded_dots:
                folded_dots.append(folded_point)

    return folded_dots

def fold_left(dots, x_intercept):
    folded_dots = []

    # keep everything above the fold in place
    for dot in dots:
        if dot[0] <= x_intercept:
            folded_dots.append(dot)
        else:
            delta = dot[0] - x_intercept
            folded_point = (x_intercept - delta, dot[1])
            if folded_point not in folded_dots:
                folded_dots.append(folded_point)

    return folded_dots

# part 1
folded = fold_left(dots, 655)
print(len(folded))

#part 2
folded = dots
for fold in folds:
    if fold[0] == "x":
        folded = fold_left(folded, fold[1])
    else:
        folded = fold_up(folded, fold[1])

plt.scatter([x[0] for x in folded], [y[1] for y in folded])
sys.stdout.flush()
plt.savefig(sys.stdout.buffer)
# redirect the output to a .png file - it needs to be flipped, and easier to read if you compress the vertical axis a bit