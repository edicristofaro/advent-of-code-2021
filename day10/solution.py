with open("input.txt", "r") as f:
    subsystem = [l.strip("\n") for l in f.readlines()]

openers = ["{", "[", "<", "("]
closers = ["}", "]", ">", ")"]
opposite = {"[": "]", "(": ")", "{": "}", "<": ">"}
values = {")": 3, "]": 57, "}": 1197, ">": 25137}

# part 1
# for part 2, made copy of subsystem - running the same corruption scan, and if its corrupt it's popped from the incomplete list,
# since the problem says we can discard the corrupted lines
illegal_closers = []
incomplete_lines = subsystem.copy()
for l in subsystem:
    open_stack = []
    for s in l:
        if s in openers:
            open_stack.append(s)
        elif s in closers:
            if len(open_stack) > 0:
                if opposite[open_stack[-1]] == s:
                    open_stack.pop()
                else:
                    illegal_closers.append(s)
                    incomplete_lines.remove(l)
                    break

print(sum(values[c] for c in illegal_closers))

# part 2
completion_additions = []
for l in incomplete_lines:
    open_stack = []
    for s in l:
        if s in openers:
            open_stack.append(s)
        elif s in closers:
            if len(open_stack) > 0:
                if opposite[open_stack[-1]] == s:
                    open_stack.pop()
    completed_segment = ""
    for s in open_stack:
        completed_segment = completed_segment + opposite[s]
    completion_additions.append(completed_segment[::-1])


def score_part_2(line):
    score = 0
    values = {")": 1, "]": 2, "}": 3, ">": 4}

    for s in line:
        score *= 5
        score += values[s]

    return score


scores = []
for l in completion_additions:
    scores.append(score_part_2(l))

print(sorted(scores)[len(scores) // 2])

"""
part 2 has a scoring function, part 1 doesn't - ugly, but works
"""
